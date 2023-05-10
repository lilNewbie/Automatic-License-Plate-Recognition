import tkinter as tk
from app import app

class Form(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.option_label = tk.Label(self, text="Input Type:")
        self.option_label.pack()
        self.option_var = tk.StringVar(self)
        self.option_var.set("Local file")
        self.option_dropdown = tk.OptionMenu(
            self, self.option_var, "Local file", "YouTube", "Image")
        self.option_dropdown.pack()

        self.name_label = tk.Label(self, text="Input:")
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
        option = self.option_var.get()
        app(source, option)
        self.master.destroy()
        
root = tk.Tk()
root.geometry("400x300")
form = Form(master=root)
form.mainloop()


