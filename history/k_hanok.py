from tkinter import *
import q_hanok

def know():
    win=Tk()
    win.geometry("1000x850")
    win.resizable(width=FALSE,height=FALSE)
    win.title("한옥 알아보기")

    def func_exit():
        win.quit()
        win.destroy()

    # 한옥 알아보기
    photo3 = PhotoImage(file='C:/history/hanok/hanok1.gif', master=win)
    label2 = Label(win, image=photo3)
    label2.pack(side=LEFT)

    label6 = Label(win,text="한옥의 구조", font=("나눔스퀘어",15))
    label6.pack()

    label7 = Label(win,text="-----------------------------------", font=("나눔스퀘어",10))
    label7.pack()

    label8 = Label(win,text="\n한옥을 구성하는 가장 기본적인 기와 \n시원한 바람을 쐬며 휴식을 취할 수 있는 마루로 구성\n", font=("나눔스퀘어",10))
    label8.pack()

    label9= Label(win,text="\n<자연과 조화> \n \n우리 조상들은 자연과의 조화를 최고의 이상으로 삼았으며\n따라서 이를 반영하여 자연에 순응하는 구조를 취함\n",font=("나눔스퀘어",10))
    label9.pack()

    label10= Label(win,text="\n<온돌의 따스함> \n \n한옥의 난방 방식인 온돌은 공기가 아닌 바닥을 데우기 때문에\n실내환경이 쾌적하게 유지됨\n",font=("나눔스퀘어",10))
    label10.pack()

    label11= Label(win,text="\n<열려있는 마루> \n \n마루는 더위에 적응하기 위하여 발달된 한옥의 건축요소로\n바닥면의 습기가 닿지 않고 바람을 통하게 함으로써 쾌적함\n",font=("나눔스퀘어",10))
    label11.pack()

    label12= Label(win,text="\n<친환경적인 건축> \n \n한옥에는 현대 건축에서 생기는 공해가 거의 없음\n따라서 한옥에 쓰인 재료들은 대부분 재활용이 가능함\n또한 아파트 등 다른 재료의 건물에 비해 독성이 없어서\n인간의 몸에 해롭지 않음\n",font=("나눔스퀘어",10))
    label12.pack()

    label13= Label(win,text="\n<곡선의 아름다움> \n \n자연스럽게 끝을 올린 한옥의 곡선은\n중국과 일본의 전통건축에서 볼 수 있는\n직선적인 지붕 형태에 비해 곡선의 아름다움을 지킴\n",font=("나눔스퀘어",10))
    label13.pack()



    #퀴즈 시작 버튼
    quiz_hanok = PhotoImage(file='C:/history/hanok/second_hanok.gif', master=win)
    hanok_button2 = Button(win, image = quiz_hanok)
    hanok_button2.config(command=q_hanok.quiz)
    hanok_button2.place(x=303,y=665)
    
    #뒤로가기 버튼
    rebutton = PhotoImage(file='C:/history/hanok/return.gif', master=win)
    btn1 = Button(win,image = rebutton)
    btn1.config(command=func_exit)
    btn1.place(x=303,y=740)
    
    win.mainloop()
