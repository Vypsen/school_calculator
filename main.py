from tkinter import *

window = Tk()
window.title('calculator')
window.geometry('262x400')
window['bg'] = 'white'


NUM_1 = 0
def addDigit_7():
    global NUM_1
    NUM_1 = NUM_1*10 + 7
    result.configure(text=NUM_1)

result = Label(window, text='0', bg='white', font = ('Arial Bold', 30))
b_plus = Button(window, text = '+', bg='grey', width=8, height=5, fg='black')
b_minus = Button(window, text = '-', bg='grey', width=8, height=5, fg='black')
b_um = Button(window, text = '*', bg='grey', width=8, height=5, fg='black')
b_del = Button(window, text = '/', bg='grey', width=8, height=5, fg='black')
b_seven= Button(window, text = '7', bg='white', width=8, height=5, fg='black', command=addDigit_7)


result.grid(row=0, column=0, columnspan=4)
b_plus.grid(row=1, column=0)
b_minus.grid(row=1, column=1)
b_um.grid(row=1, column=2)
b_del.grid(row=1, column=3)
b_seven.grid(row=2, column=0)

window.mainloop()