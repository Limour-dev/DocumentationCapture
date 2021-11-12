from psutil import disk_partitions
import winreg
import os

def getUsb():
    res = []
    for item in disk_partitions():
        if 'removable' in item.opts:
            res.append((item.device, item.opts))
    return res

def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key, "Desktop")[0]

def fendswith(special_file, suffix):
    for suf in suffix:
        if special_file.endswith(suf):
            return True
    return False

def scan_files(directory, suffix = ['.ppt', '.pptx', '.pdf', '.doc', '.docx']):
    files_list=[]
    
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if special_file.startswith('~$'):
                continue
            if fendswith(special_file.lower(), suffix):
                files_list.append(os.path.join(root,special_file))

    return files_list

def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    return fsize

def limitFileSize(files, fsize = 10000):
    files_list = []
    for special_file in files:
        if not os.path.exists(special_file):
            continue
        if (tmp:= get_FileSize(special_file)) > fsize:
            files_list.append((special_file, tmp))
    return files_list

