from systeminfo import get_systeminfo
from getconf import config
sign = "\n" + get_systeminfo()

import smtplib
from email.mime.text import MIMEText
from email.header import Header

from_addr = config['mail']
password = config['password']
to_addr = config['recipient']
smtp_server = config['smtphost']
port = config['smtpport']

def sentMail(head, text):
    if not head:
        head = get_systeminfo()
    msg = MIMEText(text + sign,'plain','utf-8')
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header(head)
    try:
        server = smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server, port)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
    except:
        print('sending mail failed!')

sentMail('HostOnline', 'starting smtpService')
