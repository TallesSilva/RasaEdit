import os
import json
import bson
import glob
import itertools
import datetime
import shutil

from docxtpl import DocxTemplate
from relatorio.templates.opendocument import Template
from secretary import Renderer

from ..models import (
    Document as DocumentModel,
    Template as TemplateModel
)

class DocumentTemplate():
    """
    ## Class to manipulate document templates.
    ### This class uses the ´docxtpl´ library for Microsoft Office files \
    and the ´relatorio´ library for Open Document files.
    This class uses ´unoconv´ for converting between file formats (.odt, .docx and .pdf).
    Must have LibreOffice's or OpenOffice's UNO bindings installed (http://dag.wiee.rs/home-made/unoconv).

    The templates' files and directories MUST follow the structure::
        Templates/
        |   {{TEMPLATE_NAME}}/
        |   |   {{TEMPLATE_NAME}}.{{FILE_FORMAT}}
        |   |   {{TEMPLATE_NAME}}.json

    The template's JSON file MUST be in the following pattern::
    Field types:
        - text
        - image
        - boolean
        - topic (used for subtopics creation)
        - repeat (used for iterating the subfields, such like table rows)
    *** It's recommended that field names use "snake_case" naming convention (lowercase words separated by underscore) ***
        {
            "template": "{{TEMPLATE_NAME}}",
            "fields": [
                {
                    "field": "{{FIELD_1}}",
                    "hint": "{{HINT_TEXT_1}}",
                    "type": "text"
                },
                {
                    "field": "{{FIELD_2}}",
                    "hint": "{{HINT_TEXT_2}}",
                    "type": "image"
                },
                {
                    "field": "{{FIELD_3}}",
                    "type": "repeat" or "topic",
                    "fields": [
                        {
                            "field": "{{SUB_FIELD_1}}",
                            "hint": "{{HINT_1}}",
                            "type": "text"
                        }
                        ...
                        {
                          "field": "{{SUB_FIELD_N}}",
                          "hint": "{{HINT_N}}",
                          "type": "text"
                        }
                    ]
                }
                ...
                {
                    "field": "{{FIELD_N}}",
                    "hint": "{{HINT_TEXT_N}}",
                    "type": "text"
                }
            ]
        }
    """

    _CONVERT_COMMAND = 'unoconv -f {out_format} -o {output} {input}'
    ODF_FORMATS = ['odt']
    OFFICE_FORMATS = ['docx']
    OTHER_FORMATS = ['pdf']
    SUPPORTED_INPUT_FORMATS = ODF_FORMATS + OFFICE_FORMATS
    SUPPORTED_OUTPUT_FORMATS = SUPPORTED_INPUT_FORMATS + OTHER_FORMATS

    def __init__(self):
        self.pwd = os.path.dirname(os.path.abspath(__file__))
        self._templates_path = 'templates'
        self._output_path = 'output'

    def _open_template(self, template: TemplateModel, file_format=None) -> None:
        '''
        Opens a template for document manipulation. The ´file_format´ argument is optional.
        '''
        template_name = template.file

        if file_format:
            self.file_format = file_format
        else:
            templates = self._list_files(
                files_path=f'{self.pwd}/{self._templates_path}/{template_name}',
                file_formats=self.SUPPORTED_INPUT_FORMATS
            )
            template = templates[0]
            self.file_format = template.split('.')[-1]
            del templates, template

        self.template_name = template_name
        self.path = f'{self.pwd}/{self._templates_path}/{template_name}/{template_name}.{self.file_format}'

        if(self.file_format in self.ODF_FORMATS):
            # using relatorio
            # self._file = Template(source='', filepath=self.path)

            # using secretary
            self._file = Renderer()
        elif(self.file_format in self.OFFICE_FORMATS):
            self._file = DocxTemplate(self.path)
        else:
            raise TypeError(
                'The file format is invalid or it is not supported.')

        try:
            self.info_path = f'{self.pwd}/{self._templates_path}/{template_name}/{template_name}.json'
            with open(self.info_path, 'r') as f:
                self.info = json.load(f)
        except Exception as e:
            raise e

    def _save(self, file_name: str, to_json: bool = True) -> str:
        '''
        Saves the document as a file. Check ´SUPPORTED_OUTPUT_FORMATS´ attribute for supported file formats.
        '''
        #print(json.dumps(self.fields, indent=4))

        out_path = f'{self.pwd}/{self._output_path}/{file_name}/{file_name}.{self.file_format}'
        os.makedirs(f'{self.pwd}/{self._output_path}/{file_name}', exist_ok=True)
        if(self.file_format in self.OFFICE_FORMATS):
            # _file of type 'DocxTemplate' (docxtpl)
            self._file.render(self.fields)
            self._file.save(out_path)
        elif(self.file_format in self.ODF_FORMATS):
            # using relatorio
            #result = self._file.generate(**self.fields).render()

            # _file of type 'Renderer' (secretary)
            result = self._file.render(self.path, **self.fields)

            with open(out_path, 'wb') as f:
                f.write(result)
        else:
            raise TypeError(
                'The file format is invalid or it is not supported.')

        return out_path

    def _list_files(self, files_path: str, file_formats: list) -> list:
        files_path = files_path + '/' if files_path[-1] != '/' else files_path
        file_formats_original = file_formats
        file_formats = ['*.' + format if format[0] !=
                        '.' else '*' + format for format in file_formats]
        # Returns a list of lists with file paths
        files = [glob.glob(f'{files_path}{e}') for e in file_formats]
        # Flattening 'files' list of lists
        files = list(itertools.chain(*files))
        if not files:
            raise TypeError(
                f'No file format ({file_formats_original}) was found in the path "{files_path}".')
        return files

    @staticmethod
    def delete(path: str):
        path = '/'.join(path.split('/')[0:-1])
        shutil.rmtree(path, ignore_errors=True)

    def retrieve(self, doc: DocumentModel, *args):
        """
        """
        self._open_template(template=doc.template, file_format=doc.format)
        self.fields = doc.fields
        return self._save(doc.name)
