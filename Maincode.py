from tkinter import *
import math

project = Tk()
project.title("Calculator")
project.geometry("323x244")
project.resizable(0,0)
project.config(bg = "orange")

variable = StringVar()

field = Entry(project,textvariable=variable,justify=RIGHT,font=('times', 24))
field.grid(columnspan=4)

input = ""

def click(num):
	global input
	input = input + str(num)
	variable.set(input)
  
def equalbtn():
	try:
		global input
		total = str(eval(input))
		variable.set(total)
		input = ""
	except:
		variable.set(" error ")
		input = ""

def delete():
	global input
	dele = input[:-1]
	variable.set(dele)
    
def clear():
	global input
	input = ""
	variable.set("")

def sqroot():
	global input
	inp=str(math.sqrt(float(input)))
	variable.set(inp)
	input = ""

def factorial():
	global input 
	fact=1
	inp=(int(input))
	for i in range(1, inp+1):
		fact = fact * i
	inp=str(fact)
	variable.set(inp)
	input = ""
    
clear = Button(project, text=' c ', fg='black', bg='orange',command=clear, height=2, width=10)
clear.grid(row=2, column=0)

root = Button(project, text=' √ ', fg='black', bg='white',command=sqroot, height=2, width=10)
root.grid(row=2, column=1)

move = Button(project, text=' <- ', fg='black', bg='white',command=delete, height=2, width=10)
move.grid(row=2, column=2)

button7 = Button(project, text=' 7 ', fg='black', bg='white',command=lambda: click(7), height=2, width=10)
button7.grid(row=3, column=0)

button8 = Button(project, text=' 8 ', fg='black', bg='white',command=lambda: click(8), height=2, width=10)
button8.grid(row=3, column=1)

button9 = Button(project, text=' 9 ', fg='black', bg='white',command=lambda: click(9), height=2, width=10)
button9.grid(row=3, column=2)

button4 = Button(project, text=' 4 ', fg='black', bg='white',command=lambda: click(4), height=2, width=10)
button4.grid(row=4, column=0)

button5 = Button(project, text=' 5 ', fg='black', bg='white',command=lambda: click(5), height=2, width=10)
button5.grid(row=4, column=1)

button6 = Button(project, text=' 6 ', fg='black', bg='white',command=lambda: click(6), height=2, width=10)
button6.grid(row=4, column=2)

button1 = Button(project, text=' 1 ', fg='black', bg='white',command=lambda: click(1), height=2, width=10)
button1.grid(row=5, column=0)

button2 = Button(project, text=' 2 ', fg='black', bg='white', command=lambda: click(2), height=2, width=10)
button2.grid(row=5, column=1)

button3 = Button(project, text=' 3 ', fg='black', bg='white',command=lambda: click(3), height=2, width=10)
button3.grid(row=5, column=2)

divide = Button(project, text=' / ', fg='black', bg='white',command=lambda: click("/"), height=2, width=10)
divide.grid(row=2, column=3)

plus = Button(project, text=' + ', fg='black', bg='white',command=lambda: click("+"), height=2, width=10)
plus.grid(row=3, column=3)

minus = Button(project, text=' - ', fg='black', bg='white',command=lambda: click("-"), height=2, width=10)
minus.grid(row=4, column=3)

multiply = Button(project, text=' * ', fg='black', bg='white',command=lambda: click("*"), height=2, width=10)
multiply.grid(row=5, column=3)

equal = Button(project, text=' = ', fg='black', bg='white',command=equalbtn, height=2, width=10)
equal.grid(row=6, column=3)

button0 = Button(project, text=' 0 ', fg='black', bg='white',command=lambda: click(0), height=2, width=10)
button0.grid(row=6, column=1)

Decimal= Button(project, text='.', fg='black', bg='white',command=lambda: click('.'), height=2, width=10)
Decimal.grid(row=6, column=2)

Factorial= Button(project, text='!', fg='black', bg='white',command=factorial, height=2, width=10)
Factorial.grid(row=6, column=0)

project.mainloop()
