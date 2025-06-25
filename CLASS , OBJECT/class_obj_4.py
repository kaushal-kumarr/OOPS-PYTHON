import tkinter as tk
from tkinter import messagebox
                                                # USING AI 

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x250")
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Enter a number:", font=("Arial", 12), bg="#f0f0f0")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.entry.pack()

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="Square", width=10, command=self.square).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Cube", width=10, command=self.cube).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Square Root", width=22, command=self.square_root).grid(row=1, column=0, columnspan=2, pady=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12, "bold"), fg="blue", bg="#f0f0f0")
        self.result_label.pack(pady=10)

    def get_number(self):
        try:
            return float(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
            return None

    def square(self):
        num = self.get_number()
        if num is not None:
            result = num ** 2
            self.result_label.config(text=f"Square: {result}")

    def cube(self):
        num = self.get_number()
        if num is not None:
            result = num ** 3
            self.result_label.config(text=f"Cube: {result}")

    def square_root(self):
        num = self.get_number()
        if num is not None:
            result = num ** 0.5
            self.result_label.config(text=f"Square Root: {result:.3f}")


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
