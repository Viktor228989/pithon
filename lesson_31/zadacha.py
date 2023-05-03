from tkinter import *
root = Tk()
root.geometry("550x550")
# a = 0 # секундохран

# def salam():
#     global a
#     root.after(1000,salam)
#     c.delete("all")
#     a+=1
#     c.create_text(250,250,text=a, font="Arial 25")
#c = Canvas(root, width=500,height=500, bg="lime")
# c.pack(anchor=CENTER, expand=True)
# c.create_text(250,250,text=a, font="Arial 25")
# img = PhotoImage(file)
# salam() # первичный вызов функции

# 3 задача=================================================================================================
c = Canvas(root, width=200,height=200, bg="lime")
c.pack(anchor=CENTER, expand=True)
a = None
b = None


def lkm(event):
    global a
    a = (event.x, event.y)
def pkm(event):
    global b
    b = (event.x, event.y)

def makeline():
    if a and b:
        c.delete("all")
        c.create_line(a[0], a[-1],
                    b[0], b[-1])


anton = Button(root, text="Тыкни на меня", command=makeline)
anton.pack()

c.bind("<Button-1>", lkm)
c.bind("<Button-3>", pkm)

root.mainloop()