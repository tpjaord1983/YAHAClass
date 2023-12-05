import pyautogui
import time
import random
#执行命令后，有3秒的准备时间用于切换光标的焦点
time.sleep(3) 
#此处的index.html文件，就是你需要输入内容的来源文件
with open('index.html', 'r', encoding='utf-8') as file: 

    lines = file.readlines()

# 计算需要滚动的行数
scroll_line = 0

# 设置一个标志来判断是第一次滚动还是后续的滚动
first_scroll = True

# 对每一行进行处理
for line in lines:

    # 一次输入一个字符
    for char in line:
        pyautogui.write(char)
        time.sleep(random.random() * 0.22)  # 间隔是一个最大为0.5秒的随机数
    
    scroll_line += 1  # 在处理完一行后，才增加滚动行数

    # 每输入15行，第一次滚动4次屏幕，后续每输入10行滚动10次屏幕
    if first_scroll and scroll_line >= 15:
        for _ in range(4):  # 鼠标滚动4次
            pyautogui.scroll(-50)
        scroll_line = 0  # 滚动结束后，重新计算输入行数
        first_scroll = False  # 重置标志变量，以便下次滚动10行
    elif not first_scroll and scroll_line >= 10:
        for _ in range(10):  # 鼠标滚动10次
            pyautogui.scroll(-50)
        scroll_line = 0  # 滚动结束后，重新计算输入行数

pyautogui.hotkey('ctrl', 's')