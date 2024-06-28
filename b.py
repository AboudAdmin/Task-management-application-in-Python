import tkinter as tk
from tkinter import messagebox, scrolledtext, Toplevel

# دالة لإضافة مهمة
def add_task():
    task_title = entry_title.get()
    task_description = text_description.get("1.0", tk.END).strip()
    if task_title and task_description:
        listbox_tasks.insert(tk.END, task_title)
        tasks.append((task_title, task_description))
        entry_title.delete(0, tk.END)
        text_description.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a title and description.")

# دالة لحذف المهمة المحددة
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
        del tasks[task_index]
    except:
        messagebox.showwarning("Warning", "You must select a task.")

# دالة لحفظ المهام في ملف
def save_tasks():
    with open("tasks.txt", "w") as f:
        for title, description in tasks:
            f.write(f"{title}\n{description}\n---\n")

# دالة لتحميل المهام من الملف
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            lines = f.readlines()
            title, description = "", ""
            for line in lines:
                if line.strip() == "---":
                    listbox_tasks.insert(tk.END, title)
                    tasks.append((title, description))
                    title, description = "", ""
                elif not title:
                    title = line.strip()
                else:
                    description += line
    except FileNotFoundError:
        pass

# دالة لعرض وتعديل وصف المهمة عند النقر على العنوان
def edit_task(event):
    try:
        task_index = listbox_tasks.curselection()[0]
        title, description = tasks[task_index]

        edit_window = Toplevel(window)
        edit_window.title("Edit Task")
        edit_window.geometry("400x300")
        edit_window.configure(bg="#f0f0f0")

        # إدخال عنوان المهمة
        label_edit_title = tk.Label(edit_window, text="Task Title:", bg="#f0f0f0", font=("Arial", 14))
        label_edit_title.pack(pady=5)
        entry_edit_title = tk.Entry(edit_window, width=30, font=("Arial", 14))
        entry_edit_title.insert(0, title)
        entry_edit_title.pack(pady=5)

        # نص وصف المهمة
        label_edit_description = tk.Label(edit_window, text="Task Description:", bg="#f0f0f0", font=("Arial", 14))
        label_edit_description.pack(pady=5)
        text_edit_description = scrolledtext.ScrolledText(edit_window, width=40, height=10, font=("Arial", 12))
        text_edit_description.insert("1.0", description)
        text_edit_description.pack(pady=5)

        # دالة لحفظ التعديلات
        def save_edit():
            new_title = entry_edit_title.get()
            new_description = text_edit_description.get("1.0", tk.END).strip()
            tasks[task_index] = (new_title, new_description)
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, new_title)
            edit_window.destroy()

        # زر لحفظ التعديلات
        button_save_edit = tk.Button(edit_window, text="Save", command=save_edit, bg="#4CAF50", fg="white", font=("Arial", 14))
        button_save_edit.pack(pady=10)

    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

# إنشاء نافذة التطبيق
window = tk.Tk()
window.title("To-Do List")
window.geometry("500x600")
window.configure(bg="#e0f7fa")

# إنشاء إطار لإدخال المهمة
frame_task = tk.Frame(window, bg="#e0f7fa")
frame_task.pack(pady=10)

# إدخال عنوان المهمة
label_title = tk.Label(frame_task, text="Task Title:", bg="#e0f7fa", font=("Arial", 14))
label_title.pack(side=tk.LEFT, padx=5)
entry_title = tk.Entry(frame_task, width=30, font=("Arial", 14))
entry_title.pack(side=tk.LEFT, padx=5)

# نص وصف المهمة
label_description = tk.Label(window, text="Task Description:", bg="#e0f7fa", font=("Arial", 14))
label_description.pack()
text_description = scrolledtext.ScrolledText(window, width=50, height=10, font=("Arial", 12))
text_description.pack(pady=10)

# قائمة لعرض المهام
listbox_tasks = tk.Listbox(window, width=50, height=10, font=("Arial", 14))
listbox_tasks.pack(pady=10)
listbox_tasks.bind('<<ListboxSelect>>', edit_task)

# أزرار لإضافة، حذف، وحفظ المهام
button_add_task = tk.Button(window, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Arial", 14))
button_add_task.pack(side=tk.LEFT, padx=10, pady=10)

button_delete_task = tk.Button(window, text="Delete Task", command=delete_task, bg="#f44336", fg="white", font=("Arial", 14))
button_delete_task.pack(side=tk.LEFT, padx=10, pady=10)

button_save_tasks = tk.Button(window, text="Save Tasks", command=save_tasks, bg="#2196F3", fg="white", font=("Arial", 14))
button_save_tasks.pack(side=tk.RIGHT, padx=10, pady=10)

# توقيع المطور
label_developer = tk.Label(window, text="Developed by: عبدالله محمودي", bg="#e0f7fa", fg="#000", font=("Arial", 18, "bold"))
label_developer.pack(pady=20)

# قائمة المهام
tasks = []

# تحميل المهام عند بدء التطبيق
load_tasks()

# بدء الحلقة الرئيسية
window.mainloop()
