# -*- encoding: utf-8 -*-
"""
@File    : AppV2.py
@Time    : 2021/11/10 14:44
@Author  : Jingmo
@Software: PyCharm
"""

import os
import tkinter
from threading import Thread
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename


# 服务管理
def exio():
    os.popen('adb kill-server')
    os.popen(f'taskkill /f /im adb.exe')
    os.popen(f'taskkill /f /im cmd.exe')


# 表格内容清空
def delButton(tree):
    x = tree.get_children()
    for item in x:
        tree.delete(item)


# 下拉列表框打印列表功能
def chaxun_biaoge_star(get_xaunze_):
    def disanfang():
        delButton(tree)
        app_all_list = os.popen('adb shell pm list packages -3').read()
        apps_list = app_all_list.split('package:')
        app_list = [x.strip() for x in apps_list if x.strip() != '']
        ind = 0
        for i_app_pkg in app_list:
            appname = os.popen(f'adb shell pm path {i_app_pkg}').read().split('/')[-1]
            ind += 1
            tree.insert("", ind, text=f"{ind}", values=(appname, i_app_pkg))  # #给第0行添加数据，索引值可重复

    def xitongyinyong():
        delButton(tree)
        app_all_list = os.popen('adb shell pm list packages -s').read()
        apps_list = app_all_list.split('package:')
        app_list = [x.strip() for x in apps_list if x.strip() != '']
        ind = 0
        for i_app_pkg in app_list:
            appname = os.popen(f'adb shell pm path {i_app_pkg}').read().split('/')[-1]
            ind += 1
            tree.insert("", ind, text=f"{ind}", values=(appname, i_app_pkg))  # #给第0行添加数据，索引值可重复

    def qiyong():
        delButton(tree)
        app_all_list = os.popen('adb shell pm list packages -e').read()
        apps_list = app_all_list.split('package:')
        app_list = [x.strip() for x in apps_list if x.strip() != '']
        ind = 0
        for i_app_pkg in app_list:
            appname = os.popen(f'adb shell pm path {i_app_pkg}').read().split('/')[-1]
            ind += 1
            tree.insert("", ind, text=f"{ind}", values=(appname, i_app_pkg))  # #给第0行添加数据，索引值可重复

    def tinyong():
        delButton(tree)
        app_all_list = os.popen('adb shell pm list packages -d').read()
        apps_list = app_all_list.split('package:')
        app_list = [x.strip() for x in apps_list if x.strip() != '']
        ind = 0
        for i_app_pkg in app_list:
            appname = os.popen(f'adb shell pm path {i_app_pkg}').read().split('/')[-1]
            ind += 1
            tree.insert("", ind, text=f"{ind}", values=(appname, i_app_pkg))  # #给第0行添加数据，索引值可重复

    def suoyouyinyong():
        delButton(tree)
        app_all_list = os.popen('adb shell pm list packages').read()
        apps_list = app_all_list.split('package:')
        app_list = [x.strip() for x in apps_list if x.strip() != '']
        ind = 0
        for i_app_pkg in app_list:
            appname = os.popen(f'adb shell pm path {i_app_pkg}').read().split('/')[-1]
            ind += 1
            tree.insert("", ind, text=f"{ind}", values=(appname, i_app_pkg))  # #给第0行添加数据，索引值可重复

    # ('第三方应用', '系统应用', '已启用的应用', '已停用的应用', '所有应用包名')
    if get_xaunze_ == "第三方应用":
        Thread(target=disanfang).start()

    if get_xaunze_ == "系统应用":
        Thread(target=xitongyinyong).start()

    if get_xaunze_ == "已启用的应用":
        Thread(target=qiyong).start()

    if get_xaunze_ == "已停用的应用":
        Thread(target=tinyong).start()

    if get_xaunze_ == "所有应用包名":
        Thread(target=suoyouyinyong).start()


