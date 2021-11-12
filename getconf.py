from json import loads as json_loads
from sys import argv as sys_argv

if len(sys_argv) >=2:
    path = sys_argv[1]
else:
    path = 'conf.json'

print(path)

with open(path, encoding='utf-8') as f:
    config = json_loads(f.read())
