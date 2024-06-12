from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

def Vaal():
    x1 = np.arange(0, 9, 0.5)
    y1 = (2 / 27) * x1 ** 2 - 3
    x2 = np.arange(-10, 0, 0.5)
    y2 = 0.04 * x2 ** 2 - 3
    x3 = np.arange(-9, -3, 0.5)
    y3 = (2 / 9) * (x3 + 6) ** 2 + 1
    x4 = np.arange(-3, 9, 0.5)
    y4 = (-1 / 12) * (x4 - 3) ** 2 + 6
    x5 = np.arange(5, 8.3, 0.5)
    y5 = (1 / 9) * (x5 - 5) ** 2 + 2
    x6 = np.arange(5, 8.5, 0.5)
    y6 = (1 / 8) * (x6 - 7) ** 2 + 1.5
    x7 = np.arange(-13, -9, 0.5)
    y7 = -0.75 * (x7 + 11) ** 2 + 6
    x8 = np.arange(-15, -13, 0.5)
    y8 = -0.5 * (x8 + 13) ** 2 + 3
    x9 = np.arange(-15, -10, 0.5)
    y9 = [1] * len(x9)
    x10 = np.arange(3, 4, 0.5)
    y10 = [3] * len(x10)
    plt.figure()
    plt.plot(x1, y1, "b-o", x2, y2, "r-o", x3, y3, "g-o", x4, y4, "c-o", x5, y5, "m-o", x6, y6, "y-o", x7, y7, "k-o", x8, y8, "b-o", x9, y9, "r-o", x10, y10, "g-o")
    plt.title("Vaal")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()

def Prillid():
    x1 = np.arange(-9, -0.5, 0.5)
    y1 = (-1 / 16) * (x1 + 5) ** 2 + 2
    x2 = np.arange(1, 9.5, 0.5)
    y2 = (-1 / 16) * (x2 - 5) ** 2 + 2
    x3 = np.arange(-9, -0.5, 0.5)
    y3 = (1 / 4) * (x3 + 5) ** 2 - 3
    x4 = np.arange(1, 9.5, 0.5)
    y4 = (1 / 4) * (x4 - 5) ** 2 - 3
    x5 = np.arange(-9, -6, 0.2)
    y5 = -(x5 + 7) ** 2 + 5
    x6 = np.arange(6, 9.5, 0.5)
    y6 = -(x6 - 7) ** 2 + 5
    x7 = np.arange(-1, 1.5, 0.5)
    y7 = -0.5 * x7 ** 2 + 1.5
    plt.figure()
    plt.plot(x1, y1, "b-o", x2, y2, "r-o", x3, y3, "g-o", x4, y4, "c-o", x5, y5, "m-o", x6, y6, "y-o", x7, y7, "k-o")
    plt.title("Prillid")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()

def Vihmavari():
    x1 = np.arange(-12, 12, 0.2)
    y1 = (-1 / 18) * x1 ** 2 + 12
    x2 = np.arange(-4, 4, 0.2)
    y2 = (-1 / 8) * x2 ** 2 + 6
    x3 = np.arange(-12, -4, 0.2)
    y3 = (-1 / 8) * (x3 + 8) ** 2 + 6
    x4 = np.arange(4, 12, 0.2)
    y4 = (-1 / 8) * (x4 - 8) ** 2 + 6
    x5 = np.arange(-4, -0.3, 0.5)
    y5 = 2 * (x5 + 3) ** 2 - 9
    x6 = np.arange(-3, 0.4, 0.4)
    y6 = 1.5 * (x6 + 3) ** 2 - 10
    plt.figure()
    plt.plot(x1, y1, "b-o", x2, y2, "r-o", x3, y3, "g-o", x4, y4, "c-o", x5, y5, "m-o", x6, y6, "y-o")
    plt.title("Vihmavari")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()

