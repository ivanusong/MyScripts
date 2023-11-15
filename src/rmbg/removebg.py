#!/Users/ivan/Desktop/MyScripts/venv/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import re

work_path = os.path.dirname(os.readlink(__file__)) if os.path.islink(__file__) else os.path.dirname(__file__)
os.chdir(work_path)


def bigger_pic(pic):
    tex = re.findall(r'(.*)\.(.*)', pic)
    文件名 = tex[0][0]
    # 扩展名 = tex[0][1]
    # ext = fullfilename[1]
    now_python_path = os.path.join(work_path, "../../venv/bin/python3")
    # print(now_python_path)
    cmd = f'{now_python_path} -m backgroundremover.cmd.cli -i "{pic}" -o "{文件名}"_nobg.png'
    os.system(cmd)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('缺少参数')
        exit(0)
    pic = sys.argv[1]
    bigger_pic(pic)
