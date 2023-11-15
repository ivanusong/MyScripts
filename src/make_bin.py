#!/usr/bin/env python3
# 该脚本用于生成二进制文件的软链接以及修复虚拟 python 环境

import os

def repair_env_pip():
    """修复 pip 依赖的环境"""
    file_list = []
    for root, dirs, files in os.walk("venv/bin"):  # 获取bin目录下的全部含有pip名字的文件路径
        for file in files:
            if "pip" in file:
                file_list.append(os.path.abspath(os.path.join(root, file)))
    for file in file_list:    # 循环修改每一个pip虚拟环境的第一行 shebang
        python_path = os.path.join(os.getcwd(), "venv/bin/python3")
        with open(file, "r") as f:
            lines = f.readlines()
        with open(file, "w") as f:
            lines[0] = "#!" + python_path + "\n"
            f.writelines(lines)

def repair_env_path():
    """修改脚本的执行环境为最新的虚拟环境"""
    now_python_path = os.path.join(os.getcwd(), "venv/bin/python3")
    Shebang = "#!" + now_python_path
    for cmd,path in cmd_list.items():
        file_path = os.path.join(os.getcwd(), "src", path)
        print(file_path)
        with open(file_path, "r") as f:
            lines = f.readlines()
        with open(file_path, "w") as f:
            lines[0] = Shebang + "\n"
            f.writelines(lines)

def make_bins(dict):
    bin_path = os.path.join(os.getcwd(), "bin")  # 获取当前bin二进制文件目录
    for cmd,path in dict.items():
        cmd_path = os.path.join(bin_path, cmd)  # 组合出软链目标路径
        file_path = os.path.join(os.getcwd(), "src", path)   # 组合出软链源文件路径
        if os.path.exists(cmd_path):   # 如果原来有软链
            os.remove(cmd_path)  # 移除原来的软链
        os.symlink(os.path.abspath(file_path), cmd_path)  # 创建软链
        os.chmod(cmd_path, 0o777) # 设置二进制软链的可执行权限

if __name__ == "__main__":
    repair_env_pip()  # 修复虚拟环境的 pip 路径
    repair_env_path()  # 执行修复环境脚本，修复因为移动或改名产生的虚拟目录变化
    cmd_list = {
        "mask": "screener/mask.py",
        "removebg": "removebg/removebg.py",
        "bigger": "picbigger/bigger.py",
    }
    make_bins(cmd_list)  # 创建上方定义好的命令与链接软链, 并设置可执行权限等
