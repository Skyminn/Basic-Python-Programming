from tkinter import *
from tkinter import messagebox
# 뒤로가기 함수
def func_exit():
    win.quit()
    win.destroy()

#전통 의상 함수
def clothes():
    window=Tk()
    window.geometry("1000x800")
    window.resizable(width=FALSE,height=FALSE)
    window.title("Korean Clothes")
    window.mainloop()

#전통 건축양식 함수
def architecture():
  
    def hanok_quiz():
        #함수 선언 부분
        def myFunc1():
            messagebox.showinfo("Japan architecture", "틀렸습니다. \n은색과 삼각형 모양의 건물을 통해 \n일본 전통 건축양식임을 확인할 수 있습니다.")
        def myFunc2():
            messagebox.showinfo("Korea architecture", "정답입니다. \n완만한 경사의 기와와 마루를 통해 \n한국 전통 건축양식임을 확인할 수 있습니다.")
        def myFunc3():
            messagebox.showinfo("China architecture", "틀렸습니다. \n건물의 대칭적인 구조를 통해 \n중국 전통 건축양식임을 확인할 수 있습니다.")

    
        window=Tk()
        window.geometry("1000x800")
        window.resizable(width=FALSE,height=FALSE)
        window.title("! 한옥 퀴즈 !")

        label1 = Label(window,text="\n! 한옥 퀴즈 시작 !",font=("tvN 즐거운이야기 Bold",40), anchor = CENTER)
        label1.pack()

        label2 = Label(window,text="다음 중 우리 전통 한옥을 골라줘!",font=("tvN 즐거운이야기 Bold",30), anchor = CENTER)
        label2.pack()
    

        #일본 건축양식
        photo1 = PhotoImage(file = "C:/history/hanok/일본.gif", master=window)
        button1 = Button(window, image = photo1, width=200, height=200)
        button1.configure(command = myFunc1)

        #한국 건축양식
        photo2 = PhotoImage(file = "C:/history/hanok/한국.gif", master=window)
        button2 = Button(window, image = photo2, width=200, height=200)
        button2.configure(command = myFunc2)
    
        #중국 건축양식
        photo3 = PhotoImage(file = "C:/history/hanok/중국.gif", master=window)
        button3 = Button(window, image = photo3, width=200, height=200)
        button3.configure(command = myFunc3)


        label1.pack()
        button1.pack(side = LEFT, padx = 60)
        button2.pack(side = LEFT, padx = 60)
        button3.pack(side = LEFT, padx = 60)



        # 메인화면으로 이동 버튼 (이미지 삽입)
        root = window
        photo4= PhotoImage(file=r'C:/history/hanok/return.gif',master=window)
        button4 = Button(window, image=photo4, command=root.destroy)
        button4.place(x=300,y=650)
        root.mainloop()
    
    def hanok_ex():
        window = Tk()
        window.geometry("1000x800")
        window.resizable(width=FALSE, height=FALSE)
        window.title("! 한옥에 대해 알아보자 !")

        label1 = Label(window,text="한옥에 대해 알아볼까요?", font=("tvN 즐거운이야기 Bold",40))
        label1.pack()

        # 한옥 알아보기
        photo1 = PhotoImage(file='C:/history/hanok/hanok1.gif',master=window)
        label2 = Label(window, image=photo1)
        label2.pack()

        label3 = Label(window,text="한옥의 구조", font=("나눔스퀘어",15))
        label3.pack()

        label4 = Label(window,text="\n한옥을 구성하는 가장 기본적인 기와 \n시원한 바람을 쐬며 휴식을 취할 수 있는 마루로 구성\n", font=("나눔스퀘어",10))
        label4.pack()

        # 퀴즈 시작 버튼 (이미지 삽입)
        photo2 = PhotoImage(file=r'C:/history/hanok/second_hanok.gif', master=window)
        button2 = Button(window, image=photo2)
        button2.config(command=hanok_quiz)
        button2.pack()


        # 메인화면으로 이동 버튼 (이미지 삽입)
        root = window
        photo3= PhotoImage(file=r'C:/history/hanok/return.gif',master=window)
        button3 = Button(window, image=photo3, command=root.destroy)
        button3.pack()
        root.mainloop()



    window=Tk()
    window.geometry("1000x900")
    window.resizable(width=FALSE,height=FALSE)
    window.title("Korean Architecture")

    label6 = Label(window,text="\n한옥에 대해 알아볼까요?\n \n",font=("tvN 즐거운이야기 Bold",40), anchor = SE)
    label6.pack()
    
    # 한복 main 사진
    photo7 = PhotoImage(file=r'C:/history/hanok/hanok2.gif',master=window)
    label7 = Label(window, image=photo7)
    label7.pack()
    # 한복 알아보기 버튼 (이미지 삽입)
    photo8 = PhotoImage(file=r'C:/history/hanok/first_hanok.gif',master=window)
    button6 = Button(window, image=photo8)
    button6.config(command=hanok_ex)
    button6.pack()


    # 퀴즈 시작 버튼 (이미지 삽입)
    photo9 = PhotoImage(file=r'C:/history/hanok/second_hanok.gif',master=window)
    button7 = Button(window, image=photo9)
    button7.config(command=hanok_quiz)
    button7.pack()



    # 메인화면으로 이동 버튼 (이미지 삽입)

    root = window
    photo10= PhotoImage(file=r'C:/history/hanok/return.gif',master=window)
    button8 = Button(window, image=photo10, command=root.destroy)
    button8.pack()



    root.mainloop()





#전통 음식 함수
def food():
    window=Tk()
    window.geometry("1000x800")
    window.resizable(width=FALSE,height=FALSE)
    window.title("Korean Food")
    window.mainloop()

#게임 설명 함수
def rule():
    window=Tk()
    window.geometry("500x500")
    window.resizable(width=FALSE,height=FALSE)
    window.title("게임 설명")
    window.mainloop()
    
#메인 창
window = Tk() 
window.geometry("1000x800") 
window.resizable(width=FALSE, height=FALSE)
window.title("Korean culture") 
window.option_add("*Font","맑은고딕 25")

#게임 종료 메뉴
mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "프로그램 종료", command = func_exit, font=("tvN 즐거운이야기 Medium",15))

#메인 창 내용
label1 = Label(window,text="바른 역사 길잡이",font=("tvN 즐거운이야기 Bold",40), anchor = SE)
label2 = Label(window, text="선 넘는 문화공정\n 우리 것을 바로 알아보자!")
label2.config(font=("tvN 즐거운이야기 Light",30))

#뒤로가기 버튼
btn1 = Button(window,text = "뒤로 가기", font=("tvN 즐거운이야기 Light",30))
btn1.config(command=quit)

#전통 의상
photo = PhotoImage(file='C:/history/전통의상.gif')
btn2 = Button(window,image=photo)
btn2.config(command=clothes)

#전통 건축양식
photo1 = PhotoImage(file='C:/history/건축양식.gif')
btn3 = Button(window,image=photo1)
btn3.config(command=architecture)

#전통 음식
photo2 = PhotoImage(file='C:/history/전통음식.gif')
btn4 = Button(window, image=photo2)
btn4.config(command=food)

#게임 설명
btn5 = Button(window,text = "게임 설명", font=("tvN 즐거운이야기 Medium",14))
btn5.config(command=rule)


label1.pack()
label2.pack()
btn5.pack(side=TOP)
btn1.place(x=850,y=700)
btn2.pack(side=LEFT,padx=40)
btn3.pack(side=LEFT,padx=40)
btn4.pack(side=LEFT,padx=40)

window.mainloop() 
