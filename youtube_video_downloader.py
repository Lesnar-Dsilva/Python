from tkinter import *
from tkinter.messagebox import showinfo;
from tkinter.ttk import Combobox;
from pytube import YouTube;
def download():
    yt = YouTube(e1.get());
    res = yt.streams.get_by_resolution(c1.get());
    showinfo("notification","Downloading");
    try:
        res.download();
    except:
        None;
    showinfo("notification","Downloaded");
win = Tk();
win.geometry("500x500");
l1 = Label(win,text="Enter link: ",font="arial 15 bold");
l1.grid(row=0,column=0)
e1 = Entry(win,width=60);
e1.grid(row=0,column=1)
l2 = Label(win,text="Resolution: ",font="arial 15 bold");
l2.grid(row=1,column=0);
c1 = Combobox(win,width=57,values=["360p","480p","720p"]);
c1.grid(row=1,column=1);
b1 = Button(win,text="Download",command=download);
b1.grid(row=2,column=1)
win.mainloop();
#1hr 30/05/2022