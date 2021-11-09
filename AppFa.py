# -*- encoding: utf-8 -*-
"""
@File    : AppFa.py
@Time    : 2021/11/8 17:39
@Author  : Jingmo
@Software: PyCharm
"""
import os
import tkinter
from threading import Thread
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename


def exio():
    os.popen('adb kill-server')
    os.popen(f'taskkill /f /im adb.exe')
    os.popen(f'taskkill /f /im cmd.exe')


def delButton(tree):
    x = tree.get_children()
    for item in x:
        tree.delete(item)


def disanfang():
    delButton(tree)
    app_all_list = os.popen('adb shell pm list packages -3').read()
    apps_list = app_all_list.split('package:')
    app_list = [x.strip() for x in apps_list if x.strip() != '']
    ind = 0
    for i in app_list:
        appname = os.popen(f'adb shell pm path {i}').read().split('/')[-1]
        ind += 1
        tree.insert("", ind, text=f"{ind}", values=(ind, appname, i))  # #给第0行添加数据，索引值可重复


def xitongyinyong():
    delButton(tree)
    app_all_list = os.popen('adb shell pm list packages -s').read()
    apps_list = app_all_list.split('package:')
    app_list = [x.strip() for x in apps_list if x.strip() != '']
    ind = 0
    for i in app_list:
        appname = os.popen(f'adb shell pm path {i}').read().split('/')[-1]
        ind += 1
        tree.insert("", ind, text=f"{ind}", values=(ind, appname, i))  # #给第0行添加数据，索引值可重复


def qiyong():
    delButton(tree)
    app_all_list = os.popen('adb shell pm list packages -e').read()
    apps_list = app_all_list.split('package:')
    app_list = [x.strip() for x in apps_list if x.strip() != '']
    ind = 0
    for i in app_list:
        appname = os.popen(f'adb shell pm path {i}').read().split('/')[-1]
        ind += 1
        tree.insert("", ind, text=f"{ind}", values=(ind, appname, i))  # #给第0行添加数据，索引值可重复


def tinyong():
    delButton(tree)
    app_all_list = os.popen('adb shell pm list packages -d').read()
    apps_list = app_all_list.split('package:')
    app_list = [x.strip() for x in apps_list if x.strip() != '']
    ind = 0
    for i in app_list:
        appname = os.popen(f'adb shell pm path {i}').read().split('/')[-1]
        ind += 1
        tree.insert("", ind, text=f"{ind}", values=(ind, appname, i))  # #给第0行添加数据，索引值可重复


def suoyouyinyong():
    delButton(tree)
    app_all_list = os.popen('adb shell pm list packages').read()
    apps_list = app_all_list.split('package:')
    app_list = [x.strip() for x in apps_list if x.strip() != '']
    ind = 0
    for i in app_list:
        appname = os.popen(f'adb shell pm path {i}').read().split('/')[-1]
        ind += 1
        tree.insert("", ind, text=f"{ind}", values=(ind, appname, i))  # #给第0行添加数据，索引值可重复


def biaoge(get_xaunze_):
    # ('第三方应用', '系统应用', '已启用的应用', '已停用的应用', '所有应用包名')
    if get_xaunze_ == "第三方应用":
        disanfang()

    if get_xaunze_ == "系统应用":
        xitongyinyong()

    if get_xaunze_ == "已启用的应用":
        qiyong()

    if get_xaunze_ == "已停用的应用":
        tinyong()

    if get_xaunze_ == "所有应用包名":
        suoyouyinyong()


def zhiing_star():
    Thread(target=zhixing_).start()


def zhixing_():
    def zhixing_star(app_pkg):
        get_cmb = cmb.get()
        if get_cmb == "卸载":
            # adb shell pm uninstall[-k][--user USER_ID] 包名
            # -k 卸载应用且保留数据与缓存，如果不加 - k 则全部删除。
            # –user指定用户 id，Android系统支持多个用户，默认用户只有一个，id = 0。
            a1 = messagebox.askokcancel('提示', f'确认卸载：{app_pkg}')
            if a1 == True:
                cmd_0 = f"adb shell pm uninstall --user 0 {app_pkg}"
                print(cmd_0)
                os.popen(cmd_0)

        if get_cmb == "停用":
            a2 = messagebox.askokcancel('提示', f'确认停用：{app_pkg}')
            if a2 == True:
                cmd_1 = f"adb shell pm disable-user {app_pkg}"
                print(cmd_1)
                os.popen(cmd_1)

        if get_cmb == "启用":
            # 列出所有停用名单
            # adb shell pm list packages -d
            a3 = messagebox.askokcancel('提示', f'确认启用：{app_pkg}')
            if a3 == True:
                cmd_2 = f"adb shell pm enable -d {app_pkg}"
                print(cmd_2)
                os.popen(cmd_2)
    try:
        for item in tree.selection():
            item_text = tree.item(item, "values")
            print(item_text[2])  # 输出所选行的第一列的值
            Thread(target=zhixing_star, args=(item_text[2],)).start()
    except:
        messagebox.askokcancel('错误', "请在【表格中】选择需要执行操作的项目")


