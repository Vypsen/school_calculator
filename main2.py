from tkinter import *


body = Tk()
body.title('matematichka')
body.geometry('300x400')
body['bg'] = 'white'
NUM_1 = 0
def addDigit_7():
    global NUM_1
    NUM_1 = NUM_1*10+7
    result.configure(text=NUM_1)

def addDigit_8():
    global NUM_1
    NUM_1 = NUM_1*10+8
    result.configure(text=NUM_1)
def addDigit_9():
    global NUM_1
    NUM_1 = NUM_1*10+9
    result.configure(text=NUM_1)
def addDigit_4():
    global NUM_1
    NUM_1 = NUM_1*10+4
    result.configure(text=NUM_1)
def addDigit_5():
    global NUM_1
    NUM_1 = NUM_1*10+5
    result.configure(text=NUM_1)
def addDigit_6():
    global NUM_1
    NUM_1 = NUM_1*10+6
    result.configure(text=NUM_1)
def addDigit_1():
    global NUM_1
    NUM_1 = NUM_1*10+1
    result.configure(text=NUM_1)
def addDigit_2():
    global NUM_1
    NUM_1 = NUM_1*10+2
    result.configure(text=NUM_1)
def addDigit_3():
    global NUM_1
    NUM_1 = NUM_1*10+3
    result.configure(text=NUM_1)

result = Label(body, text='0', bg='white', font=('WhitehallCyr', 30))
b_plus = Button(body, text='+', bg='white', width=8, height=5, fg='black', font=(40))
b_min = Button(body, text='-', bg='white', width=8, height=5, fg='black', font=(40))
b_umno = Button(body, text='*', bg='white', width=8, height=5, fg='black', font=(40))
b_del = Button(body, text='/', bg='white', width=8, height=5, fg='black', font=(40))
b_sev = Button(body, text='7', bg='white', width=8, height=5, fg='black', command=addDigit_7)
b_eight = Button(body, text='8', bg='white', width=8, height=5, fg='black', command=addDigit_8)
b_nin = Button(body, text='9', bg='white', width=8, height=5, fg='black', command=addDigit_9)
b_four = Button(body, text='4', bg='white', width=8, height=5, fg='black', command=addDigit_4)
b_five = Button(body, text='5', bg='white', width=8, height=5, fg='black', command=addDigit_5)
b_six = Button(body, text='6', bg='white', width=8, height=5, fg='black', command=addDigit_6)
b_one = Button(body, text='1', bg='white', width=8, height=5, fg='black', command=addDigit_1)
b_two = Button(body, text='2', bg='white', width=8, height=5, fg='black', command=addDigit_2)
b_three = Button(body, text='3', bg='white', width=8, height=5, fg='black', command=addDigit_3)



result.grid(row=0, column=0, columnspan=4)
b_plus.grid(row=1, column=0)
b_min.grid(row=1, column=1)
b_umno.grid(row=1, column=2)
b_del.grid(row=1, column=3)
b_sev.grid(row=8, column=1)
b_eight.grid(row=8, column=2)
b_nin.grid(row=8, column=3)
b_four.grid(row=9, column=1)
b_five.grid(row=9, column=2)
b_six.grid(row=9, column=3)
b_one.grid(row=10, column=1)
b_two.grid(row=10, column=2)
b_three.grid(row=10, column=3)

body.mainloop()