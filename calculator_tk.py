import tkinter as tk

class MacCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x480")
        self.root.configure(bg="#1C1C1C")
        self.root.resizable(False, False)

        self.expression = ""

        # Display
        self.display = tk.Entry(root, font=("Arial", 32), bg="#1C1C1C", fg="white",
                                bd=0, justify="right", insertbackground="white")
        self.display.pack(fill="both", padx=15, pady=20, ipady=15)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#1C1C1C")
        btn_frame.pack()

        # Button layout - Mac style
        buttons = [
            ('AC', 1, 0, "#A5A5A5", "black"), ('+/-', 1, 1, "#A5A5A5", "black"), ('%', 1, 2, "#A5A5A5", "black"), ('÷', 1, 3, "#FF9F0A", "white"),
            ('7', 2, 0, "#333333", "white"), ('8', 2, 1, "#333333", "white"), ('9', 2, 2, "#333333", "white"), ('×', 2, 3, "#FF9F0A", "white"),
            ('4', 3, 0, "#333333", "white"), ('5', 3, 1, "#333333", "white"), ('6', 3, 2, "#333333", "white"), ('-', 3, 3, "#FF9F0A", "white"),
            ('1', 4, 0, "#333333", "white"), ('2', 4, 1, "#333333", "white"), ('3', 4, 2, "#333333", "white"), ('+', 4, 3, "#FF9F0A", "white"),
            ('0', 5, 0, "#333333", "white", 2), ('.', 5, 2, "#333333", "white"), ('=', 5, 3, "#FF9F0A", "white"),
        ]

        for btn in buttons:
            text, r, c, bg, fg = btn[0], btn[1], btn[2], btn[3], btn[4]
            colspan = btn[5] if len(btn) > 5 else 1

            b = tk.Button(btn_frame, text=text, font=("Arial", 20, "bold"),
                          bg=bg, fg=fg, bd=0, width=4 if colspan==1 else 9, height=1,
                          command=lambda t=text: self.on_click(t))
            b.grid(row=r, column=c, columnspan=colspan, padx=5, pady=5, ipadx=5, ipady=10, sticky="nsew")

    def on_click(self, char):
        if char == 'AC':
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                exp = self.expression.replace('×', '*').replace('÷', '/')
                result = str(eval(exp))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.expression = result
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""
        elif char == '+/-':
            if self.expression:
                try:
                    val = float(self.expression)
                    self.expression = str(-val)
                    self.display.delete(0, tk.END)
                    self.display.insert(0, self.expression)
                except: pass
        else:
            self.expression += char
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = MacCalculator(root)
    root.mainloop()