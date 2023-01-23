import tkinter as tk;
calc= "";
def add(s):
    global calc;
    calc += str(s)
    txt.delete(1.0,"end");
    txt.insert(1.0,calc);
def evl():
    global calc;
    try:
        calc = str(eval(calc));
        txt.delete(1.0,"end");
        txt.insert(1.0,calc);
    except:
        clear();
        txt.insert(1.0,"Error");
def clear():
    global calc;
    calc = "";
    txt.delete(1.0,"end");
win = tk.Tk();
win.geometry("300x275");
txt = tk.Text(win,height=2,width=16,font=("Arial",24));
txt.grid(columnspan=5);
btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_0 = tk.Button(win,text="1",command=lambda: add(1),width=5,font=("Arial",14)),tk.Button(win,text="2",command=lambda: add(2),width=5,font=("Arial",14)),tk.Button(win,text="3",command=lambda: add(3),width=5,font=("Arial",14)),tk.Button(win,text="4",command=lambda: add(4),width=5,font=("Arial",14)),tk.Button(win,text="5",command=lambda: add(5),width=5,font=("Arial",14)),tk.Button(win,text="6",command=lambda: add(6),width=5,font=("Arial",14)),tk.Button(win,text="7",command=lambda: add(7),width=5,font=("Arial",14)),tk.Button(win,text="8",command=lambda: add(8),width=5,font=("Arial",14)),tk.Button(win,text="9",command=lambda: add(9),width=5,font=("Arial",14)),tk.Button(win,text="0",command=lambda: add(0),width=5,font=("Arial",14));
btn_1.grid(row=2,column=1);
btn_2.grid(row=2,column=2);
btn_3.grid(row=2,column=3);
btn_4.grid(row=3,column=1);
btn_5.grid(row=3,column=2);
btn_6.grid(row=3,column=3);
btn_7.grid(row=4,column=1);
btn_8.grid(row=4,column=2);
btn_9.grid(row=4,column=3);
btn_0.grid(row=5,column=2);
btn_plus,btn_minus,btn_div,btn_multiply,btn_open,btn_close = tk.Button(win,text="+",command=lambda: add("+"),width=5,font=("Arial",14)),tk.Button(win,text="-",command=lambda: add("-"),width=5,font=("Arial",14)),tk.Button(win,text="/",command=lambda: add("/"),width=5,font=("Arial",14)),tk.Button(win,text="*",command=lambda: add("*"),width=5,font=("Arial",14)),tk.Button(win,text="(",command=lambda: add("("),width=5,font=("Arial",14)),tk.Button(win,text=")",command=lambda: add(")"),width=5,font=("Arial",14));
btn_plus.grid(row=2,column=4);
btn_minus.grid(row=3,column=4);
btn_div.grid(row=4,column=4);
btn_multiply.grid(row=5,column=4);
btn_open.grid(row=5,column=1);
btn_close.grid(row=5,column=3);
btn_clear,btn_equals = tk.Button(win,text="C",command=clear,width=11,font=("Arial",14)),tk.Button(win,text="=",command=evl,width=11,font=("Arial",14));
btn_clear.grid(row=6,column=1,columnspan=2);
btn_equals.grid(row=6,column=3,columnspan=2);
win.mainloop();
#1hr 26/05/2022