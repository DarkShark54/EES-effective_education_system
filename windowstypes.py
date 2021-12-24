from tkinter import *
#from view import index
from tkinter import messagebox
from tkinter import ttk

class Authorization():
   def __init__(self):
       # кортежи и словари, содержащие настройки шрифтов и отступов
       self.font_header = ('Roboto', 15)
       self.font_entry = ('Roboto', 12)
       self.label_font = ('Roboto', 11)
       self.base_padding = {'padx': 10, 'pady': 8}
       self.header_padding = {'padx': 10, 'pady': 12}
       self.window = Tk()
       self.window.geometry('250x270')
       self.data = None
       main_label = Label(self.window,
                   text='Login',
                   font=self.font_header,
                   justify=CENTER,
                   **self.header_padding)
       main_label.pack()

       self.username_entry = Entry(self.window,
                       bg='#fff',
                       fg='#444',
                       font=self.font_entry)
       self.username_entry.pack()

       password_label = Label(self.window,
                       text='Password',
                       font=self.label_font,
                       **self.base_padding)
       password_label.pack()


       self.password_entry = Entry(self.window,
                       bg='#fff',
                       fg='#444',
                       font=self.font_entry)
       self.password_entry.pack()


       send_btn = Button(self.window,
                  text='          Enter          ',
                  command=self.button)
       send_btn.pack()
       self.window.mainloop()

   def quit(self):
       self.window.destroy()
   def button(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        professor_id = index("POST","authorization",[username,password])
        if professor_id:
            self.data = professor_id
            self.quit()
        else:
            messagebox.showinfo('Error', 'Incorrect')

class mainwindow():
   def __init__(self, id):
         # кортежи и словари, содержащие настройки шрифтов и отступов
       self.font_header = ('Roboto', 15)
       self.font_entry = ('Roboto', 12)
       self.label_font = ('Roboto', 11)
       self.base_padding = {'padx': 10, 'pady': 8}
       self.header_padding = {'padx': 10, 'pady': 12}
       self.window = Tk()
       self.window.geometry('920x580')
       self.data = index("GET", "data_client", id)

       self.window.columnconfigure(0, weight=0)
       self.window.columnconfigure(0, pad=0)
       self.window.rowconfigure(0, weight=0)
       self.window.rowconfigure(0, pad=10)

       self.window.rowconfigure(1, weight=0)
       self.window.rowconfigure(1, pad=10)

       self.window.rowconfigure(2, weight=0)
       self.window.rowconfigure(2, pad=10)

       self.window.rowconfigure(3, weight=0)
       self.window.rowconfigure(3, pad=80)


       self.classcombo = ttk.Combobox(self.window,values=[
                                    "1А Класс",
                                    "2Б Класс",
                                    "3А Класс",
                                    "4А Класс",
                                    "5А Класс"]
                                      )
       #opts = { 'ipadx': 10, 'ipady': 10, 'sticky': 'nwse' }
       opts1 = { 'ipadx': 40, 'ipady': 10, 'sticky': 's' }

       self.classcombo.grid(column=0, row=1, ipady=40,ipadx=20)
       self.classcombo.current(0)

       print( self.classcombo.current(),  self.classcombo.get())

       subj_value = [key for key in self.data.key()]
       self.subjectcombo = ttk.Combobox(self.window,values= subj_value,
                                        postcommand = changeclass(self))

       self.subjectcombo.grid(column=0, row=0, ipady=40,ipadx=20)
       self.subjectcombo.current(0)

       print( self.subjectcombo.current(),  self.subjectcombo.get())

       form_btn = Button(self.window,
                  font = self.font_header,
                  text='Сформировать',
                  command=self.button)
       form_btn.grid(column=0, row=3, ipady=40,ipadx=20, sticky='s')


       self.window.mainloop()
   def changeclass(self):
       currentsubj = self.subjectcombo.get()
       classvalue = [value for value in self.data.value()]
       self.classcombo.config(value = classvalue)

   def button(self):
    return
