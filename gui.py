import tkinter
from tkinter import *
from tkinter import messagebox
# my name is 
def call(number):
   global operator
   operator = operator+str(number)
   text_input.set(operator)

def clear():
   text_input.set("")

def equal():
   global operator
   sumup=str(eval(operator))
   text_input.set(sumup)
   operator=sumup

   

root=Tk()
root.title('Calculator')
operator=""
text_input=StringVar()

enter=Entry(root, bd=5, relief="raised", textvariable=text_input, justify="right", bg="grey", fg="white")
enter.grid(row=1, column=1)

frame1=Frame(root)

b1=Button(frame1, text="1", command=lambda:call(1), bg="sky blue", fg="white", activebackground="gray", bd=4, padx=8, pady=5)
b1.grid(row=1, column=1)
b2=Button(frame1, text="2", command=lambda:call(2), bg="sky blue", fg="white", activebackground="gray", bd=4, padx=8, pady=5)
b2.grid(row=1, column=2)
b3=Button(frame1, text="3", command=lambda:call(3), bg="sky blue", fg="white", activebackground="gray", bd=4, padx=8, pady=5)
b3.grid(row=1, column=3)
add=Button(frame1, text="+", command=lambda:call("+"), bd=4, padx=8, pady=5)
add.grid(row=1, column=4)

b4=Button(frame1, text="4", command=lambda:call(4), bg="sky blue", fg="white", activebackground="gray", bd=4, padx=8, pady=5)
b4.grid(row=2, column=1)
b5=Button(frame1, text="5", command=lambda:call(5), bg="sky blue", fg="white", activebackground="gray", bd=4, padx=8, pady=5)
b5.grid(row=2, column=2)
b6=Button(frame1, text="6", command=lambda:call(6), bg="sky blue", fg="white", activebackground="gray", bd=4, padx=8, pady=5)
b6.grid(row=2, column=3)
sub=Button(frame1, text="-", command=lambda:call("-"), bd=4, padx=8, pady=5)
sub.grid(row=2, column=4)


b7=Button(frame1, text="7", command=lambda:call(7), bg="sky blue", fg="white", activebackground="gray", bd=4, padx=8, pady=5)
b7.grid(row=3, column=1)
b8=Button(frame1, text="8", command=lambda:call(8), bg="sky blue", fg="white", activebackground="gray", bd=4, padx=8, pady=5)
b8.grid(row=3, column=2)
b9=Button(frame1, text="9", command=lambda:call(9), bg="sky blue", fg="white", activebackground="gray", bd=4, padx=8, pady=5)
b9.grid(row=3, column=3)
multi=Button(frame1, text="*", command=lambda:call("*"), bd=4, padx=8, pady=5)
multi.grid(row=3, column=4)

b9=Button(frame1, text="0", command=lambda:call(0), bg="sky blue", fg="white", activebackground="gray", bd=4, padx=8, pady=5)
b9.grid(row=4, column=1)
div=Button(frame1, text="c", command=clear, bd=4, padx=8, pady=5)
div.grid(row=4, column=2)
div=Button(frame1, text="/", command=lambda:call("/"), bd=4, padx=8, pady=5)
div.grid(row=4, column=3)
equalto=Button(frame1, text="=", command=equal, bd=4, padx=8, pady=5)
equalto.grid(row=4, column=4)



frame1.grid(row=2, column=1)

root.mainloop()