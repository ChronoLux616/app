import smtplib
from email.mime.text import MIMEText


EMAIL_HOST = 'smtp.xx.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'email'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_TO = 'addressee'


def send_email():
    try:
        mailServer = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        print('Conectado...')

        mensaje = MIMEText(""" Este es un mensaje de Prueba :)""")
        mensaje['From'] = EMAIL_HOST_USER
        mensaje['To'] = EMAIL_TO
        mensaje['Subject'] = "Tienes un nuevo correo"

        mailServer.sendmail(EMAIL_HOST_USER, EMAIL_TO, mensaje.as_string())

        print("Correo enviado")
    except Exception as e:
        print(e)


send_email()
