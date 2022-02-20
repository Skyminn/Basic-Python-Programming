'''한옥 퀴즈 페이지'''
from tkinter import *       # = import tkinter
from tkinter import messagebox # 메세지박스 안에 있는 문자를 보여주는 팝업창이 뜸

def quiz():
    #함수 선언 부분
    def myFunc1():
        messagebox.showinfo("Japan architecture", "틀렸습니다. \n은색과 삼각형 모양의 건물을 통해 \n일본 전통 건축양식임을 확인할 수 있습니다.")

    def myFunc2():
        messagebox.showinfo("Korea architecture", "정답입니다. \n완만한 경사의 기와와 마루를 통해 \n한국 전통 건축양식임을 확인할 수 있습니다.")

    def myFunc3():
        messagebox.showinfo("China architecture", "틀렸습니다. \n건물의 대칭적인 구조를 통해 \n중국 전통 건축양식임을 확인할 수 있습니다.")

    
    win=Tk()
    win.geometry("1000x800")
    win.resizable(width=FALSE,height=FALSE)
    win.title("! 한옥 퀴즈 !")

    label1 = Label(win,text="\n! 한옥 퀴즈 시작 !",font=("tvN 즐거운이야기 Bold",40), anchor = CENTER)
    label1.pack()

    label2 = Label(win,text="다음 중 우리 전통 한옥을 골라줘!",font=("tvN 즐거운이야기 Bold",30), anchor = CENTER)
    label2.pack()
    

    #일본 건축양식
    photo1 = PhotoImage(file = "C:/history/hanok/일본.gif", master=win)
    button1 = Button(win, image = photo1, width=200, height=200)
    button1.configure(command = myFunc1)

    #한국 건축양식
    photo2 = PhotoImage(file = "C:/history/hanok/한국.gif", master=win)
    button2 = Button(win, image = photo2, width=200, height=200)
    button2.configure(command = myFunc2)
    
    #중국 건축양식
    photo3 = PhotoImage(file = "C:/history/hanok/중국.gif", master=win)
    button3 = Button(win, image = photo3, width=200, height=200)
    button3.configure(command = myFunc3)


    label1.pack()
    button1.pack(side = LEFT, padx = 60)
    button2.pack(side = LEFT, padx = 60)
    button3.pack(side = LEFT, padx = 60)



    # 메인화면으로 이동 버튼 (이미지 삽입)
    root = win
    photo4= PhotoImage(file=r'C:/history/hanok/return.gif',master=win)
    button4 = Button(win, image=photo4, command=root.destroy)
    button4.place(x=300,y=650)
    root.mainloop()
    