def chaxun():
    delButton(tree)
    os.popen(f'taskkill /f /im cmd.exe')
    get_xaunze_ = xaunze_.get()
    Thread(target=biaoge, args=(get_xaunze_,)).start()


def stare_app():
    delButton(tree)
    xuliehao = os.popen('adb devices').read()
    phone =  os.popen('adb shell getprop ro.product.model').read()
    lianjie = messagebox.askokcancel('链接 提示',
                                     phone + xuliehao +
                                     "显示【手机型号】和【序列号】点击确认即可\n请否则开启手机【USb调试】相关功能, 正确链接手机\n点击取消 退出程序")
    if lianjie == False:
        root.destroy()
        exit()
    get_xaunze_ = xaunze_.get()
    Thread(target=biaoge, args=(get_xaunze_,)).start()


def jiangjianzuhang():
    def jiangjianzhuang_star():
        delButton(tree)
        os.popen(f'taskkill /f /im cmd.exe')
        apk = askopenfilename(title='选择需要安装的文件 [ apk ]', initialdir='/', filetypes=[('Android File', '*.apk')])
        apkinfo = os.popen(f'adb install -r -d {apk}').read()
        messagebox.askokcancel('显示 success 则表示安装完成', f'{apkinfo}')
    Thread(target=jiangjianzhuang_star).start()


if __name__ == '__main__':
    os.popen('mode con cols=50 lines=10')
    try:
        root = tkinter.Tk()
        root.title("ADB手机应用管理工具")  # #窗口标题
        root.geometry("700x400+700+200")  # #窗口位置500后面是字母x
        root.resizable(False, False)

        # 表格
        tree = ttk.Treeview(root, height=10, show="headings", )  # #创建表格对象
        tree["columns"] = ("序号", "安装包（参考）", "包名")  # #定义列
        tree.column("序号", width=60)  # #设置列
        tree.column("安装包（参考）", width=280)
        tree.column("包名", width=360)

        tree.heading("序号", text="序号")  # #设置显示的表头名
        tree.heading("安装包（参考）", text="安装包（应用名仅供参考无法准确获取）")
        tree.heading("包名", text="应用包名-讲道理，全部无误")

        VScroll1 = ttk.Scrollbar(tree, orient='vertical', command=tree.yview)
        VScroll1.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
        # 给treeview添加配置
        tree.configure(yscrollcommand=VScroll1.set)
        tree.place(x=0, y=60)

        # 创建下拉菜单
        xaunze_ = ttk.Combobox(root, font=('微软雅黑', 14), width=14, state="readonly")
        # 设置下拉菜单中的值
        xaunze_['value'] = ('第三方应用', '系统应用', '已启用的应用', '已停用的应用', '所有应用包名')
        # 设置默认值，即默认下拉框中的内容
        xaunze_.current(0)
        xaunze_.place(x=20, y=10)

        # 创建下拉菜单
        cmb = ttk.Combobox(root, font=('微软雅黑', 14), width=8, state="readonly")
        # 设置下拉菜单中的值
        cmb['value'] = ('卸载', '停用', '启用')
        # 设置默认值，即默认下拉框中的内容
        cmb.current(1)
        cmb.place(x=40, y=320)

        zhixing = tkinter.Button(root, text="↑ 执行", font=('微软雅黑', 12), width=10, command=zhiing_star)
        zhixing.config(fg="red", bg="white")
        zhixing.place(x=160, y=314)

        jiangji = tkinter.Button(root, text="降级安装（保留数据）", font=('微软雅黑', 12), command=jiangjianzuhang)
        jiangji.config(fg="black", bg="white")
        jiangji.place(x=500, y=310)

        jieshu = tkinter.Button(root, text="关闭ADB服务", font=('微软雅黑', 12), command=exio)
        jieshu.config(fg="black", bg="white")
        jieshu.place(x=580, y=10)

        chaxunde_ = tkinter.Button(root, text="查询", font=('微软雅黑', 12), command=stare_app())
        chaxunde = tkinter.Button(root, text="查询", font=('微软雅黑', 12), width=10, command=chaxun)
        chaxunde.config(fg="green", bg="white")
        chaxunde.place(x=240, y=10)

        root.mainloop()
    finally:
        exio()
