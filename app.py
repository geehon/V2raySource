#!/usr/bin/env python
import requests
import re
import pyperclip
import tkinter
import tkinter.messagebox


def main():
    try:
        r = requests.get('https://view.freev2ray.org/', timeout=2)
        if r.status_code == 200:
            try:
                vmess = get_str(r.text)
            except AttributeError:
                tkinter.messagebox.showinfo('提示', '匹配不到vemss')
            else:
                dd = pyperclip.copy(vmess)
                tkinter.messagebox.showinfo('提示', '获取成功')
        else:
            tkinter.messagebox.showinfo('提示', '获取失败')
    except requests.exceptions.ConnectionError:
        tkinter.messagebox.showinfo('提示', '网络异常')


def get_str(str):
    str = re.search("(vmess://[\w+]*)", str).group()
    return str


if __name__ == "__main__":
    main()
