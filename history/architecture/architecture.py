from tkinter import *
from tkinter import messagebox

#함수 선언 부분
def myFunc1():
    messagebox.showinfo("Japan architecture", "틀렸습니다. \n은색과 삼각형 모양의 건물을 통해 \n일본 전통 건축양식임을 확인할 수 있습니다.")

def myFunc2():
    messagebox.showinfo("Korea architecture", "정답입니다. \n완만한 경사의 기와와 마루를 통해 \n한국 전통 건축양식임을 확인할 수 있습니다.")

def myFunc3():
    messagebox.showinfo("China architecture", "틀렸습니다. \n건물의 대칭적인 구조를 통해 \n중국 전통 건축양식임을 확인할 수 있습니다.")


#화면 크기 및 제목
window = Tk()
window.geometry("1000x800")
window.resizable(width=FALSE,height=FALSE)
window.title("Korean architeture")


#화면 글씨
label1 = Label(window, text="\n Q. 다음 중 한국 전통 건축 양식을 고르시오. ", font=("tvN 즐거운 이야기 Bold", 30), anchor = SE)

#일본 건축양식
photo1 = PhotoImage(file = r"C:\history\architecture\일본.gif")
button1 = Button(window, image = photo1, width=200, height=200)
button1.configure(command = myFunc1)

#한국 건축양식
photo2 = PhotoImage(file = r"C:\history\architecture\한국.gif")
button2 = Button(window, image = photo2, width=200, height=200)
button2.configure(command = myFunc2)

#중국 건축양식
photo3 = PhotoImage(file = r"C:\history\architecture\중국.gif")
button3 = Button(window, image = photo3, width=200, height=200)
button3.configure(command = myFunc3)

#뒤로가기 버튼
btn1 = Button(window,text = "뒤로 가기", font=("tvN 즐거운이야기 Light",10))
btn1.configure(command=quit)

label1.pack()
button1.pack(side = LEFT, padx = 60)
button2.pack(side = LEFT, padx = 60)
button3.pack(side = LEFT, padx = 60)
btn1.place(x=850,y=700)

window.mainloop()
