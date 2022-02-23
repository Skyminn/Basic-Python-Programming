from tkinter import *
from tkinter import messagebox

import k_hanbok
import q_hanbok

import k_hanok
import q_hanok

import k_kimchi
import q_kimchi


# 뒤로가기 함수
def func_exit():
    win.quit()
    win.destroy()

#전통 의상 함수
def clothes():
    win=Tk()
    win.geometry("1000x800")
    win.resizable(width=FALSE,height=FALSE)
    win.title("Korean Clothes")

    #han_intro = Label(win,text="한복에 대해 알아볼까요?",font=("tvN 즐거운이야기 Bold",40), anchor = SE)
    #han_intro.pack()
    
    #한복 main 사진
    hanbok_mainphoto = PhotoImage(file=r'C:\history\hanbok\2.gif', master=win)
    hanbok_main = Label(win, image = hanbok_mainphoto)
    hanbok_main.pack()


    #한복 알아보기 버튼 (이미지 삽입)
    know_hanbok = PhotoImage(file=r'C:\history\hanbok\first hanbok.gif', master=win)
    hanbok_button = Button(win, image=know_hanbok)
    hanbok_button.config(command=k_hanbok.know)
    hanbok_button.pack()

    #퀴즈 시작 버튼 (이미지 삽입)
    quiz_hanbok = PhotoImage(file=r'C:\history\hanbok\hanbok quiz.gif', master=win)
    hanbok_button2 = Button(win, image = quiz_hanbok)
    hanbok_button2.config(command=q_hanbok.quiz)
    hanbok_button2.pack()

    # 메인화면으로 이동 버튼 (이미지 삽입)
    root = win
    photo4= PhotoImage(file=r'C:/history/hanok/return.gif',master=win)
    button4 = Button(win, image=photo4, command=root.destroy)
    button4.place(x=303,y=700)
    root.mainloop()
    
    win.mainloop()

#전통 건축양식 함수
def architecture():
    win=Tk()
    win.geometry("1000x800")
    win.resizable(width=FALSE,height=FALSE)
    win.title("Korean Architecture")

    hanok_intro = Label(win,text="한옥에 대해 알아볼까요?",font=("tvN 즐거운이야기 Bold",40), anchor = SE)
    hanok_intro.pack()
    
    #한옥 main 사진
    hanok_mainphoto = PhotoImage(file='C:/history/hanok/hanok2.gif', master=win)
    hanok_main = Label(win, image = hanok_mainphoto)
    hanok_main.pack()


    #한옥 알아보기 버튼 (이미지 삽입)
    know_hanok = PhotoImage(file='C:/history/hanok/first_hanok.gif', master=win)
    hanok_button = Button(win, image=know_hanok)
    hanok_button.config(command=k_hanok.know)
    hanok_button.pack()

    #퀴즈 시작 버튼 (이미지 삽입)
    quiz_hanok = PhotoImage(file='C:/history/hanok/second_hanok.gif', master=win)
    hanok_button2 = Button(win, image = quiz_hanok)
    hanok_button2.config(command=q_hanok.quiz)
    hanok_button2.pack()

    # 메인화면으로 이동 버튼 (이미지 삽입)
    root = win
    photo4= PhotoImage(file='C:/history/hanok/return.gif',master=win)
    button4 = Button(win, image=photo4, command=root.destroy)
    button4.place(x=303,y=620)
    root.mainloop()
    
    win.mainloop()

 
