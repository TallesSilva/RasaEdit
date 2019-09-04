import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from typing import List

# Configurações de Conexão
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
username = 'luna.ged.kyros@gmail.com'
password = 'Luna@123'
from_addr = 'luna.ged.kyros@gmail.com'


# Função para envio de e-mail com anexo
def envia_email(to_addrs: List[str], file_path) -> bool:
    # Abrindo arquivo que será anexado:
    filename = file_path.split('/')[-1]
    attachment = open(file_path, 'rb')

    # Definindo atributos do email:
    message = MIMEMultipart()
    message['subject'] = '[Documento] ' + filename
    message['from'] = 'Luna GED Kyros'
    message['to'] = ', '.join(to_addrs)

    # Corpo do email:
    body = """Olá,\n\nSegue em anexo o documento que você solicitou!\n\nAtt.\nLuna"""
    message.attach(MIMEText(body,'plain'))

    # Anexando Arquivo:
    mime = MIMEBase('application', 'octet-stream')
    mime.set_payload(attachment.read())
    encoders.encode_base64(mime)
    mime.add_header('Content-Disposition',"attachment; filename= " + filename)
    message.attach(mime)

    # Iniciando conexão com o servidor SMTP:
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)

    # Enviando email e encerrando conexão:
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()
    return True