# 依据列表内容执行下拉列表功能
def zhixing_star():
    def zhixing_(app_pkg):
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

    if str(len(tree.selection())) != "0":
        for items in tree.selection():
            item_text = tree.item(items, "values")[1]
            print("已选择：" + item_text)  # 输出所选行的第一列的值
            th_app = messagebox.askokcancel('提示', f"确认对 {item_text} 执行操作？")
            if th_app == True:
                Thread(target=zhixing_, args=(item_text,)).start()
    else:
        messagebox.showinfo('提示', "没有对任何应用进行操作！")


# 查询函数
def chaxun_star():
    delButton(tree)
    get_xaunze_ = xaunze_.get()
    Thread(target=chaxun_biaoge_star, args=(get_xaunze_,)).start()


# 搜索函数
def sousuo_star():
    def in_suosuo_(get_ent):
        delButton(tree)
        chaxun_app_list = os.popen(f'adb shell pm list packages | findstr "{get_ent}"').read()
        c_apps_list = chaxun_app_list.split('package:')
        app_list = [x.strip() for x in c_apps_list if x.strip() != '']
        ind = 0
        for i_app_pkg in app_list:
            appname = os.popen(f'adb shell pm path {i_app_pkg}').read().split('/')[-1]
            ind += 1
            tree.insert("", ind, text=f"{ind}", values=(appname, i_app_pkg))  # #给第0行添加数据，索引值可重复

    get_ent = str(app_ss_pkg.get())
    this_a = messagebox.askokcancel('提示', f"{get_ent} 是正确包名关键字吗？\n\n如果不是请重新输入！")
    if this_a == True:
        Thread(target=in_suosuo_, args=(get_ent,)).start()


# 开始弹窗
def stare_app():
    def start_():
        xuliehao = os.popen('adb devices').read()
        phone = os.popen('adb shell getprop ro.product.model').read()
        lianjie = messagebox.askokcancel('使用说明',
                                         phone + xuliehao +
                                         "显示【手机型号】和【序列号】点击确认即可\n"
                                         "否则请开启手机【USb调试】相关功能, 正确链接手机\n软件由Python制作，运行效率较慢，善待！\n"
                                         "点击取消 退出程序")
        if lianjie == False:
            root.destroy()
            exit()
    Thread(target=start_, ).start()


# 降级安装
def jiangjianzuhang_star():
    def jiangjianzhuang_():
        apk = askopenfilename(title='选择需要安装的文件 [ apk ]', initialdir='/', filetypes=[('Android File', '*.apk')])
        apkinfo = os.popen(f'adb install -r -d {apk}').read()
        messagebox.askokcancel('显示 success 则表示安装完成', f'{apkinfo}')

    jiangji = messagebox.askokcancel('降级安装提示', "降级操作，还请做好备份，\n"
                                               "部分应用降级可能出现闪退，不建议跨大版本降级\n取消关闭应用降级操作")
    if jiangji == True:
        Thread(target=jiangjianzhuang_).start()


# 应用相关信息
def app_info_star():
    def app_info(app_):
        this_app_versionCode = os.popen(f'adb shell pm dump {app_} | findstr "versionCode"').read().split("=")[-1].replace('\n', '').replace('\r', '')
        this_app_primaryCpuAbi = os.popen(f'adb shell pm dump {app_} | findstr "primaryCpuAbi"').read().split("=")[-1].replace('\n', '').replace('\r', '')
        this_app_versionName = os.popen(f'adb shell pm dump {app_} | findstr "versionName"').read().split("=")[-1].replace('\n', '').replace('\r', '')
        this_app_firstInstallTime = os.popen(f'adb shell pm dump {app_} | findstr "firstInstallTime"').read().split("=")[-1].replace('\n', '').replace('\r', '')
        this_app_lastUpdateTime = os.popen(f'adb shell pm dump {app_} | findstr "lastUpdateTime"').read().split("=")[-1].replace('\n', '').replace('\r', '')

        messagebox.showinfo("App信息", f"{app_}\n目标Sdk：{this_app_versionCode}"
                                     f"\n版本号：{this_app_versionName}"
                                     f"\n支持的CPU架构：{this_app_primaryCpuAbi}"
                                     f"\n首次安装时间：{this_app_firstInstallTime}"
                                     f"\n最后更新时间：{this_app_lastUpdateTime}"
                            )

    if str(len(tree.selection())) != "0":
        for app_item in tree.selection():
            app_text = tree.item(app_item, "values")[1]
            Thread(target=app_info, args=(app_text,)).start()
    else:
        messagebox.showinfo('提示', "没有对任何应用进行操作！")


