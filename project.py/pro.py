def Center():
   #The size of the window
   win_width  = 1350
   win_height = 690
   #get the size of the screen
   screen_width = root.winfo_screenwidth()
   screen_height = root.winfo_screenheight()
   #place the window on the x-y coordinates
   x = (screen_width // 2) - (win_width // 2)
   y = (screen_height // 2) - (win_height // 2)
   #center the window 
   root.geometry(f"{win_width}x{win_height}+{x}+{y}")
   root.resizable(False,False)
from tkinter import *
from tkinter import ttk
root=Tk()
Center()
#root.geometry('1350x690')
root.title('student managment app')
# root.resizable(False,False)
title=Label(root, 
text='Student registration system',
bg="darkred",
font=('momospace',14,'bold'),
fg="white"
)
title.pack(fill='x')    
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
########################################
#-------Management buttons------
btn_frame=Frame(root, bg="white")
btn_frame.place(x=1137,y=435,width=210,height=253)
title1=Label( 
             btn_frame,
             text="Manage Students",
             font=('Deco',14,'bold'),
             fg='darkred', 
             bg='white')
title1.pack(fill=X)

add_btn = Button(btn_frame, text="Add Student", bg="darkred", fg="white")
add_btn.place(x=33, y=30, width=150, height=30)

del_btn = Button(btn_frame, text="Delete Student", bg="darkred", fg="white")
del_btn.place(x=33, y=65, width=150, height=30)

update_btn = Button(btn_frame, text="Update Data", bg="darkred", fg="white")
update_btn.place(x=33, y=100, width=150, height=30)

clear_btn = Button(btn_frame, text="Clear Fields", bg="darkred", fg="white")
clear_btn.place(x=33, y=135, width=150, height=30)

about_btn = Button(btn_frame, text="About Us", bg="darkred", fg="white")
about_btn.place(x=33, y=170, width=150, height=30)

exit_btn = Button(btn_frame, text="Exit", bg="darkred", fg="white")
exit_btn.place(x=33, y=205, width=150, height=30)
<<<<<<< HEAD
#show dietals
Dietals_Frame=Frame(root,bg='#F2F4F4')
Dietals_Frame.place(x=1,y=82,width=1134,height=605)
#scroll creation
Scroll_x=Scrollbar(Dietals_Frame,orient=HORIZONTAL)
Scroll_y=Scrollbar(Dietals_Frame,orient=VERTICAL)
#treeview
Student_Table=ttk.Treeview(Dietals_Frame,
                          columns=('address','gender','certie','phone','emil','name','id'),
                          xscrollcommand=Scroll_x.set,
                          yscrollcommand=Scroll_y.set)
Student_Table.place(x=1,y=1,width=1130,height=587)
Scroll_x.pack(side=BOTTOM,fill=X)
Scroll_y.pack(side=LEFT,fill=Y)
Scroll_x.config(command=Student_Table.xview)
Scroll_y.config(command=Student_Table.yview)
Student_Table['show']='headings'
Student_Table.heading('address',text='Stusent Address')
Student_Table.heading('gender',text='Stusent Gender')
Student_Table.heading('certie',text='Student qualifications')
Student_Table.heading('phone',text='Stusent Phone')
Student_Table.heading('emil',text='Stusent Emil')
Student_Table.heading('name',text='Stusent Name')
Student_Table.heading('id',text='Stusent ID')
Student_Table.column('address',width=125)
Student_Table.column('gender',width=30)
Student_Table.column('certie',width=65)
Student_Table.column('phone',width=65)
Student_Table.column('emil',width=70)
Student_Table.column('name',width=100)
Student_Table.column('id',width=17)


#-----search manage-----
search_frame=Frame(root,bg='white')
search_frame.place(x=1,y=30,width=1134,height=50)

lbl_search=Label(search_frame,text='search for a student',bg='white')
lbl_search.place(x=10,y=12)

combo_search=ttk.Combobox(search_frame,justify='left')
combo_search['value']=('Id','Name','Email')
combo_search.place(x=120,y=12)

search_Entry=Entry(search_frame,justify='left',bd='2')
search_Entry.place(x=270,y=12)

se_btn=Button(search_frame,text='search',bg="darkred")
se_btn.place(x=400,y=10,width=100,height=25)
root.mainloop()
