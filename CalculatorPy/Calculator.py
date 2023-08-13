import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x350")
        self.resizable(0,0)
        self.title("Calculator")
        self.iconbitmap("Calculator.ico")

        self.expression = ""
        self.input = None
        self.TextInput = tk.StringVar()
        self._ComponentCreation()

    def _ComponentCreation(self):
        InputFrame = tk.Frame(self, width=400, height=50, bg="grey")
        InputFrame.pack(side=tk.TOP)
        Input = tk.Entry(InputFrame, font=("arial", 18, "bold"), textvariable=self.TextInput, width=30, justify=tk.RIGHT)
        Input.grid(row=0, column=0, ipady=10)

        ButtonsFrame = tk.Frame(self, width=400, height=450, bg="grey")
        ButtonsFrame.pack()

        ButtonClean = tk.Button(ButtonsFrame, text="Clear", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=self._EventClean)
        ButtonClean.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        ButtonDivide = tk.Button(ButtonsFrame, text="/", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda:self._EventClick("/"))
        ButtonDivide.grid(row=0, column=3, padx=1, pady=1)

        ButtonSeven = tk.Button(ButtonsFrame, text="7", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda:self._EventClick(7))
        ButtonSeven.grid(row=1, column=0, padx=1, pady=1)

        ButtonEight = tk.Button(ButtonsFrame, text="8", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda:self._EventClick(8))
        ButtonEight.grid(row=1, column=1, padx=1, pady=1)

        ButtonNine = tk.Button(ButtonsFrame, text="9", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda:self._EventClick(9))
        ButtonNine.grid(row=1, column=2, padx=1, pady=1)

        ButtonMultiply = tk.Button(ButtonsFrame, text="*", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda:self._EventClick("*"))
        ButtonMultiply.grid(row=1, column=3, padx=1, pady=1)

        ButtonFour = tk.Button(ButtonsFrame, text="4", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda:self._EventClick(4))
        ButtonFour.grid(row=2, column=0, padx=1, pady=1)

        ButtonFive = tk.Button(ButtonsFrame, text="5", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda:self._EventClick(5))
        ButtonFive.grid(row=2, column=1, padx=1, pady=1)

        ButtonSix = tk.Button(ButtonsFrame, text="6", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda:self._EventClick(6))
        ButtonSix.grid(row=2, column=2, padx=1, pady=1)

        ButtonSubtract = tk.Button(ButtonsFrame, text="-", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda:self._EventClick("-"))
        ButtonSubtract.grid(row=2, column=3, padx=1, pady=1)

        ButtonOne = tk.Button(ButtonsFrame, text="1", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda:self._EventClick(1))
        ButtonOne.grid(row=3, column=0, padx=1, pady=1)

        ButtonTwo = tk.Button(ButtonsFrame, text="2", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda:self._EventClick(2))
        ButtonTwo.grid(row=3, column=1, padx=1, pady=1)

        ButtonThree = tk.Button(ButtonsFrame, text="3", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda:self._EventClick(3))
        ButtonThree.grid(row=3, column=2, padx=1, pady=1)

        ButtonAdd = tk.Button(ButtonsFrame, text="+", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda:self._EventClick("+"))
        ButtonAdd.grid(row=3, column=3, padx=1, pady=1)

        ButtonZero = tk.Button(ButtonsFrame, text="0", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda:self._EventClick(0))
        ButtonZero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

        ButtonPoint = tk.Button(ButtonsFrame, text=".", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda:self._EventClick("."))
        ButtonPoint.grid(row=4, column=2, padx=1, pady=1)

        ButtonEquals = tk.Button(ButtonsFrame, text="=", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=self._EventEquals)
        ButtonEquals.grid(row=4, column=3, padx=1, pady=1)

    def _EventClean(self):
        self.expression = ""
        self.TextInput.set(self.expression)

    def _EventClick(self, Element):
        self.expression = f"{self.expression}{Element}"
        self.TextInput.set(self.expression)

    def _EventEquals(self):
        try:
            if self.expression:
                Result = str(eval(self.expression))
                self.TextInput.set(Result)
        except Exception as e:
            messagebox.showerror("Error", f"{e}")
            self.TextInput.set("")
        finally:
            self.expression = ""

if __name__=="__main__":
    calculator = Calculator()
    calculator.mainloop()