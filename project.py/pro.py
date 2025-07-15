from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry('1350x690')
root.title('student managment app')
title=Label(root, 
text='Student registration system',
bg="darkred",
font=('momospace',14,'bold'),
fg="white"
)
title.pack(fill='x')    #العنصر هيكون ف الوضع الافقي
root.config(background='gray')
#########################################################
Manage_Frame = Frame(root, bg='white')
Manage_Frame.place(x=1137, y=30, width=210, height=400)
lbl = Label(
    Manage_Frame,
    text='Student Form',
    foreground='darkred',
    font=('Arial', 14, 'bold'),
    bg='white'
)
lbl.grid(row=0, column=0, columnspan=2, pady=10)
#ID
lbl_ID=Label(Manage_Frame,text='ID',bg='white')
lbl_ID.grid(row=1,column=0, padx=7, pady=5)
txt_ID=Entry(Manage_Frame,bd='2')    #to make border
txt_ID.grid(row=1,column=1, padx=7, pady=5)
#Name
lbl_name=Label(Manage_Frame,text='Name',bg='white')
lbl_name.grid(row=2,column=0, padx=7, pady=5)
txt_name=Entry(Manage_Frame,bd='2')    #to make border
txt_name.grid(row=2,column=1, padx=7, pady=5)
#Email
lbl_Email=Label(Manage_Frame,text='Email',bg='white')
lbl_Email.grid(row=3,column=0, padx=7, pady=5)
txt_Email=Entry(Manage_Frame,bd='2')
txt_Email.grid(row=3,column=1, padx=7, pady=5)
###phone
lbl_Phone=Label(Manage_Frame,text='Phone',bg='white')
lbl_Phone.grid(row=4,column=0, padx=7, pady=5)
txt_Phone=Entry(Manage_Frame,bd='2')
txt_Phone.grid(row=4,column=1, padx=7, pady=5)
####certificate
lbl_Certificate=Label(Manage_Frame,text='Certificate',bg='white')
lbl_Certificate.grid(row=5,column=0, padx=1, pady=5)
txt_Certificate=Entry(Manage_Frame,bd='2')
txt_Certificate.grid(row=5,column=1, padx=1, pady=5)
#Gender
lbl_Gender=Label(Manage_Frame,text='Gender',bg='white')
lbl_Gender.grid(row=6,column=0, padx=1, pady=5)
combo_Gender = ttk.Combobox(Manage_Frame)
combo_Gender['values'] = ['Male', 'Female']
combo_Gender.grid(row=6,column=1, padx=1, pady=5)
#address
lbl_Address=Label(Manage_Frame,text='Address',bg='white')
lbl_Address.grid(row=7,column=0, padx=1, pady=5)
txt_Address=Entry(Manage_Frame,bd='2')
txt_Address.grid(row=7,column=1, padx=1, pady=5)
root.mainloop()
