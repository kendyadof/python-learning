# enviando emails smtp com python
import os
import pathlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import smtplib
from dotenv import load_dotenv # type:ignore
load_dotenv()

# caminho arquivo
CAMINHO = pathlib.Path(__file__).parent / 'aula185.html' # pode ser .txt

# dados do remetente e destinatario
remetente = os.getenv("FROM_EMAIL","")
destinatario = remetente
# configurações do servidor smtp
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = os.getenv("FROM_EMAIL","")
smtp_password = os.getenv("EMAIL_PASSWORD","")

# Msg de texto
with open(CAMINHO, "r") as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome="Joao")

print(texto_email)

# transformar mensagem em MIMEMultipart
# from # to # subject
mime_multipart = MIMEMultipart()
mime_multipart["from"] = remetente
mime_multipart["to"] = destinatario
mime_multipart["subject"] = "assunto"

corpo_email = MIMEText(texto_email, "html", "utf-8") # ou "html" ao inves de plain
mime_multipart.attach(corpo_email)

# envia o email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo() # extended hello
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print("Email enfaggot com sucesso")