#전통 음식 함수
def food():
    win=Tk()
    win.geometry("1000x900")
    win.resizable(width=FALSE, height=FALSE)
    win.title("Korean Food")

    label1 = Label(win,text="김치에 대해 알아볼까요?",font=("tvN 즐거운이야기 Bold",40))
    label1.pack(pady=50)


    #김치 main 사진
    photo1 = PhotoImage(file = "C:\\history\김치\kimchi introduce1.gif",master=win)
    label3 = Label(win, image = photo1)
    label3.pack(pady=50)


    #김치 알아보기 버튼
    photo2 = PhotoImage(file="C:\\history\김치\lets know kimchi.gif",master=win)
    button1 = Button(win, image=photo2)
    button1.config(command=k_kimchi.know)
    button1.pack(pady=10)


    #퀴즈 시작 버튼
    photo3 = PhotoImage(file="C:\\history\김치\kimchi quiz.gif",master=win)
    button2 = Button(win, image=photo3)
    button2.config(command=q_kimchi.f_quiz)
    button2.pack(pady=10)


    #메인화면으로 이동 버튼
    root = win
    photo4 = PhotoImage(file="C:\\history\\return.gif",master=win)
    button3 = Button(win, image=photo4, command=root.destroy)
    button3.pack(pady=10)

    root.mainloop()   
        
    
#게임 설명 함수
def rule():
    win=Tk()
    win.geometry("500x300")
    win.resizable(width=FALSE,height=FALSE)
    win.title("게임 설명")

    label1 = Label(win, text="게임 취지", font=("나눔스퀘어",15))
    label1.pack()

    label2 = Label(win, text="-----------------------------------", font=("나눔스퀘어",10))
    label2.pack()

    label3 = Label(win, text="한, 중, 일의 비슷하면서도 다른\n건축, 음식, 의복 양식을 구분해 우리 전통 문화를 알아보자!\n", font=("나눔스퀘어",10))
    label3.pack()

    label4 = Label(win, text="각종 매체에서 각색된 역사적 사실과\n와전되어 전해지고 있는 우리나라 문화에 대한 혼동을 방지하기 위해\n어린 학생들을 대상으로 올바른 우리 문화를 교육하기 위한 퀴즈게임이다.\n", font=("나눔스퀘어",10))
    label4.pack()

    label7 = Label(win, text="-----------------------------------", font=("나눔스퀘어",10))
    label7.pack()
    
    label5 = Label(win, text="주의 사항", font=("나눔스퀘어",15))
    label5.pack()


    label6 = Label(win, text="퀴즈의 경우 메시지 박스가 뜨며 창이 뒤로 가는 경우가 있으니\n창을 클릭해 앞으로 가져오면 퀴즈를 계속 이어나갈 수 있습니다.\n", font=("나눔스퀘어",10))
    label6.pack()

    
    win.mainloop()

#메인 창
win = Tk() 
win.geometry("1000x800") 
win.resizable(width=FALSE, height=FALSE)
win.title("Korean culture") 
win.option_add("*Font","맑은고딕 25")

#게임 종료 메뉴
mainMenu = Menu(win)
win.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "프로그램 종료", command = func_exit, font=("tvN 즐거운이야기 Medium",15))

#메인 창 내용
label1 = Label(win,text="바른 역사 길잡이",font=("tvN 즐거운이야기 Bold",40), anchor = SE)
label2 = Label(win, text="선 넘는 문화공정\n 우리 것을 바로 알아보자!!")
label2.config(font=("tvN 즐거운이야기 Light",30))

#뒤로가기 버튼 (이미지 삽입)  
rebutton = PhotoImage(file=r'C:\history\end.gif', master=win)
btn1 = Button(win,image = rebutton)
btn1.config(command=quit)

#전통 의상
photo = PhotoImage(file='C:\history\전통의상.gif')
btn2 = Button(win,image=photo)
btn2.config(command=clothes)

#전통 건축양식
photo1 = PhotoImage(file='C:\history\건축양식.gif')
btn3 = Button(win,image=photo1)
btn3.config(command=architecture)

#전통 음식
photo2 = PhotoImage(file='C:\history\전통음식.gif')
btn4 = Button(win, image=photo2)
btn4.config(command=food)

#게임 설명
btn5 = Button(win,text = "게임 설명", font=("tvN 즐거운이야기 Bold",20))
btn5.config(command=rule)


label1.pack()
label2.pack()
btn5.pack(side=TOP)
btn1.place(x=303,y=700)
btn2.pack(side=LEFT,padx=50)
btn3.pack(side=LEFT,padx=50)
btn4.pack(side=LEFT,padx=50)

win.mainloop() 
