from tkinter import *
root = Tk()
root.geometry("550x550")

# bk(background) - фон
# fg(foreground) - цвет текста
# ====================Текст===================
c = Canvas(root, width=500, height=500, bg="white")
# c.create_text(10, 10,
#               text="Чупапи Муняня", anchor=NW,
#               font="Arial 25 italic", fill="pink")
# ===============================================


c.pack(anchor=CENTER, expand=True)


# =====================Прямоугольник==================================
# c.create_rectangle(10, 10,
#                    50, 100,
#                    outline="#2d1aa2",
#                    width=5)
# =======================================


# ====================Окружность===========================
# c.create_oval(10, 10, 50, 100,)
# ====================


# ====================Многоугольник========================
# c.create_polygon(10, 100,
#                  200, 200,
#                  10, 200)
# =================================


# ==================arc======================================
# c.create_oval(10,10,
#               100,100,
#               fill="pink")
# c.create_arc(10,10,
#              100,100,
#              fill="gold",
#              start=-90,
#              extent=-90,
#              width=8,
#              style=ARC)
# c.create_arc(10,10,
#              100,100,
#              fill="magenta",
#              start=45,
#              extent=135,
#              style=CHORD)

# c.create_arc(10,10,
#              100,100,
#              fill="silver",
#             start=30,extent=-180)
#==============================


#=============== line(arrow)============
# c.create_line(10,10,
#               250, 250,
#               arrow="last",
#               arrowshape=(50,550,50))
# ===================================
c.create_rectangle(10, 10,
                   50, 100,
                   outline="#2d1aa2",
                   dash="-..",
                   activewidth=20,
                   activefill="pink",
                   width=5)



root.mainloop()