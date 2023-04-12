import tkinter as tk
root=tk.Tk()
root.geometry=("300x300")

label = tk.Label(root, text="Ваш адрес")
label.pack()

entry = tk.Entry(root)
entry.pack()

label1 = tk.Label(root, text="Комментарий")
label1.pack()

text = tk.Text(root)
text.pack()

conifirm = tk.Button(root,text="Отправить")
conifirm.pack()





root.mainloop()