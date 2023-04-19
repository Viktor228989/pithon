# from tkinter import *
#
# def rf():
#     if cb_val.get() == True:
#         btn['state'] = "disabled"
#
#
# root = Tk()
#
#
# cb_val = BooleanVar()
# cb = Checkbutton(root, text="Активировать",
#                  variable=cb_val,
#                  onvalue=True,
#                  offvalue=False)
# cb.pack()
# btn = Button(root, text="Активировано", command=rf)
# btn.pack()
#
#
#
# root.mainloop()
#
# from tkinter import *
#
# def bold():
#     if val_bold.get():
#         lab['font'] +='bold'
# #     else:
# #         lab['font'] = lab['font'].replace("bold",)
# #
# # def italik():
# #     pass
# #
# # root=Tk()
# # lab = Label(root, text="Я текст", font="Arial 15")
# # lab.pack()
#
# val_bold = BooleanVar()
# cb_bold=Checkbutton(root,
#                     text="ирный",
#                     command=bold,
#                     variable=val_bold,
#                     onvalue = True,
#                     offvalue = False)
# cb_bold.pack()
#
# val_italik=BooleanVar
# cb_italik=Checkbutton(root,
#                       text="ирный",
#                       command=italik,
# #                       onvalue=True,
# #                       offvalue=False)
# # cb_italik.pack()
# #
# # root.mainloop()
#
from tkinter import *
root = Tk()
root.g4('400x400')
root = Tk()
root.geometry('400x400')

# mas = ['red','green',"blue",'purple','pink','gold']
# def fg(e):
#     root.config(background=mas[val.get()])


# val = IntVar()
# ck = Scale(root,from_=0,
#            to=5,
#            variable=val,
#            command=fg,
#            orient=HORIZONTAL)
# ck.pack()

ima = PhotoImage(file="уважение.png").subsample(3,3)
lab = Label(root,image=ima)
lab.pack()


root.mainloop()

