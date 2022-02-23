from tkinter import *
import q_hanbok

def know():
    win=Tk()
    win.geometry("1000x850")
    win.resizable(width=FALSE,height=FALSE)
    win.title("한복 알아보기")

    def func_exit():
        win.quit()
        win.destroy()

    # 한복 알아보기
    frame1=Frame(win)
    frame1.pack(side="left",fill="both",expand=True)

    frame2=Frame(win)
    frame2.pack(side="right",fill="both",expand=True)

    photo3 = PhotoImage(file=r'C:\history\hanbok\여자한복.gif', master=win)
    label2 = Label(frame1, image=photo3)
    label2.pack()


    label6 = Label(frame1,text="한복 저고리의 구조", font=("나눔스퀘어",15))
    label6.pack()

    label8 = Label(frame1,text="-----------------------------------", font=("나눔스퀘어",10))
    label8.pack()

    label7 = Label(frame1,text="한복을 구성하는 가장 기본적인 상의로,\n팔과 상체를 덮는 저고리는 부위에 따라 길,깃 등으로구성\n", font=("나눔스퀘어",10))
    label7.pack()

    label8 = Label(frame1,text="한복치마의 구조", font=("나눔스퀘어",15))
    label8.pack()

    label19 = Label(frame1,text="-----------------------------------", font=("나눔스퀘어",10))
    label19.pack()

    label9 = Label(frame1,text="여성의 한복을 구성하는 가장 기본적인 하의로,\n한복의 치마는 그 착장법이 뒤여밈으로 다른 아시아 국가들의 의상과 약간 다른 특징이 있음.\n", font=("나눔스퀘어",10))
    label9.pack()

    photo4 = PhotoImage(file=r'C:\history\hanbok\남자한복.gif', master=win)
    label3 = Label(frame1, image=photo4)
    label3.pack()

    label10 = Label(frame1,text="한복바지의 구조", font=("나눔스퀘어",15))
    label10.pack()

    label20 = Label(frame1,text="-----------------------------------", font=("나눔스퀘어",10))
    label20.pack()

    label11 = Label(frame1,text="남성의 한복을 구성하는 가장 기본적인 하의로,\n구성은 대칭하지만 앞뒤 중심이 사선이어서 움직이고 좌식생활에 편함\n", font=("나눔스퀘어",10))
    label11.pack()

    photo5 = PhotoImage(file=r'C:\history\hanbok\조끼.gif', master=win)
    label4 = Label(frame2, image=photo5)
    label4.pack()

    label14 = Label(frame2,text="한복조끼의 구조", font=("나눔스퀘어",15))
    label14.pack()

    label21 = Label(frame2,text="-----------------------------------", font=("나눔스퀘어",10))
    label21.pack()

    label15 = Label(frame2,text="안에 덧대어 입는 저고리인 덧저고리와 흡사한 개념을 통칭하여 쓰는 말로,\n조끼는 서양 복식에서 들어온 것으로 \n한복에 주머니가 없어 소지품을 보관하는 것이 어려웠던 점을 보완함\n", font=("나눔스퀘어",10))
    label15.pack()

    photo6 = PhotoImage(file=r'C:\history\hanbok\두루마기마고자.gif', master=win)
    label5 = Label(frame2, image=photo6)
    label5.pack()

    label12 = Label(frame2,text="한복포(도포)의 구조", font=("나눔스퀘어",15))
    label12.pack()

    label22 = Label(frame2,text="-----------------------------------", font=("나눔스퀘어",10))
    label22.pack()

    label13 = Label(frame2,text="외투의 일종으로,방한복의 역할을 하며 예를 갖추는 자리에 입음\n활동성을 중시한 옷이며 두루마기도 포의 일종\n포는 중국과 일본의 의복과 한국의 의복을 구분하는 기준이 되기도 함.\n", font=("나눔스퀘어",10))
    label13.pack()

    

    label16 = Label(frame2,text="그 외", font=("나눔스퀘어",15))
    label16.pack()

    label23 = Label(frame2,text="-----------------------------------", font=("나눔스퀘어",10))
    label23.pack()

    label17 = Label(frame2,text="한복 저고리의 고름 또는 치마허리에 차는 여성 장신구의 일종인 노리개,\n한복에 주머니가 없어 허리춤에 따로 차고다녔던 주머니,\n중인 이상과 기혼자남자만이 갓을 쓸 수 있었으며, \n상투를 보호하는 모자인 갓 등이 있음\n", font=("나눔스퀘어",10))
    label17.pack()

    #퀴즈 시작 버튼
    quiz_hanbok = PhotoImage(file=r'C:\history\hanbok\hanbok quiz.gif', master=win)
    hanbok_button2 = Button(win, image = quiz_hanbok)
    hanbok_button2.config(command=q_hanbok.quiz)
    hanbok_button2.place(x=303,y=665)
    
    #뒤로가기 버튼
    rebutton = PhotoImage(file=r'C:\history\return.gif', master=win)
    btn1 = Button(win,image = rebutton)
    btn1.config(command=func_exit)
    btn1.place(x=303,y=740)
    
    win.mainloop()



