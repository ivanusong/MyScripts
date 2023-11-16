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


{'data': {'logs': [{'filename': '<system>', 'timestamp': '08:59:03.131', 'unix_time': 1700096343131, 'level': 'info', 'args': ['脚本环境初始化...']}, {'filename': '<system>', 'timestamp': '08:59:03.133', 'unix_time': 1700096343133, 'level': 'info', 'args': ['已开始执行']}, {'filename': '<system>', 'timestamp': '08:59:03.160', 'unix_time': 1700096343160, 'level': 'info', 'args': ['执行完毕']}], 'result': '[{"姓名":"姓名","年龄":"年龄","性别":"性别"},{"姓名":"神灯","年龄":"男","性别":"送到"},{"姓名":"东方赛","年龄":"腮风赛","性别":"塞给"}]'}, 'error': '', 'status': 'finished'}