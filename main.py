# login
from tkinter import *
import tkinter

window = tkinter.Tk()
window.title("Quiz Login")
window.geometry("270x210")
window.configure(bg="dark slate blue")
def callback():
   username = user.get()
   password = passw.get()
   if username == 'quiz' and password == '12345':
       message.configure(text = "Logged in.")
       window.destroy()

   else:
       message.configure(text = "Username and password don't match the account \n under the name;\n \'" + username + "\'. \nPlease try again.")
title1 = tkinter.Label(window, text="Log in to play the Quiz\n", bg="dark slate blue")
usertitle = tkinter.Label(window, text="Username", bg="dark slate blue")
passtitle = tkinter.Label(window, text="Password", bg="dark slate blue")
message = tkinter.Label(window, bg="dark slate blue")
user = tkinter.Entry(window)
passw = tkinter.Entry(window, show='*')
go = tkinter.Button(window, text="LOG IN", command = callback, bg="gray")
title1.pack()
usertitle.pack()
user.pack()
passtitle.pack()
passw.pack()
go.pack()
message.pack()
window.mainloop()

# end
from tkinter import *
top=Tk()
top.title("              QUIZ")
top.geometry("270x210")
top.configure(bg="dark slate blue")
t=Label(top,text="THANK YOU FOR PLAYING THE QUIZ")
t.place()
t.pack()
top.mainloop()