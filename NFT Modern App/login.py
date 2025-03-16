from tkinter import *

root1 = Tk()
root1.geometry('468x493')
root1.overrideredirect(1)
root1.wm_attributes("-transparentcolor", "grey")

def username_text_hide(e):
    hover_username.config(text='')

def password_text_hide(e):
    hover_password.config(text='')

def move_app(e):
    root1.geometry(f'+{e.x_root}+{e.y_root}')

# Load and place image as background
frame_photo = PhotoImage(file='login.png')
frame_label = Label(root1, border=0, bg='grey', image=frame_photo)
frame_label.pack(fill="both", expand=True)

#text entry for username and password
username_entry = Entry(root1,border=0,width=35,font=('bold',12),background='#3E3E3E',foreground='white',insertbackground='white')
username_entry.place(x=78,y=150)

password_entry = Entry(root1,border=0,width=35,font=('bold',12),background='#3E3E3E',foreground='white',insertbackground='white')
password_entry.place(x=78,y=210)

#login button
login_btn = PhotoImage(file='loginbtn.png')

login_lab = Label(root1,border=0,background='#202441',image=login_btn,cursor='hand2')
login_lab.place(x=70,y=290)

#create new account button
create_btn = PhotoImage(file='create.png')

create_lab = Label(root1,border=0,background='#202441',image=create_btn,cursor='hand2')
create_lab.place(x=70,y=390)

#forgot password button
forgot_btn = PhotoImage(file='forgot.png')

forgot_lab = Label(root1,border=0,image=forgot_btn,background='#202441',cursor='hand2')
forgot_lab.place(x=80,y=255)

#hover username
hover_username = Label(root1,text='username',background='#3E3E3E',foreground='#CEC3C3',font=('arial',12))
hover_username.place(x=73,y=148)

#hover password
hover_password = Label(root1,text='password',background='#3E3E3E',foreground='#CEC3C3',font=('arial',12))
hover_password.place(x=73,y=208)

# Make the frame draggable
frame_label.bind("<B1-Motion>", move_app)

#more faster remove label
username_entry.bind('<Enter>',username_text_hide)
password_entry.bind('<Enter>',password_text_hide)

root1.mainloop()
