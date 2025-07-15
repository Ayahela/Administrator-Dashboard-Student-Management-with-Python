from tkinter import *
# class Student:
#      def __init__(self,root):
        #   self.root=root
        #   self.root.geometry('1350x690')
        #   self.root.title

root=Tk()
# ob=Student(root)
root.geometry('1350x690')
# root.resizable(False,True)
root.title('student managment app')
title=Label(root, 
text='Student registration system',
bg="black",
font=('momospace',14,'bold'),
fg="white"
)

title.pack(fill='x')
root.config(background='silver')
root.mainloop()