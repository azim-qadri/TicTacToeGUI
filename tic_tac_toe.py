from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image


root = Tk()
root.title('Tic Tac Toe')
root.configure(padx=30, pady=50)

cross = ImageTk.PhotoImage(Image.open(r'C:\Users\User\PycharmProjects\TicTacToe\cross.png').resize((60, 60)))
zero = ImageTk.PhotoImage(Image.open(r'C:\Users\User\PycharmProjects\TicTacToe\zero.png').resize((60, 60)))
count = 0
s = ''
z = ''


def draw():
    global count
    if count >= 8:
        Label(root, text='Draw').grid(row=5, column=0, columnspan=3)
        disable()
    else:
        pass


def disable():
    b1['state'] = 'disabled'
    b2['state'] = 'disabled'
    b3['state'] = 'disabled'
    b4['state'] = 'disabled'
    b5['state'] = 'disabled'
    b6['state'] = 'disabled'
    b7['state'] = 'disabled'
    b8['state'] = 'disabled'
    b9['state'] = 'disabled'


def cross_count(x):
    global s
    global count
    s += str(x)
    if '1' in s:
        if '2' in s:
            if '3' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '1' in s:
        if '3' in s:
            if '2' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '2' in s:
        if '1' in s:
            if '3' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '2' in s:
        if '3' in s:
            if '1' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '3' in s:
        if '1' in s:
            if '2' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '3' in s:
        if '2' in s:
            if '1' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '1' in s:
        if '4' in s:
            if '7' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '1' in s:
        if '7' in s:
            if '4' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '4' in s:
        if '1' in s:
            if '7' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '4' in s:
        if '7' in s:
            if '1' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '7' in s:
        if '1' in s:
            if '4' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '7' in s:
        if '4' in s:
            if '1' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '7' in s:
        if '8' in s:
            if '9' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '7' in s:
        if '9' in s:
            if '8' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '8' in s:
        if '7' in s:
            if '9' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '8' in s:
        if '9' in s:
            if '7' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '9' in s:
        if '7' in s:
            if '8' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '9' in s:
        if '8' in s:
            if '7' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '3' in s:
        if '6' in s:
            if '9' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '3' in s:
        if '9' in s:
            if '6' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '6' in s:
        if '3' in s:
            if '9' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '6' in s:
        if '9' in s:
            if '3' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '9' in s:
        if '3' in s:
            if '6' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '9' in s:
        if '6' in s:
            if '3' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '1' in s:
        if '5' in s:
            if '9' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '1' in s:
        if '9' in s:
            if '5' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in s:
        if '1' in s:
            if '9' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in s:
        if '9' in s:
            if '1' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '9' in s:
        if '1' in s:
            if '5' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '9' in s:
        if '5' in s:
            if '1' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '3' in s:
        if '5' in s:
            if '7' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '3' in s:
        if '7' in s:
            if '5' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in s:
        if '3' in s:
            if '7' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in s:
        if '7' in s:
            if '3' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '7' in s:
        if '3' in s:
            if '5' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '7' in s:
        if '5' in s:
            if '3' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '2' in s:
        if '5' in s:
            if '8' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '2' in s:
        if '8' in s:
            if '5' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in s:
        if '2' in s:
            if '8' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in s:
        if '8' in s:
            if '2' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '8' in s:
        if '5' in s:
            if '2' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '8' in s:
        if '2' in s:
            if '5' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '4' in s:
        if '5' in s:
            if '6' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '4' in s:
        if '6' in s:
            if '5' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in s:
        if '4' in s:
            if '6' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in s:
        if '6' in s:
            if '4' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '6' in s:
        if '5' in s:
            if '4' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '6' in s:
        if '4' in s:
            if '5' in s:
                Label(root, text='Player 1 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1


def zero_count(x):
    global z
    global count
    print(z)
    z += str(x)
    if '1' in z:
        if '2' in z:
            if '3' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '1' in z:
        if '3' in z:
            if '2' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '2' in z:
        if '1' in z:
            if '3' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '2' in z:
        if '3' in z:
            if '1' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '3' in z:
        if '1' in z:
            if '2' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '3' in z:
        if '2' in z:
            if '1' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '1' in z:
        if '4' in z:
            if '7' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '1' in z:
        if '7' in z:
            if '4' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '4' in z:
        if '1' in z:
            if '7' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '4' in z:
        if '7' in z:
            if '1' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '7' in z:
        if '1' in z:
            if '4' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '7' in z:
        if '4' in z:
            if '1' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '7' in z:
        if '8' in z:
            if '9' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '7' in z:
        if '9' in z:
            if '8' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '8' in z:
        if '7' in z:
            if '9' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '8' in z:
        if '9' in z:
            if '7' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '9' in z:
        if '7' in z:
            if '8' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '9' in z:
        if '8' in z:
            if '7' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '3' in z:
        if '6' in z:
            if '9' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '3' in z:
        if '9' in z:
            if '6' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '6' in z:
        if '3' in z:
            if '9' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '6' in z:
        if '9' in z:
            if '3' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '9' in z:
        if '3' in z:
            if '6' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '9' in z:
        if '6' in z:
            if '3' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '1' in z:
        if '5' in z:
            if '9' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '1' in z:
        if '9' in z:
            if '5' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in z:
        if '1' in z:
            if '9' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in z:
        if '9' in z:
            if '1' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '9' in z:
        if '1' in z:
            if '5' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '9' in z:
        if '5' in z:
            if '1' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '3' in z:
        if '5' in z:
            if '7' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '3' in z:
        if '7' in z:
            if '5' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in z:
        if '3' in z:
            if '7' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in z:
        if '7' in z:
            if '3' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '7' in z:
        if '3' in z:
            if '5' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '7' in z:
        if '5' in z:
            if '3' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '2' in z:
        if '5' in z:
            if '8' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '2' in z:
        if '8' in z:
            if '5' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in z:
        if '2' in z:
            if '8' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in z:
        if '8' in z:
            if '2' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '8' in z:
        if '5' in z:
            if '2' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '8' in z:
        if '2' in z:
            if '5' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '4' in z:
        if '5' in z:
            if '6' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '4' in z:
        if '6' in z:
            if '5' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in z:
        if '4' in z:
            if '6' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '5' in z:
        if '6' in z:
            if '4' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '6' in z:
        if '5' in z:
            if '4' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1
    if '6' in z:
        if '4' in z:
            if '5' in z:
                Label(root, text='Player 2 won').grid(row=5, column=0, columnspan=3)
                disable()
                count -= 1


def but(x):
    global count
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9
    global s
    global z
    if count % 2 == 0:
        if x == 1:
            b1.destroy()
            b1 = Button(root, image=cross, state='active')
            b1.grid(row=0, column=0, ipadx=40, ipady=20, padx=10, pady=5)
            print(b1['state'])
            cross_count(x)
            draw()
        if x == 2:
            b2.destroy()
            b2 = Button(root, image=cross, state='active')
            b2.grid(row=0, column=1, ipadx=40, ipady=20, padx=10, pady=5)
            cross_count(x)
            draw()
        if x == 3:
            b3.destroy()
            b3 = Button(root, image=cross, state='active')
            b3.grid(row=0, column=2, ipadx=40, ipady=20, padx=10, pady=5)
            cross_count(x)
            draw()

        if x == 4:
            b4.destroy()
            b4 = Button(root, image=cross, state='active')
            b4.grid(row=1, column=0, ipadx=40, ipady=20, padx=10, pady=5)
            cross_count(x)
            draw()
        if x == 5:
            b5.destroy()
            b5 = Button(root, image=cross, state='active')
            b5.grid(row=1, column=1, ipadx=40, ipady=20, padx=10, pady=5)
            cross_count(x)
            draw()
        if x == 6:
            b6.destroy()
            b6 = Button(root, image=cross, state='active')
            b6.grid(row=1, column=2, ipadx=40, ipady=20, padx=10, pady=5)
            cross_count(x)
            draw()
        if x == 7:
            b7.destroy()
            b7 = Button(root, image=cross, state='active')
            b7.grid(row=2, column=0, ipadx=40, ipady=20, padx=10, pady=5)
            cross_count(x)
            draw()
        if x == 8:
            b8.destroy()
            b8 = Button(root, image=cross, state='active')
            b8.grid(row=2, column=1, ipadx=40, ipady=20, padx=10, pady=5)
            cross_count(x)
            draw()
        if x == 9:
            b9.destroy()
            b9 = Button(root, image=cross, state='active')
            b9.grid(row=2, column=2, ipadx=40, ipady=20, padx=10, pady=5)
            cross_count(x)
            draw()

    else:
        if x == 1:
            b1.destroy()
            b1 = Button(root, image=zero, state='active')
            b1.grid(row=0, column=0, ipadx=40, ipady=20, padx=10, pady=5)
            zero_count(x)
            draw()
        if x == 2:
            b2.destroy()
            b2 = Button(root, image=zero, state='active')
            b2.grid(row=0, column=1, ipadx=40, ipady=20, padx=10, pady=5)
            zero_count(x)
            draw()
        if x == 3:
            b3.destroy()
            b3 = Button(root, image=zero, state='active')
            b3.grid(row=0, column=2, ipadx=40, ipady=20, padx=10, pady=5)
            zero_count(x)
            draw()
        if x == 4:
            b4.destroy()
            b4 = Button(root, image=zero, state='active')
            b4.grid(row=1, column=0, ipadx=40, ipady=20, padx=10, pady=5)
            zero_count(x)
            draw()
        if x == 5:
            b5.destroy()
            b5 = Button(root, image=zero, state='active')
            b5.grid(row=1, column=1, ipadx=40, ipady=20, padx=10, pady=5)
            zero_count(x)
            draw()
        if x == 6:
            b6.destroy()
            b6 = Button(root, image=zero, state='active')
            b6.grid(row=1, column=2, ipadx=40, ipady=20, padx=10, pady=5)
            zero_count(x)
            draw()
        if x == 7:
            b7.destroy()
            b7 = Button(root, image=zero, state='active')
            b7.grid(row=2, column=0, ipadx=40, ipady=20, padx=10, pady=5)
            zero_count(x)
            draw()
        if x == 8:
            b8.destroy()
            b8 = Button(root, image=zero, state='active')
            b8.grid(row=2, column=1, ipadx=40, ipady=20, padx=10, pady=5)
            zero_count(x)
            draw()
        if x == 9:
            b9.destroy()
            b9 = Button(root, image=zero, state='active')
            b9.grid(row=2, column=2, ipadx=40, ipady=20, padx=10, pady=5)
            zero_count(x)
            draw()

    count += 1


b1 = Button(root, command=lambda: but(1))
b1.grid(row=0, column=0, ipadx=40, ipady=40, padx=10, pady=5)
b2 = Button(root, command=lambda: but(2))
b2.grid(row=0, column=1, ipadx=40, ipady=40, padx=10, pady=5)
b3 = Button(root, command=lambda: but(3))
b3.grid(row=0, column=2, ipadx=40, ipady=40, padx=10, pady=5)
b4 = Button(root, command=lambda: but(4))
b4.grid(row=1, column=0, ipadx=40, ipady=40, padx=10, pady=5)
b5 = Button(root, command=lambda: but(5))
b5.grid(row=1, column=1, ipadx=40, ipady=40, padx=10, pady=5)
b6 = Button(root, command=lambda: but(6))
b6.grid(row=1, column=2, ipadx=40, ipady=40, padx=10, pady=5)
b7 = Button(root, command=lambda: but(7))
b7.grid(row=2, column=0, ipadx=40, ipady=40, padx=10, pady=5)
b8 = Button(root, command=lambda: but(8))
b8.grid(row=2, column=1, ipadx=40, ipady=40, padx=10, pady=5)
b9 = Button(root, command=lambda: but(9))
b9.grid(row=2, column=2, ipadx=40, ipady=40, padx=10, pady=5)
bb = Button(root, state='active')
root.mainloop()
