#김치 퀴즈 페이지
from tkinter import *
from tkinter import messagebox

def f_quiz():
    win=Tk()
    win.geometry("1200x800")
    win.resizable(width=FALSE,height=FALSE)
    win.title("! 김치 퀴즈 ! ")

    def func_exit():
        win.quit()
        win.destroy()


# 오답시 출력 부분 함수
    def f1():
        messagebox.showinfo('틀렸습니다','파오차이는 중국의 채소 절임 식품으로 한국의 김치라고 오보되는 경우가 많으니 주의해야 합니다.')
    def f2():
        messagebox.showinfo('틀렸습니다','츠케모노는 채소를 절임한 일본의 저장 식품으로 한국의 김치와 달리 발효를 많이 시키지 않는 것이 특징입니다.')
# 정답시 출력 메세지
    def t1():
        messagebox.showinfo('정답입니다!','김치는 한국의 대표적인 채소 발효 식품으로, 우리나라 전통 음식입니다.') 


    label2 = Label(win,text="다음 중 우리 전통 음식인 김치를  골라줘!",font=("tvN 즐거운이야기 Bold",30), anchor = CENTER)
    label2.pack()



    #한국 김치
    photo = PhotoImage(file="C:\\history\김치\Kimchi2.gif",master=win)
    btn1 = Button(win,image=photo)
    btn1.config(command=t1)

    #중국 파오차이
    photo1 = PhotoImage(file='C:\\history\김치\pao_cai2.gif',master=win)
    btn2 = Button(win,image=photo1)
    btn2.config(command=f1)

    #일본 츠케모노
    photo2 = PhotoImage(file='C:\\history\김치\Tsukemono2.gif',master=win)
    btn3 = Button(win, image=photo2)
    btn3.config(command=f2)
        
    btn1.pack(side=LEFT,padx=10)
    btn2.pack(side=LEFT,padx=10)
    btn3.pack(side=LEFT,padx=10)


    #메인화면으로 이동
    photo6 = PhotoImage(file="C:\\history\\return.gif", master=win)
    button6 = Button(win, image=photo6)
    button6.config(command=func_exit)
    button6.place(x=400,y=650)

    win.mainloop()
