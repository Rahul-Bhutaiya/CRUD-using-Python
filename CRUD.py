from tkinter import *
from mysql.connector import connect
from tkinter import messagebox


def register_user(cur_obj,con_obj,main_layout,insert_ent1,insert_ent2,insert_ent3):
    cur_obj.execute('insert into user (name,email,pwd) values (%s,%s,%s)',(insert_ent1.get(),insert_ent2.get(),insert_ent3.get()))
    messagebox.showinfo('Information','User Registered Succeesfully')
    con_obj.commit()
    cur_obj.close()
    con_obj.close()
    main_layout.destroy()
    user_data()

def delete_user(user_id,cur_obj,con_obj,main_layout):
    cur_obj.execute(f'delete from user where id={user_id}')
    con_obj.commit()
    cur_obj.close()
    con_obj.close()
    main_layout.destroy()
    user_data()

def update_query(insert_ent1,insert_ent2,insert_ent3,u_id,cur_obj,con_obj,main_layout):
    cur_obj.execute('update user set name=%s,email=%s,pwd=%s where id=%s',(insert_ent1.get(),insert_ent2.get(),insert_ent3.get(),u_id))
    con_obj.commit()
    cur_obj.close()
    con_obj.close()
    main_layout.destroy()
    user_data()

def update_user(cur_obj,con_obj,main_layout,insert_ent1,insert_ent2,insert_ent3,register_btn,u_id,u_name,u_email,u_pwd):
    insert_ent1.delete(0,END)
    insert_ent2.delete(0,END)
    insert_ent3.delete(0,END)

    insert_ent1.insert(0,u_name)
    insert_ent2.insert(0,u_email)
    insert_ent3.config(show='')
    insert_ent3.insert(0,u_pwd)
    register_btn.config(text='Update',command=lambda :update_query(insert_ent1,insert_ent2,insert_ent3,u_id,cur_obj,con_obj,main_layout))

def user_data():
    main_layout=Tk()
    main_layout.title('Update User Data')
    main_layout.state('zoomed')
    main_layout.iconbitmap('images\icons8-apple-logo-16 (1).ico')


    f1=Frame(main_layout,height=300,width=600,bg='#7676ee')
    f1.grid(row=4,column=0,columnspan=2)

    con_obj=connect(host='localhost',user='root',password='',database='python_database01')
    cur_obj=con_obj.cursor()
    cur_obj.execute('select * from user')
    rows=cur_obj.fetchall()

    insert_lbl1=Label(main_layout,text='Name')
    insert_lbl1.grid(row=0,column=0)
    
    insert_ent1=Entry(main_layout)
    insert_ent1.grid(row=0,column=1)
    
    insert_lbl2=Label(main_layout,text='Email')
    insert_lbl2.grid(row=1,column=0)

    insert_ent2=Entry(main_layout)
    insert_ent2.grid(row=1,column=1)

    insert_lbl3=Label(main_layout,text='Password')
    insert_lbl3.grid(row=2,column=0)

    insert_ent3=Entry(main_layout,show='*')
    insert_ent3.grid(row=2,column=1)

    register_btn=Button(main_layout,text='Register',command=lambda:register_user(cur_obj,con_obj,main_layout,insert_ent1,insert_ent2,insert_ent3))
    register_btn.grid(row=3,column=0,columnspan=2,pady=20)

    row_count=0
    for row in rows:
        for column_count in range(len(row)):
            lbl1=Label(f1,text=row[column_count],bg='#7676ee')
            lbl1.grid(row=row_count,column=column_count)

        btn1=Button(f1,text='Delete',bg='#7676ee',command=lambda user_id=row[0]:delete_user(user_id,cur_obj,con_obj,main_layout))
        btn1.grid(row=row_count,column=column_count+1)
        btn2=Button(f1,text='Update',bg='#7676ee',command=lambda u_id=row[0],u_name=row[1],u_email=row[2],u_pwd=row[3]:update_user(cur_obj,con_obj,main_layout,insert_ent1,insert_ent2,insert_ent3,register_btn,u_id,u_name,u_email,u_pwd))
        btn2.grid(row=row_count,column=column_count+2)
        row_count+=1

    main_layout.mainloop()
user_data()