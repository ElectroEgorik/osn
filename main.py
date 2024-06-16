import tkinter as tk
from tkinter import messagebox, scrolledtext
import bd
import jjjj
import log

def show_table():
    output = bd.bd()
    if isinstance(output, str):
        text_area.insert(tk.END, output + '\n')
    else:
        text_area.insert(tk.END, str(output) + '\n')
def gr_ip():
    output = bd.bd(group_by='ip')
    if isinstance(output, str):
        text_area.insert(tk.END, output + '\n')
    else:
        text_area.insert(tk.END, str(output) + '\n')
def gr_date():
    output = bd.bd(group_by='date')
    if isinstance(output, str):
        text_area.insert(tk.END, output + '\n')
    else:
        text_area.insert(tk.END, str(output) + '\n')
def write_to_json():
    jjjj.js()
    messagebox.showinfo("Информация", "Содержимое таблицы записано в JSON файл.")
def read_and_write_logs():
    log.llog()
    messagebox.showinfo("Информация", "Логи прочитаны и записаны в базу данных.")

root = tk.Tk()
root.title("Управление логами и таблицами")
root.geometry("800x600")
text_area = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD)
text_area.pack(pady=10)
btn_show_table = tk.Button(root, text="Показать таблицу", command=show_table)
btn_show_table.pack(pady=10)
btn_show_table = tk.Button(root, text="Группировать по IP", command=gr_ip)
btn_show_table.pack(pady=10)
btn_show_table = tk.Button(root, text="Группировать по Дате", command=gr_date)
btn_show_table.pack(pady=10)
btn_write_to_json = tk.Button(root, text="Записать в JSON", command=write_to_json)
btn_write_to_json.pack(pady=10)
btn_read_and_write_logs = tk.Button(root, text="Прочитать и записать логи", command=read_and_write_logs)
btn_read_and_write_logs.pack(pady=10)
root.mainloop()