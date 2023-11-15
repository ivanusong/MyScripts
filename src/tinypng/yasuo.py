#!/Users/ivan/Desktop/MyScripts/venv/bin/python3

# 需要更高级的参数开发可以参考以下地址:
# https://tinypng.com/developers/reference/python

import tinify
tinify.key = "jbtT9C0H-zhPajOkfzlGy0rrGBSfOpXD"

import sys
import re

def compress_pic(pic):
    tex = re.findall(r'(.*)\.(.*)', pic)
    文件名 = tex[0][0]
    扩展名 = tex[0][1]
    source = tinify.from_file(pic)
    source.to_file(f'{文件名}_compressed.{扩展名}')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('缺少参数')
        exit(0)
    pic = sys.argv[1]
    compress_pic(pic)
    print('搞掂!')
