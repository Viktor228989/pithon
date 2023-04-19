from tkinter import *
#
# def printer(pupu):
#     print(cb_val.get())
#     cb.deselect()
#     cb.select()
#
root = Tk()
root.geometry("299x200")
#
#
#
# cb_val = BooleanVar() # переменная хранящая значения
#
# cb = Checkbutton(root,
#                  text="Подписка",
#                  variable=cb_val,
#                  onvalue=True,
#                  offvalue=False)
# cb.pack()
# cb.bind("<Button-3>", printer)
# def get_rb():
#     print(rb_val.get())
#
# rb_val = IntVar()
# print(rb_val.get())
# rb = Radiobutton(root,variable=rb_val,text="ОДИН", value=505, command=get_rb).pack()
# jb = Radiobutton(root,variable=rb_val,text="ДВА", value=47, command=get_rb).pack()

# def pupu():
#     print(lst.curselection()) # CURrent Selection - текущий выбр
#
# v = ["Тортик", "Кифасик", "Пирожки"]
#
# lst = Listbox(root, selectmode=EXTENDED)
# lst.pack()
# for elem in v:
#     lst.insert("end", elem) # размещние элемента в ListBox
#
# Button(root, text="Активироватьб", command=pupu).pack()
#
# def get_scale(e):
#     print(scal.get())
# scal = Scale(root,from_=4, to=16,
#              orient=HORIZONTAL,
#              length=200, # длина полосы
#              width=50, # ширина полосы
#              tickinterval=2, # подписать с шагом
#              command=get_scale)
# scal.pack()
# def activate():
#     if btn1['state'] == "disabled":
#         btn1["state"] = "normal"
#     else:
#         btn1['state'] = "disabled"
#
# btn1= Button(root,text="Я кнопка")
# btn1.pack()
# btn2=Button(root, text="Активировать Windows2023", command=activate)
# btn2.pack()
root.mainloop()