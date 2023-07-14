import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Entry widget to display input/output
        self.display = tk.Entry(self.master, width=25, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons for digits 0-9
        for i in range(10):
            tk.Button(self.master, text=str(i), width=5, height=2, command=lambda x=i: self.button_click(str(x))).grid(row=1 + i // 3, column=i % 3)

        # Other buttons
        tk.Button(self.master, text="+", width=5, height=2, command=lambda: self.button_click("+")).grid(row=4, column=0)
        tk.Button(self.master, text="-", width=5, height=2, command=lambda: self.button_click("-")).grid(row=4, column=1)
        tk.Button(self.master, text="*", width=5, height=2, command=lambda: self.button_click("*")).grid(row=4, column=2)
        tk.Button(self.master, text="/", width=5, height=2, command=lambda: self.button_click("/")).grid(row=5, column=0)
        tk.Button(self.master, text="C", width=5, height=2, command=self.clear_display).grid(row=5, column=1)
        tk.Button(self.master, text="=", width=5, height=2, command=self.calculate).grid(row=5, column=2)

    def button_click(self, text):
        self.display.insert(tk.END, text)

    def clear_display(self):
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.clear_display()
            self.display.insert(tk.END, result)
        except:
            self.clear_display()
            self.display.insert(tk.END, "Error")

if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
