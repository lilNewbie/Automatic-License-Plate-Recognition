import tkinter as tk
from app import app

class Form(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self, text="Input video:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.submit_button = tk.Button(
            self, text="Submit", command=self.submit_form)
        self.submit_button.pack()

        self.exit_button = tk.Button(
            self, text="Exit", command=self.master.destroy)
        self.exit_button.pack()

    def submit_form(self):
        source = self.name_entry.get()
        app(source)
        self.master.destroy()
        
root = tk.Tk()
root.geometry("400x300")
form = Form(master=root)
form.mainloop()


