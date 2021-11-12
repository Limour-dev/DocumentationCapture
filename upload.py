from aligo import Aligo
from smtpinfo import sentMail
from sys import exit as sys_exit
import time
import tempfile
import os

today = time.strftime("%Y-%m-%d", time.localtime())

ali = Aligo()
root = ali.create_folder('DocumentationCapture', check_name_mode='refuse').file_id
root = ali.create_folder(today, check_name_mode='refuse', parent_file_id=root).file_id

def getSuffix(path):
    return os.path.splitext(path)[-1]

def preForUp(path):
    tmp = tempfile.mkstemp(suffix=getSuffix(path))
    with open(path, 'rb') as f:
        tmpf = f.read()
    with open(tmp[1], 'wb') as f:
        f.write(tmpf)
    return tmp

def uploadf(path):
    tmp = preForUp(path)[1]
    file_id = ali.upload_file(tmp, parent_file_id=root).file_id
    sentMail(f"uploadf {path}", file_id)
    
