from tkinter import *

root=Tk()
root.title("SIMPLE CALCULATOR")


e =Entry(root,width=35,bg="green",fg="blue",borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#e.insert(0, "Enter your name: ")

def button_click(number):
  current=e.get()
  e.delete(0, END)
  e.insert(0,str(current) + str(number)

def button_clear():
  e.delete(0, END)

def button_add():
  first_num=e.get()
  global math
  math="addition"
  f_num=int(first_num)
  e.delete(0,END)


def button_equal():
  second_num=e.get()
  e.delete(0,END)
  if math == "addition":
    e.insert(0, f_num + int(second_num))
  if math == "subtraction":
    e.insert(0, f_num - int(second_num)) 
  if math == "multiplication":
    e.insert(0, f_num * int(second_num))
  if math == "division":
    e.insert(0, f_num / int(second_num))

def button_subtract():
  first_num=e.get()
  global math
  math="subtraction"
  f_num=int(first_num)
  e.delete(0,END)

def button_multiply():
  first_num=e.get()
  global math
  math="multiplication"
  f_num=int(first_num)
  e.delete(0,END)

def button_divide():
  first_num=e.get()
  global math
  math="division"
  f_num=int(first_num)
  e.delete(0,END)

#adds buttons to the screen
buttom_1=Button(root,text="1",padx=40, pady=20 ,command= Lambda: button_click(1) ) 
buttom_2=Button(root,text="2",padx=40, pady=20 ,command= Lambda: button_click(2))
buttom_3=Button(root,text="3",padx=40, pady=20 ,command= Lambda: button_click(3))
buttom_4=Button(root,text="4",padx=40, pady=20 ,command= Lambda: button_click(4))
buttom_5=Button(root,text="5",padx=40, pady=20 ,command= Lambda: button_click(5))
buttom_6=Button(root,text="6",padx=40, pady=20 ,command= Lambda: button_click(6))
buttom_7=Button(root,text="7",padx=40, pady=20 ,command=  Lambda: button_click(7))
buttom_8=Button(root,text="8",padx=40, pady=20 ,command=  Lambda: button_click(8))
buttom_9=Button(root,text="9",padx=40, pady=20 ,command=  Lambda: button_click(9))
buttom_0=Button(root,text="0",padx=40, pady=20 ,command= Lambda: button_click(0))
button_add=Button(root,text="+",padx=39, pady=20 ,command=button_add)
button_equal=Button(root,text="=",padx=91, pady=20 ,command= button_equal)
button_clear=Button(root,text="clear",padx=79, pady=20 ,command=button_clear)
button_subtract=Button(root,text="-",padx=41, pady=20 ,command=button_subtract)
button_multiply=Button(root,text="*",padx=40, pady=20 ,command=button_multiply)
button_divide=Button(root,text="/",padx=41, pady=20 ,command=button_divide)



#puts buttons on the screen
buttom_1.grid(row=3 ,column=0 )
buttom_2.grid(row=3 ,column=1 )
buttom_3.grid(row=3 ,column=2 )

buttom_4.grid(row=2 ,column=0 )
buttom_5.grid(row=2 ,column=1 )
buttom_6.grid(row=2 ,column=2 )

buttom_7.grid(row=1 ,column=0 )
buttom_8.grid(row=1 ,column=1 )
buttom_9.grid(row=1 ,column=2 )

buttom_0.grid(row=4 ,column=0 )
button_clear.grid(row=4 ,column=1,columnspan=2)
button_add.grid(row=5 ,column=0 )
button_equal.grid(row=5 ,column=1,columnspan=2)

button_subtract.grid(row=6 ,column=0 )
button_multiply.grid(row=6 ,column=1 )
button_divide.grid(row=6 ,column=2 )


root.mainloop()