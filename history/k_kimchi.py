from tkinter import *
import q_kimchi

def know():
    win=Tk()
    win.geometry("1000x800")
    win.resizable(width=FALSE,height=FALSE)
    win.title("김치 알아보기")

    def func_exit():
        win.quit()
        win.destroy()

    # 김치 알아보기
    photo10 = PhotoImage(file = "C:\\history\김치\kimchi introduce1.gif",master=win)
    label30 = Label(win, image = photo10)
    label30.pack()


    label10 = Label(win,text = "김치는 무, 배추, 오이 등을 주재료로 만드는 우리나라의 발효 식품이다.", font=("tvN 즐거운이야기 Bold",30))
    label20 = Label(win,text = "주로 절인 배추에 고춧가루, 마늘, 간 무, 액젓, 설탕 등을 넣어 만든 양념을 고루 발라 담근다.", font=("tvN 즐거운이야기 Bold",20))
    label10.pack(anchor = CENTER, pady=30)
    label20.pack(pady=20)


    #퀴즈 시작 버튼
    photo5 = PhotoImage(file="C:\\history\김치\kimchi quiz.gif", master=win)
    button5 = Button(win, image=photo5)
    button5.config(command=q_kimchi.f_quiz)
    button5.pack()


    #메인화면으로 이동 버튼
    photo7 = PhotoImage(file="C:\\history\\return.gif", master=win)
    button7 = Button(win, image=photo7)
    button7.config(command=func_exit)
    button7.pack()
    
    win.mainloop()
    
