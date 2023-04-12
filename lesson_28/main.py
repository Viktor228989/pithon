import tkinter as tk
#
# def hell_o(event):
#     print("event=", event)
#     print("Очередой хело ворд")

root = tk.Tk()
# root.title("Мой первый ТкИНтеР") #заголовок
root.geometry("250x500") #разрешение окна
#
# photokarochka = tk.PhotoImage(file="img.png")
#
# lab1=tk.Label(root, text="Опа", image=photokarochka)
# lab1.pack()
#
# btn = tk.Button(root) # master - привязка к окну
# btn.bind("<Button-1>", hell_o) # левая кнопка мыши
# # btn.bind("<Double-Button-1>", hell_o) # ldjqyfz кнопка мыши
# # btn.bind("<Button-3>", hell_o) # правая кнопка мыши
# #btn.bind("<Return>", hell_o)
# # btn['comad'] = hell_o #действие при нажатии
# btn['text'] = 'Приффки'
# btn['font'] = ('times new roman', 20, "bold") # шрифт
# btn['height'] = 64 # высота
# btn['width'] = 2 # ширина
# btn["foreground"] = 'blue'
# btn['background'] = 'pink' # цвет фона
# btn.pack(anchor="e") # разместить элемент
# # anchor=e привязка на east (право)

def show_message():
    label['text'] = ent.get() # как очистить поле ввода
    ent.delete(0, 'end')



label = tk.Label(text="Приффки")
label.pack()
ent = tk.Entry(root)
ent.pack()
conifirm = tk.Button(text="Отправить", command=show_message)
conifirm.pack()

root.mainloop()