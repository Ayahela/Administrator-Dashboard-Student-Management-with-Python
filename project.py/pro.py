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
import pymysql
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
#-----variables------

id_var=StringVar()
name_var=StringVar()
email_var=StringVar()
phone_var=StringVar()
certificate_var=StringVar()
gender_var=StringVar()
address_var=StringVar()
se_var=StringVar()
dell_var=StringVar()
qulification_var=StringVar()
#----------------------------

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
txt_ID=Entry(Manage_Frame,bd='2',textvariable=id_var)    #to make border
txt_ID.grid(row=1,column=1, padx=7, pady=5)
#Name
lbl_name=Label(Manage_Frame,text='Name',bg='white')
lbl_name.grid(row=2,column=0, padx=7, pady=5)
txt_name=Entry(Manage_Frame,bd='2',textvariable=name_var)    #to make border
txt_name.grid(row=2,column=1, padx=7, pady=5)
#Email
lbl_Email=Label(Manage_Frame,text='Email',bg='white')
lbl_Email.grid(row=3,column=0, padx=7, pady=5)
txt_Email=Entry(Manage_Frame,bd='2',textvariable=email_var)
txt_Email.grid(row=3,column=1, padx=7, pady=5)
###phone
lbl_Phone=Label(Manage_Frame,text='Phone',bg='white')
lbl_Phone.grid(row=4,column=0, padx=7, pady=5)
txt_Phone=Entry(Manage_Frame,bd='2',textvariable=phone_var)
txt_Phone.grid(row=4,column=1, padx=7, pady=5)
####certificate
lbl_Certificate=Label(Manage_Frame,text='Certificate',bg='white')
lbl_Certificate.grid(row=5,column=0, padx=1, pady=5)
txt_Certificate=Entry(Manage_Frame,bd='2',textvariable=certificate_var)
txt_Certificate.grid(row=5,column=1, padx=1, pady=5)
#Gender
lbl_Gender=Label(Manage_Frame,text='Gender',bg='white')
lbl_Gender.grid(row=6,column=0, padx=1, pady=5)
combo_Gender = ttk.Combobox(Manage_Frame,textvariable=gender_var)
combo_Gender['values'] = ['Male', 'Female']
combo_Gender.grid(row=6,column=1, padx=1, pady=5)

#address
lbl_Address=Label(Manage_Frame,text='Address',bg='white')
lbl_Address.grid(row=7,column=0, padx=1, pady=5)
txt_Address=Entry(Manage_Frame,bd='2',textvariable=address_var)
txt_Address.grid(row=7,column=1, padx=1, pady=5)
#delete
lbl_delete=Label(Manage_Frame,fg='red',bg='white',text='delete student')
lbl_delete.grid(row=8, column=0, padx=7, pady=5)

delete_Entry=Entry(Manage_Frame,bd=2,justify='center', textvariable=id_var)
delete_Entry.grid(row=8, column=1, padx=7, pady=5)


########################################
#-------add+con----------------
#fetch_all()
def add_student():
    con = pymysql.connect(host='localhost',user='root', password='', database='stud2')
    cur=con.cursor()
    cur.execute("insert into student2 values(%s,%s,%s,%s,%s,%s,%s)",(
                                                        id_var.get(),
                                                        name_var.get(),
                                                        phone_var.get(),
                                                        email_var.get(),
                                                        certificate_var.get(),

                                                        gender_var.get(),
                                                        address_var.get()
                                                         ))
    con.commit()
    fetch_all()
    con.close()
#-----------Delete function---------    
def delete():
    con =pymysql.connect(host='localhost',user='root',password='',database='stud2') 
    cur=con.cursor()   
    cur.execute('delete from student2 where id=%s',id_var.get())
    con.commit()
    fetch_all()
    con.close()

##############################
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

add_btn = Button(btn_frame, text="Add Student", bg="darkred", fg="white",command=add_student)
add_btn.place(x=33, y=30, width=150, height=30)

del_btn = Button(btn_frame, text="Delete Student", bg="darkred", fg="white",command=delete)
del_btn.place(x=33, y=65, width=150, height=30)

update_btn = Button(btn_frame, text="Update Data", bg="darkred", fg="white")
update_btn.place(x=33, y=100, width=150, height=30)

clear_btn = Button(btn_frame, text="Clear Fields", bg="darkred", fg="white")
clear_btn.place(x=33, y=135, width=150, height=30)

about_btn = Button(btn_frame, text="About Us", bg="darkred", fg="white")
about_btn.place(x=33, y=170, width=150, height=30)

exit_btn = Button(btn_frame, text="Exit", bg="darkred", fg="white")
exit_btn.place(x=33, y=205, width=150, height=30)
# <<<<<<< HEAD
#show dietals
Dietals_Frame=Frame(root,bg='#F2F4F4')
Dietals_Frame.place(x=1,y=82,width=1134,height=605)
#scroll creation
Scroll_x=Scrollbar(Dietals_Frame,orient=HORIZONTAL)
Scroll_y=Scrollbar(Dietals_Frame,orient=VERTICAL)
#treeview
Student_Table=ttk.Treeview(Dietals_Frame,
columns=('id','name','phone','email','certie','gender','address'),
xscrollcommand=Scroll_x.set,
yscrollcommand=Scroll_y.set)
Student_Table.place(x=1,y=1,width=1130,height=587)
Scroll_x.pack(side=BOTTOM,fill=X)
Scroll_y.pack(side=LEFT,fill=Y)
Scroll_x.config(command=Student_Table.xview)
Scroll_y.config(command=Student_Table.yview)
Student_Table['show']='headings'
Student_Table.heading('id',text='Student id')
Student_Table.heading('name',text='Student Name')
Student_Table.heading('phone',text='Student Phone')
Student_Table.heading('email',text='Student Email')

Student_Table.heading('certie',text='Student qualifications')
Student_Table.heading('gender',text='Student Gender')
Student_Table.heading('address',text='Student Address')
Student_Table.column('id',width=20)
Student_Table.column('gender',width=20)
Student_Table.column('certie',width=50)
Student_Table.column('phone',width=65)
Student_Table.column('email',width=80)
Student_Table.column('name',width=100) 
Student_Table.column('address',width=60)

#---------fetch function--------------
def fetch_all():
    con =pymysql.connect(host='localhost',user='root',password='',database='stud2') 
    cur=con.cursor()
    cur.execute('select * from student2')
    rows=cur.fetchall()
    if len (rows)!= 0:
      Student_Table.delete(*Student_Table.get_children())
      for row in rows:
        Student_Table.insert("",END,value=row)
      con.commit()  
    con.close() 

########################################
#-----------calling fetch function--------
fetch_all()
#######################################

#-----search manage-----
search_frame=Frame(root,bg='white')
search_frame.place(x=1,y=30,width=1134,height=50)

lbl_search=Label(search_frame,text='search for a student',bg='white')
lbl_search.place(x=10,y=12)

combo_search=ttk.Combobox(search_frame,justify='left')
combo_search['value']=('Id','Name','Email')
combo_search.place(x=120,y=12)

search_Entry=Entry(search_frame,justify='left',bd='2',textvariable=se_var)
search_Entry.place(x=270,y=12)
se_btn=Button(search_frame,text='search',bg="darkred", fg="white")
se_btn.place(x=400,y=10,width=100,height=25)
root.mainloop()
