from tkinter import *
import smtplib
root=Tk()
def send():
    #we will use try and catch to handle the error in the project
    try:
        username=temp_username.get()
        password=temp_password.get()
        to=temp_reciever.get()
        subject=temp_subject.get()
        body=temp_body.get()
        if username=="" or password=="" or subject=="" or to=="" or body=="":
            notif.config(text="All fields required", fg="red")
            return
        else:
            finalMessage='Subject:{}\n\n{}'.format(subject, body)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(username, to, finalMessage)
            notif.config(text='Email has been sent', fg='green')
    except:
        notif.config(text="Error sending email", fg="red")
def reset():
    usernameEntry.delete(0, 'end')
    passwordEntry.delete(0, 'end')
    recieverEntry.delete(0, 'end')
    subjectEntry.delete(0, 'end')
    bodyEntry.delete(0, 'end')

#root.geometry("544x600")
root.title("Custom Gmail App")
#Graphics
titleLabel=Label(root, text="Custom Email App", font=("calibri", 15), fg="red")
titleLabel.grid()
Label(root, text="Write your Email in the below form",font=("calibri", 11)).grid(row=1, sticky=W, padx=5)
Label(root, text="Email",font=("calibri", 11)).grid(row=2, sticky=W, padx=5)
Label(root, text="Password",font=("calibri", 11)).grid(row=3, sticky=W, padx=5)
Label(root, text="To",font=("calibri", 11)).grid(row=4, sticky=W, padx=5)
Label(root, text="Subject",font=("calibri", 11)).grid(row=5, sticky=W, padx=5)
Label(root, text="Body",font=("calibri", 11)).grid(row=6, sticky=W, padx=5)
notif=Label(root, text="",font=("calibri", 11))
notif.grid(row=7, sticky=S, padx=5)
#storage in the entry box
temp_username=StringVar()
temp_password=StringVar()
temp_reciever=StringVar()
temp_subject=StringVar()
temp_body=StringVar()
#entry box
usernameEntry=Entry(root,textvariable=temp_username)
usernameEntry.grid(row=2, column=0)
passwordEntry=Entry(root,show="*",textvariable=temp_password)
passwordEntry.grid(row=3, column=0)
recieverEntry=Entry(root,textvariable=temp_reciever)
recieverEntry.grid(row=4, column=0)
subjectEntry=Entry(root,textvariable=temp_subject)
subjectEntry.grid(row=5, column=0)
bodyEntry=Entry(root,textvariable=temp_body)
bodyEntry.grid(row=6, column=0)

#Buttons
Button(root,text="Send", command=send).grid(row=7, sticky=W, pady=15, padx=5)
Button(root,text="Reset", command=reset).grid(row=7, sticky=W, pady=45, padx=45)
root.mainloop()