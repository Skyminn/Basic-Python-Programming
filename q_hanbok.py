'''한복 퀴즈 페이지'''
from tkinter import *       # = import tkinter
from tkinter import messagebox # 메세지박스 안에 있는 문자를 보여주는 팝업창이 뜸

def quiz():
    win=Tk()
    win.geometry("1000x800")
    win.resizable(width=FALSE,height=FALSE)
    win.title("! 한복 퀴즈 !")

    def func_exit():
        win.quit()
        win.destroy()

# 오답시 출력 메세지
    def f1():
        messagebox.showinfo('틀렸습니다','해당 의복은 중국의 한푸 입니다!\n우리 전통 한복에는 저고리의 고름이 앞쪽에 있습니다!')

    def f2():
        messagebox.showinfo('틀렸습니다','해당 의복은 중국의 치파오 입니다!\n우리 전통 한복은 저고리와 치마, 두 부분으로 나누어 진 게 특징이에요!')

# 정답시 출력 메세지
    def t1():
        messagebox.showinfo('정답입니다!','우리 전통 한복은 옷고름이 앞쪽에 있고,\n저고리와 치마로 나뉘고, 노리개를 단 것이 특징이에요!')

    hanbok_quiz = Label(win,text="다음 중 우리 전통 한복을 골라줘!",font=("tvN 즐거운이야기 Bold",30), anchor = CENTER)
    hanbok_quiz.pack()

    # 한복 퀴즈 - 사진 1 (한푸)
    hquiz_photo = PhotoImage(file=r'C:\history\hanbok\hanfu.gif', master = win)
    hanbokquiz_button1 = Button(win, image=hquiz_photo, command=f1)
    hanbokquiz_button1.pack(side=LEFT, padx=20)

    # 한복 퀴즈 - 사진 2 (한복)
    hquiz_photo2 = PhotoImage(file=r'C:\history\hanbok\h2.gif', master = win)
    hanbokquiz_button2 = Button(win, image=hquiz_photo2, command=t1)
    hanbokquiz_button2.pack(side=LEFT, padx=20)

    # 한복 퀴즈 - 사진 3 (치파오)
    hquiz_photo3 = PhotoImage(file=r'C:\history\hanbok\qipao.gif', master = win)
    hanbokquiz_button3 = Button(win, image=hquiz_photo3, command=f2)
    hanbokquiz_button3.pack(side=LEFT, padx=20)

    #뒤로가기 버튼
    rebutton = PhotoImage(file=r'C:\history\return.gif', master=win)
    btn1 = Button(win,image = rebutton)
    btn1.config(command=func_exit)
    btn1.place(x=303,y=700)

    win.mainloop()


