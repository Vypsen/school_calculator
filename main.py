from tkinter import *

body = Tk()
body.title('calculator')
body.geometry('200x350')
body['bg'] = 'white'

numResult = 0
numInput = 0
event = ''

# добавление опредленной цифры в поле ввода 
def addDigit(digit):
    global numInput
    numInput = numInput*10+digit
    result.configure(text=numInput)

# получение определенной цифры
def addDigit_7():
    addDigit(7)

def addDigit_8():
    addDigit(8)

def addDigit_9():
    addDigit(9)

def addDigit_4():
    addDigit(4)

def addDigit_5():
    addDigit(5)

def addDigit_6():
    addDigit(6)

def addDigit_1():
    addDigit(1)

def addDigit_2():
    addDigit(2)

def addDigit_3():
    addDigit(3)

def addDigit_0():
    addDigit(0)

# вызов подсчёта запомнинание прошлого арифметического действия
def plus():
    count()
    global event 
    event = 'plus'

def minus():
    count()
    global event 
    event = 'minus'

def divide():
    count()
    global event
    event = 'divide'

def multiply():
    count()
    global event
    event = 'multiply'

# функция подсчёта
def count():
    global event
    global numInput
    # если ещё не было никаких действий
    global numResult
    if event == '' and numResult == 0:
        numResult = numInput
        numInput = 0
        result.configure(text=numResult)
    else:
        if event == 'plus':
            numResult += numInput
        elif event == 'minus':
            numResult -= numInput
        elif event == 'multiply':
            numResult *= numInput
        elif event == 'divide':
            numResult /= numInput
        event = ''
        numInput = 0
        result.configure(text=numResult)

# создание элементов интерфейса
result = Label(body, text='0', bg='white', font=('WhitehallCyr', 20))
b_plus = Button(body, text='+', bg='#BBBBBB', width=5, height=3, fg='black', command=plus)
b_min = Button(body, text='-', bg='#BBBBBB', width=5, height=3, fg='black', command=minus)
b_multiply = Button(body, text='*', bg='#BBBBBB', width=5, height=3, fg='black', command=multiply)
b_divide = Button(body, text='/', bg='#BBBBBB', width=5, height=3, fg='black', command=divide)
b_sev = Button(body, text='7', bg='#BBBBBB', width=5, height=3, fg='black', command=addDigit_7)
b_eight = Button(body, text='8', bg='#BBBBBB', width=5, height=3, fg='black', command=addDigit_8)
b_nin = Button(body, text='9', bg='#BBBBBB', width=5, height=3, fg='black', command=addDigit_9)
b_four = Button(body, text='4', bg='#BBBBBB', width=5, height=3, fg='black', command=addDigit_4)
b_five = Button(body, text='5', bg='#BBBBBB', width=5, height=3, fg='black', command=addDigit_5)
b_six = Button(body, text='6', bg='#BBBBBB', width=5, height=3, fg='black', command=addDigit_6)
b_one = Button(body, text='1', bg='#BBBBBB', width=5, height=3, fg='black', command=addDigit_1)
b_two = Button(body, text='2', bg='#BBBBBB', width=5, height=3, fg='black', command=addDigit_2)
b_three = Button(body, text='3', bg='#BBBBBB', width=5, height=3, fg='black', command=addDigit_3)
b_zero = Button(body, text='0', bg='#BBBBBB', width=5, height=3, fg='black', command=addDigit_0)
b_cleat = Button(body, text='C', bg='#BBBBBB', width=5, height=3, fg='black')
b_count = Button(body, text='==', bg='#BBBBBB', width=5, height=3, fg='black', command=count)

# добавление элементов интерфейса
result.grid(row=0, column=0, columnspan=4)
b_plus.grid(row=1, column=0)
b_min.grid(row=1, column=1)
b_multiply.grid(row=1, column=2)
b_divide.grid(row=1, column=3)
b_sev.grid(row=2, column=0)
b_eight.grid(row=2, column=1)
b_nin.grid(row=2, column=2)
b_four.grid(row=3, column=0)
b_five.grid(row=3, column=1)
b_six.grid(row=3, column=2)
b_one.grid(row=4, column=0)
b_two.grid(row=4, column=1)
b_three.grid(row=4, column=2)
b_zero.grid(row=5, column=1)
b_count.grid(row=2, column=3)

body.mainloop()