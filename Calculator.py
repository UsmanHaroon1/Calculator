from tkinter import *

class calc:

    def __init__(self,master):
        master.title('Calculator')
        master.geometry()

        frame = Frame(master,bg = "Light blue")
        frame.pack()

        self.editor = Entry(frame,bg = "LightGreen",width = 28)
        self.button1 = Button(frame, text = "1",width = 3,fg = "Black",command = lambda:self.buttonClick(1)).grid(row = 2, column = 0)
        self.button2 = Button(frame, text = "2",width = 3,fg = "Black",command = lambda:self.buttonClick(2)).grid(row = 2, column = 1)
        self.button3 = Button(frame, text = "3",width = 3,fg = "Black",command = lambda:self.buttonClick(3)).grid(row = 2, column = 2)
        self.button4 = Button(frame, text = "4",width = 3,fg = "Black",command = lambda:self.buttonClick(4)).grid(row = 3, column = 0)
        self.button5 = Button(frame, text = "5",width = 3,fg = "Black",command = lambda:self.buttonClick(5)).grid(row = 3, column = 1)
        self.button6 = Button(frame, text = "6",width = 3,fg = "Black",command = lambda:self.buttonClick(6)).grid(row = 3, column = 2)
        self.button7 = Button(frame, text = "7",width = 3,fg = "Black",command = lambda:self.buttonClick(7)).grid(row = 4, column = 0)
        self.button8 = Button(frame, text = "8",width = 3,fg = "Black",command = lambda:self.buttonClick(8)).grid(row = 4, column = 1)
        self.button9 = Button(frame, text = "9",width = 3,fg = "Black",command = lambda:self.buttonClick(9)).grid(row = 4, column = 2)
        self.button0 = Button(frame, text = "0",width = 3,fg = "Black",command = lambda:self.buttonClick(0)).grid(row = 5, column = 0,columnspan = 1)
        self.buttondot = Button(frame, text = ".",width = 3,fg = "Black",command = lambda:self.buttonClick('.')).grid(row = 5, column = 1,columnspan = 1)
        self.buttonplu = Button(frame,text = "+",width = 3,fg = "Black",command = lambda:self.buttonClick('+')).grid(row = 2,column = 3)
        self.buttonminus = Button(frame,text = "-",width = 3,fg = "Black",command = lambda:self.buttonClick('-')).grid(row = 3,column = 3)
        self.buttonmul = Button(frame,text = "*",width = 3,fg = "Black",command = lambda:self.buttonClick('*')).grid(row = 4,column = 3)
        self.buttondiv = Button(frame,text = "/",width = 3,fg = "Black",command = lambda:self.buttonClick('/')).grid(row = 5,column = 3)
        self.buttonclr = Button(frame,text = "AC",width = 5 ,height = 6, command = lambda:self.clear()).grid(row = 2,column = 6,columnspan = 1,rowspan = 4)

        self.buttonres = Button(frame,text = "=",width = 3,fg = "Black",command = self.buttonres).grid(row = 5, column = 2 ,columnspan = 1)

        self.editor.grid(row = 1,column = 0,columnspan = 8,sticky = W+E)

    def buttonClick(self,number):
        self.editor.insert(END,number)

    def clear(self):
        self.editor.delete(0,END)

    def buttonres(self):
        self.enterance = self.editor.get()
        try:
            self.results = eval(self.enterance)
        except SyntaxError or NameError or Exception:
            self.editor.delete(0,END)
            self.editor.insert(0,'Invalid Input!')
        except ZeroDivisionError:
            self.editor.delete(0,END)
            self.editor.insert(0,"Zero divisor error")
        else:
            self.editor.delete(0,END)
            self.editor.insert(0,self.results)
        print("Ok")

root = Tk()
b = calc(root)
root.mainloop()
