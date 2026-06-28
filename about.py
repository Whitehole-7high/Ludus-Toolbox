#Copyright (c) 2026 Whitehole
#Released under the MIT License.
#===========================================
#文件名 about.py
# 创建时间 2026-06-28
# 项目 Ludus Toolbox
#===========================================
import tkinter as tk
from tkinter import ttk, messagebox


# 创建关于窗口主界面
root = tk.Tk()
root.title("关于 Ludus工具箱")
root.geometry("500x300")
root.resizable(False, False)

# 顶部标题
title_label = ttk.Label(root, text="Ludus工具箱", font=("微软雅黑", 16, "bold"))
title_label.pack(pady=15)

# 分割线
sep = ttk.Separator(root, orient=tk.HORIZONTAL)
sep.pack(fill=tk.X, padx=30)

# 主体信息容器框
main_frame = ttk.Frame(root)
main_frame.pack(pady=20)

# 版权行
lab_copyright = ttk.Label(main_frame, text="Copyright (c) 2026 Whitehole", font=("微软雅黑", 10))
lab_copyright.pack()

# 协议行
lab_license = ttk.Label(main_frame, text="开源协议：MIT License", font=("微软雅黑", 10))
lab_license.pack(pady=6)
lab_license = ttk.Label(main_frame, text="开源地址：https://github.com/Whitehole-7high/Ludus-Toolbox", font=("微软雅黑", 10))
lab_license.pack(pady=6)
# 开源声明
lab_note = ttk.Label(main_frame, text="部分第三方闭源配套工具，源码仓库不予展示", font=("微软雅黑", 10))
lab_note.pack(pady=6)

# 底部关闭按钮
btn_close = ttk.Button(root, text="关闭", command=root.destroy)
btn_close.pack(pady=10)

root.mainloop()