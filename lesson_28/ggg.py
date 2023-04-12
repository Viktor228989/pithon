import tkinter as tk
import urllib

root = tk.Tk()
root.geometry("700x700")

img = tk.PhotoImage(file="img.png").subsample(2,2)
label = tk.Label(image=img)
label.pack()

img2 = img.zoom(2, 1)
label2 = tk.Label(image=img2)
label2.pack()


img3 = img.subsample(2, 2)
label3 = tk.Label(image=img3)
label3.pack()

root.mainloop()

uimgUrl="https://winda10.com/rezhimy-windows-10/kartinka-v-kartinke-windows-10-kak-vklyuchit.html"
u=urllib.re
