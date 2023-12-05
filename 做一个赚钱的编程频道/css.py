import pyautogui
import time
import random
import os

time.sleep(3)

file_index = 1

while True:
    filename = f"{file_index}.css"

    # 检查文件是否存在
    if not os.path.exists(filename):
        print(f"File {filename} not found, stopping script.")
        break

    print(f"Processing file {filename}")

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    scroll_line = 0
    first_scroll = True

    # 对每一行进行处理
    for line in lines:
        # 一次输入一个字符
        for char in line:
            pyautogui.write(char)
            time.sleep(random.random() * 0.01)  # 间隔是一个最大为0.01秒的随机数

        scroll_line += 1  # 在处理完一行后，才增加滚动行数

        # 滚动逻辑
        if first_scroll and scroll_line >= 15:
            for _ in range(4):
                pyautogui.scroll(-50)
            scroll_line = 0
            first_scroll = False
        elif not first_scroll and scroll_line >= 10:
            for _ in range(10):
                pyautogui.scroll(-50)
            scroll_line = 0

    # 执行保存操作
    pyautogui.hotkey('ctrl', 's')
    print(f"File {filename} processed and saved.")

    # 等待2秒
    time.sleep(2)

    # 移动到下一个文件
    file_index += 1
