#!/Users/ivan/Desktop/MyScripts/venv/bin/python3

import sys
import os
import re

work_path = os.path.dirname(os.readlink(__file__)) if os.path.islink(__file__) else os.path.dirname(__file__)
os.chdir(work_path)
cmd_path = f"{work_path}/realesrgan-ncnn-vulkan"

def bigger_pic(pic, scale):
    tex = re.findall(r'(.*)\.(.*)', pic)
    文件名 = tex[0][0]
    扩展名 = tex[0][1]
    cmd = f'"{cmd_path}" -i "{pic}" -o "{文件名}_x{scale}.{扩展名}" -f {扩展名} -n realesr-animevideov3-x{scale} -s {scale}'
    os.system(cmd)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('缺少参数')
        exit(0)
    pic = sys.argv[1]
    scale = sys.argv[2]
    bigger_pic(pic, scale)
    print('搞掂!')
