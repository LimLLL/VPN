from pathlib import Path
import os
import subprocess

# Clone the repository and copy files
subprocess.run(['git', 'clone', '--branch=release', 'https://github.com/Loyalsoldier/geoip', '/tmp/geoip'])
subprocess.run(['cp', '/tmp/geoip/text/*', './pure_text_ip'], shell=True)

path = './pure_text_ip'

# 读取所有文件名
def read_file_name(path):
    p = Path(path)
    return [x for x in p.iterdir() if x.is_file()]

all_ips_exclude_china = ''
for file in read_file_name(path):
    if not file.name.endswith('cn.txt'):
        with open(file, 'r') as f:
            all_ips_exclude_china += f.read()
    else:
        print('skip file: ' + file.name)

with open('./pure_text_ip/geoip_exclude_china.txt', 'w') as f:
    f.write(all_ips_exclude_china)