if __name__ == '__main__':
    os.popen('mode con cols=50 lines=10')
    try:
        root = tkinter.Tk()
        root.title("ADB手机应用管理工具")  # #窗口标题
        root.geometry("700x400+700+360")  # #窗口位置500后面是字母x
        root.resizable(False, False)

        # 表格
        tree = ttk.Treeview(root, height=10, show="headings")  # #创建表格对象
        tree["columns"] = ("安装包（参考）", "包名")  # #定义列
        tree.column("安装包（参考）", width=300)
        tree.column("包名", width=400)

        tree.heading("安装包（参考）", text="安装包（应用名仅供参考无法准确获取）")
        tree.heading("包名", text="应用包名【讲道理-无误】")

        VScroll1 = ttk.Scrollbar(tree, orient='vertical', command=tree.yview)
        VScroll1.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
        # 给treeview添加配置
        tree.configure(yscrollcommand=VScroll1.set)
        tree.place(x=0, y=60)

        # 创建下拉菜单
        xaunze_ = ttk.Combobox(root, font=('宋体', 16, "bold"), width=14, state="readonly")
        # 设置下拉菜单中的值
        xaunze_['value'] = ('第三方应用', '系统应用', '已启用的应用', '已停用的应用', '所有应用包名')
        # 设置默认值，即默认下拉框中的内容
        xaunze_.current(3)
        xaunze_.place(x=14, y=14)

        app_info_ = tkinter.Button(root, text="获取App信息", font=('宋体', 12, "bold"), width=12, command=app_info_star)
        app_info_.config(fg="green", bg="white")
        app_info_.place(x=370, y=12)

        app_info_leb = tkinter.Label(root, text="请先查询/查找应用\n←再选择应用获取App信息\n过程较慢，耐心等待", font=('宋体', 12))
        app_info_leb.place(x=500, y=3)

        chaxunde = tkinter.Button(root, text="查询", font=('宋体', 12, "bold"), width=9, command=chaxun_star)
        chaxunde.config(fg="green", bg="white")
        chaxunde.place(x=210, y=12)

        zhixing_pkg = tkinter.Label(root, text="↑请先查询/查找应用\n再选择列表应用执行↓", font=('宋体', 12))
        zhixing_pkg.place(x=10, y=298)

        # 创建下拉菜单
        cmb = ttk.Combobox(root, font=('宋体', 16, "bold"), width=6, state="readonly")
        # 设置下拉菜单中的值
        cmb['value'] = ('卸载', '停用', '启用')
        # 设置默认值，即默认下拉框中的内容
        cmb.current(1)
        cmb.place(x=30, y=346)

        zhixing = tkinter.Button(root, text="← 执行", font=('宋体', 12, "bold"), width=9, command=zhixing_star)
        zhixing.config(fg="red", bg="white")
        zhixing.place(x=142, y=345)

        app_ss_pkg = tkinter.Label(root, text="包名\n不要反人类输入\n支持模糊查询→", font=('宋体', 12))
        app_ss_pkg.place(x=218, y=288)

        app_ss_pkg = tkinter.Entry(root, font=('微软雅黑', 14, "bold"), justify='center', width=24)
        app_ss_pkg.place(x=340, y=298)

        sousuo = tkinter.Button(root, text="↑ 关键字查找", font=('宋体', 12, "bold"), width=14, command=sousuo_star)
        sousuo.config(fg="red", bg="white")
        sousuo.place(x=340, y=345)

        jiangji = tkinter.Button(root, text="降级安装（保留数据）", font=('宋体', 12, "bold"), command=jiangjianzuhang_star)
        jiangji.config(fg="green", bg="white")
        jiangji.place(x=500, y=345)

        stare_app()
        root.mainloop()
    finally:
        exio()
        # pass