def Liblikas():
    x1 = np.arange(-9, -0.5, 0.5)
    y1 = (-1 / 8) * (x1 + 9) ** 2 + 8
    x2 = np.arange(1, 9, 0.5)
    y2 = (-1 / 8) * (x2 - 9) ** 2 + 8
    x3 = np.arange(-9, -7.5, 0.5)
    y3 = 7 * (x3 + 8) ** 2 + 1
    x4 = np.arange(8, 9.5, 0.5)
    y4 = 7 * (x4 - 8) ** 2 + 1
    x5 = np.arange(-8, -0.5, 0.5)
    y5 = (1 / 49) * (x5 + 1) ** 2
    x6 = np.arange(1, 8, 0.5)
    y6 = (1 / 49) * (x6 - 1) ** 2
    x7 = np.arange(-8, -0.5, 0.5)
    y7 = (-4 / 49) * (x7 + 1) ** 2
    x8 = np.arange(1, 8.5, 0.5)
    y8 = (-4 / 49) * (x8 - 1) ** 2
    x9 = np.arange(-8, -0.5, 0.5)
    y9 = (1 / 3) * (x9 + 5) ** 2 - 7
    x10 = np.arange(1, 8.5, 0.5)
    y10 = (1 / 3) * (x10 - 5) ** 2 - 7
    x11 = np.arange(0, 0, 0.5)
    y11 = -2 * (x11 + 1) ** 2 - 2
    x12 = np.arange(0, 0, 0.5)
    y12 = -2 * (x12 - 1) ** 2 - 2
    x13 = np.arange(-1, 1, 0.5)
    y13 = -4 * x13 ** 2 + 2
    x14 = np.arange(-1, 1, 0.5)
    y14 = 4 * x14 ** 2 - 6
    x15 = np.arange(-1.5, 0.5, 0.5)
    y15 = -1.5 * x15 + 2
    x16 = np.arange(0, 2, 0.5)
    y16 = 1.5 * x16 + 2
    plt.figure()
    plt.plot(x1, y1, "b-o", x2, y2, "r-o", x3, y3, "g-o", x4, y4, "c-o", x5, y5, "m-o", x6, y6, "y-o", x7, y7, "k-o", x8, y8, "b-o", x9, y9, "r-o", x10, y10, "g-o", x11, y11, "c-o", x12, y12, "m-o", x13, y13, "y-o", x14, y14, "k-o", x15, y15, "b-o", x16, y16, "r-o")
    plt.title("Liblikas")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()

def Kilpkonn():
    x1 = np.arange(-9, 9.5, 0.5)
    y1 = (-1 / 18) * x1 ** 2 + 12
    x2 = np.arange(-9, -0.5, 0.5)
    y2 = (2 / 9) * (x2 + 5) ** 2 + 2
    x3 = np.arange(0.5, 9.5, 0.5)
    y3 = (2 / 9) * (x3 - 5) ** 2 + 2
    x4 = np.arange(-9, -5.5, 0.5)
    y4 = -(2 / 9) * (x4 + 7) ** 2 + 5
    x5 = np.arange(5.5, 9.5, 0.5)
    y5 = -(2 / 9) * (x5 - 7) ** 2 + 5
    x6 = np.arange(-5, -2.5, 0.5)
    y6 = -(4 / 9) * (x6 + 3.5) ** 2 + 10
    x7 = np.arange(2.5, 5.5, 0.5)
    y7 = -(4 / 9) * (x7 - 3.5) ** 2 + 10
    x8 = np.arange(-5, 5.5, 0.5)
    y8 = (4 / 81) * x8 ** 2 - 9
    plt.figure()
    plt.plot(x1, y1, "b-o", x2, y2, "r-o", x3, y3, "g-o", x4, y4, "c-o", x5, y5, "m-o", x6, y6, "y-o", x7, y7, "k-o", x8, y8, "b-o")
    plt.title("Kilpkonn")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()

aken = Tk()
aken.title('Graafikud')
aken.geometry('400x400')
aken.configure(bg='#add8e6')

lbl = Label(aken, text="Vali graafik", font="Calibri 26", bg='#add8e6', fg='black')
lbl.pack()

btn1 = Button(aken, text="Vaal", font="Calibri 26", width=15, command=Vaal)
btn1.pack(pady=5)
btn2 = Button(aken, text="Vihmavari", font="Calibri 26", width=15, command=Vihmavari)
btn2.pack(pady=5)
btn3 = Button(aken, text="Liblikas", font="Calibri 26", width=15, command=Liblikas)
btn3.pack(pady=5)
btn4 = Button(aken, text="Prillid", font="Calibri 26", width=15, command=Prillid)
btn4.pack(pady=5)
btn5 = Button(aken, text="Kilpkonn", font="Calibri 26", width=15, command=Kilpkonn)
btn5.pack(pady=5)

aken.mainloop()
