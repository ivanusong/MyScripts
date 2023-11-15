#!/Users/ivan/Desktop/MyScripts/venv/bin/python3

from PIL import Image as img
import sys
import os
import re

work_path = os.path.dirname(os.readlink(__file__)) if os.path.islink(__file__) else os.path.dirname(__file__)
os.chdir(work_path)

# 加载一些静态资源: 读取底图、遮罩图
iPhone_img = img.open(os.path.join(work_path, 'iPhone13mini.png'))  
Mask_img = img.open(os.path.join(work_path, 'iPhone13mini_mask.png'))

# 主函数
def mask_img(img_path):
    screen_img = img.open(img_path) # 获取手机截图
    screen_img = screen_img.resize((760, 1642))  # 重设截图尺寸
    if screen_img.size == Mask_img.size:
        iPhone_img.paste(screen_img, (94, 80), Mask_img)
        文件名 = re.findall(r'(.*)\.(.*)', img_path)[0][0]
        # 文件名 = img_path.split(".")[-2]
        iPhone_img.save(文件名 + "_mockup.png",'png')
        return True
    else:
        return screen_img


if __name__ == "__main__":
    # p = '/Users/ivan/Desktop/iShot_2023-11-13_16.27.48.jpg'
    if len(sys.argv) == 1:
        print("请传入截图路径")
    else:
        mask_img(sys.argv[1])
