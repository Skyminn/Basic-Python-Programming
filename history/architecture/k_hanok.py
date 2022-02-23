from tkinter import *
import q_hanok

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

