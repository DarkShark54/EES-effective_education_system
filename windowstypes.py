from tkinter import *
from view import index
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
       self.data = 0
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
                  command=self.button, bg="#009393",fg='#ffffff')
       send_btn.pack()
       self.window.mainloop()

   def quit(self):
       self.window.destroy()
   def button(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        professor_id = index("POST","authorization", [username, password])
        if professor_id:
            self.data = professor_id[0][0]
            self.quit()
        else:
            messagebox.showinfo('Error', 'Incorrect')



class mainwindow():
   def __init__(self, id):
         # кортежи и словари, содержащие настройки шрифтов и отступов
       self.font_header = ('Roboto', 14)
       self.font_entry = ('Roboto', 12)
       self.font_label = ('Roboto', 11)
       self.base_padding = {'padx': 10, 'pady': 8}
       self.header_padding = {'padx': 10, 'pady': 12}
       self.window = Tk()
       self.window.geometry('1520x580')
       self.data = index("GET", "data_client", id)

       self.window.columnconfigure(0, weight=0)
       self.window.columnconfigure(0, pad=0)
       self.window.rowconfigure(0, weight=0)
       self.window.rowconfigure(0, pad=10)

       self.window.columnconfigure(1, weight=0)
       self.window.columnconfigure(1, pad=0)
       self.window.rowconfigure(1, weight=0)
       self.window.rowconfigure(1, pad=10)

       self.window.columnconfigure(2, weight=0)
       self.window.columnconfigure(2, pad=0)
       self.window.rowconfigure(2, weight=0)
       self.window.rowconfigure(2, pad=10)

       self.window.columnconfigure(3, weight=0)
       self.window.columnconfigure(3, pad=0)
       self.window.rowconfigure(3, weight=0)
       self.window.rowconfigure(3, pad=10)

       self.window.columnconfigure(4, weight=0)
       self.window.columnconfigure(4, pad=0)
       self.window.rowconfigure(4, weight=0)
       self.window.rowconfigure(4, pad=10)

       self.window.columnconfigure(5, weight=0)
       self.window.columnconfigure(5, pad=0)
       self.window.rowconfigure(5, weight=0)
       self.window.rowconfigure(5, pad=10)

       self.window.columnconfigure(6, weight=0)
       self.window.columnconfigure(6, pad=0)
       self.window.rowconfigure(6, weight=0)
       self.window.rowconfigure(6, pad=10)

       self.canvas_list = []
       self.button_list = []

       self.label = Label()
       self.label.grid(column=1000, row=0)
       self.classcombo = ttk.Combobox(self.window)

       self.classcombo.grid(column=0, row=1, ipady=10,ipadx=20)


       print( self.classcombo.current(),  self.classcombo.get())

       subj_value = [key for key in self.data.keys()]
       self.subjectcombo = ttk.Combobox(self.window,values= subj_value,
                                        postcommand = self.changeclass)

       self.subjectcombo.grid(column=0, row=0, ipady=10,ipadx=20)
       self.subjectcombo.current(0)


       print( self.subjectcombo.current(),  self.subjectcombo.get())

       form_btn = Button(self.window,
                  font = self.font_header,
                  text='Сформировать',
                  command=self.tree_button,bg="#009393",fg='#ffffff')
       form_btn.grid(column=0, row=2, ipady=10,ipadx=20,pady= 5, sticky='s')

       self.sript_label1 = Label(font = self.font_label,text="Тема не пройдена",background="#DBDBDB")
       self.sript_label1.grid(column=0, row=3, ipady=10,ipadx=20, sticky='nswe')
       self.sript_label2 = Label(font = self.font_label,text="Тема усвоена не полностью",background="#FFFB98")
       self.sript_label2.grid(column=0, row=4, ipady=10,ipadx=20, sticky='nswe')
       self.sript_label3 = Label(font = self.font_label,text="Тема не усвоена",background="#FF7272")
       self.sript_label3.grid(column=0, row=5, ipady=10,ipadx=20, sticky='nswe')
       self.sript_label4 = Label(font = self.font_label,text="Тема усвоена полностью",background="#9BFF92")
       self.sript_label4.grid(column=0, row=6, ipady=10,ipadx=20,  sticky='nswe')

       self.window.mainloop()

   def changeclass(self):
       currentsubj = self.subjectcombo.get()
       classvalue = self.data[currentsubj]
       self.classcombo.config(value = classvalue)

   def tree_button(self):


    dict_subj_of_theme_subtopic = index("GET", "subj_theme", self.subjectcombo.get().split(' ')[0])
    self.label = Label(font = self.font_header,text="",background="#FFF")
    count = 0
    for k in dict_subj_of_theme_subtopic.keys():
        count+=1

        count += len(dict_subj_of_theme_subtopic[k])
    print(count)
    i = 0
    j=0
    if self.button_list:
        for i in range(0,len(self.button_list)):
            for j in range(0,len(self.button_list[i])):
                self.button_list[i][j].grid_remove()
    i = 0
    j=0
    if self.canvas_list:
        for i in range(0,len(self.canvas_list)):
            for j in range(0,len(self.canvas_list[i])):
                self.canvas_list[i][j].grid_remove()
    i = 0
    j=0
    for maintopic in dict_subj_of_theme_subtopic.keys():
     self.button_list.append([])
     self.canvas_list.append([])
     i+=1
     self.button_list[i-1].append( Button(self.window,font = self.font_header, text=maintopic, command = lambda button_text = maintopic: self.script_button(button_text)))
     self.button_list[i-1][0].grid(column=i, row=0, ipady=10, ipadx=20, padx = 20,sticky='s')

     j=0
     for subtopic in dict_subj_of_theme_subtopic[maintopic]:

        j+=1
        self.canvas_list[i-1].append(Canvas(self.window,width=120, height=50))
        self.canvas_list[i-1][j-1].create_line(100, 0, 100, 150)
        self.canvas_list[i-1][j-1].grid(column=i, row=j, ipady=10, ipadx=20, padx=0, pady=0, sticky='n')

        self.button_list[i-1].append( Button(self.window,font = self.font_header, text = subtopic, command = lambda button_text = subtopic: self.script_button(button_text)))
        self.button_list[i-1][j].grid(column=i, row=j, ipady=10, ipadx=20, padx=10, sticky='s')


   def script_button(self, button_name):
        list_students_marks = index("GET", "students_marks", [button_name, self.classcombo.get()])
        print(list_students_marks)
        self.label.config(text=list_students_marks)
        self.label.grid(column=1000, row=0)


