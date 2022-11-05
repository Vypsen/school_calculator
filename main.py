from tkinter import *

window_root = Tk()
window_root.title('calculator')
window_root.geometry('300x400')
window_root['bg'] = 'white'

num_1 = 0
def addDigit7():
    global num_1
    num_1 = num_1*10 + 7
    result.configure(text=num_1)
    
    3^2
result = Label(window_root, text='0', bg='white', font=('Arial Bolt', 30))
b_plus = Button(window_root, text='+', bg='grey', width=8, height=5, fg='black')
b_minus = Button(window_root, text='-', bg='grey', width=8, height=5, fg='black')
b_um = Button(window_root, text='*', bg='grey', width=8, height=5, fg='black')
b_del = Button(window_root, text='/', bg='grey', width=8, height=5, fg='black')
b_7 = Button(window_root, text='7', bg='grey', width=8, height=5, fg='black', command=addDigit7)
b_8 = Button(window_root, text='8', bg='grey', width=8, height=5, fg='black')
b_9 = Button(window_root, text='9', bg='grey', width=8, height=5, fg='black')

result.grid(row=0, column=0, columnspan=4)
b_plus.grid(row=1,column=0)
b_minus.grid(row=1,column=1)
b_um.grid(row=1,column=2)
b_del.grid(row=1,column=3)
b_7.grid(row=2,column=0)
b_8.grid(row=2,column=1)
b_9.grid(row=2,column=2)

window_root.mainloop()



