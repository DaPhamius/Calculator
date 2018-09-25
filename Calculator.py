from tkinter import *


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualInput():
    global operator, historyText
    historyText.set(operator)
    sumup= str(round(eval(operator), 10))
    text_Input.set(sumup)
    operator = sumup

def btnNegative():
    global operator, text_Input
    if text_Input.get()[0] == "-":
        text_Input.set(text_Input.get()[1:])
        operator = operator[1:]
    else:
        text_Input.set("-("+text_Input.get()+")")
        operator = "-("+operator+")"

def btnBackspace():
    global operator
    text_Input.set(text_Input.get()[:-1])
    operator = operator[:-1]


cal = Tk()
cal.title = ("Calculator")
operator = ""
text_Input = StringVar()

historyText = StringVar()

historyText.set("")
inputHistory = Label(cal, textvariable=historyText, font=("arial", 20, 'bold'), bd= 30, bg = "silver", anchor=E).grid( row=0, columnspan = 100, sticky = W+E)

#Display
#-------------
txtDisplay = Entry(cal, font=("arial", 20, "bold",), textvariable = text_Input, bd = 30, insertwidth = 3, bg ="silver", justify = "right").grid(row=1, columnspan=4)


#Buttons:

#First row of buttons
#-----------------------------------
btn7=Button(cal, padx = 16, pady=10,bd = 8, fg = "black", font =("arial", 20, "bold"), text="7", command=lambda:btnClick(7)).grid(row=2,column =0)
btn8=Button(cal, padx = 16, pady=10,bd = 8, fg = "black", font =("arial", 20, "bold"), text="8", command=lambda:btnClick(8)).grid(row=2,column =1)
btn9=Button(cal, padx = 16, pady=10,bd = 8, fg = "black", font =("arial", 20, "bold"), text="9",command=lambda:btnClick(9)).grid(row=2,column =2)
btnBackspace=Button(cal, padx = 7, pady=4,bd = 8, fg = "black", font =("arial", 20, "bold"), text="Del", command=btnBackspace).grid(row=2,column =3)

#Second row of buttons
#=========================================62

btn4=Button(cal, padx = 16, pady=10,bd = 8, fg = "black", font =("arial", 20, "bold"), text="4", command=lambda:btnClick(4)).grid(row=3,column =0)
btn5=Button(cal, padx = 16, pady=10,bd = 8, fg = "black", font =("arial", 20, "bold"), text="5", command=lambda:btnClick(5)).grid(row=3,column =1)
btn6=Button(cal, padx = 16, pady=10,bd = 8, fg = "black", font =("arial", 20, "bold"), text="6", command=lambda:btnClick(6)).grid(row=3,column =2)
Addition=Button(cal, padx = 16, pady=10,bd = 8, fg = "black", font =("arial", 20, "bold"), text="+", command=lambda:btnClick("+")).grid(row=3,column =3)

#Third row of buttons
#=========================================

btn1=Button(cal, padx = 16, pady=10,bd = 8, fg = "black", font =("arial", 20, "bold"), text="1", command=lambda:btnClick(1)).grid(row=4,column =0)
btn2=Button(cal, padx = 16, pady=10,bd = 8, fg = "black", font =("arial", 20, "bold"), text="2", command=lambda:btnClick(2)).grid(row=4,column =1)
btn3=Button(cal, padx = 16, pady=10,bd = 8, fg = "black", font =("arial", 20, "bold"), text="3", command=lambda:btnClick(3)).grid(row=4,column =2)
Substraction=Button(cal, padx = 16, pady=10,bd = 8, fg = "black", font =("arial", 20, "bold"), text="-", command=lambda:btnClick("-")).grid(row=4,column =3)

#Fourth row of buttons
#==========================================
btn0=Button(cal, padx = 16, pady=10, bd = 8, fg = "black", font =("arial", 20, "bold"), text="0", command=lambda:btnClick(0)).grid(row=5,column =0)
btnComma=Button(cal, padx = 16, pady=10, bd = 8, fg = "black", font =("arial", 20, "bold"), text=".", command=lambda:btnClick(".")).grid(row=5,column =1)
btnEqual=Button(cal, padx = 16, pady=10,bd = 8, fg = "black", font =("arial", 20, "bold"), text="=", command=btnEqualInput).grid(row=5,column =2)
Multiplcation=Button(cal, padx = 16, pady=10,bd = 8, fg = "black", font =("arial", 20, "bold"), text="*", command=lambda:btnClick("*")).grid(row=5,column =3)



#==========================================
Division=Button(cal, padx = 16, pady=10,bd = 8, fg = "black", font =("arial", 20, "bold"), command=lambda:btnClick("/"), text="/").grid(row=6,column =3)
benClear=Button(cal, padx=16, pady=10, bd=8, fg="black", font=("arial", 20, "bold"), text="C", command= btnClearDisplay).grid(row=6, column=2)
btnParantesesOpen=Button(cal, padx = 1, pady=4,bd = 6, fg = "black", font =("arial", 20, "bold"), text="(", command=lambda:btnClick("(")).grid(row=6,column =0, sticky="W")
btnParantesesClose=Button(cal, padx = 1, pady=4,bd = 6, fg = "black", font =("arial", 20, "bold"), text=")", command=lambda:btnClick(")")).grid(row=6,column =0, sticky="E")
btnNegative=Button(cal, padx =16, pady=10, bd=8, fg="black", font=("arial", 20, "bold"), text="+-", command=btnNegative).grid(row=6, column=1)

cal.mainloop()
