from tkinter import * #파이썬 기본 GUI 제작도구인 tkinder 모든 기능 사용 
from tkinter import messagebox

def func_open():
    messagebox.showinfo("메뉴 선택" , "열기 메뉴를 선택함")

def func_exit() :
    window.quit
    window.destroy()

window = Tk() #기본이 되는 윈도우창 생성

mainMenu = Menu(window) #생성한 바탕 창에 부착할 메인메뉴 객체를 만들겠다.
window.config(menu=mainMenu) #창의 속성을 변경하여, 방금 만든 mainmenu를 창에 넣겠다. 

fileMenu = Menu(mainMenu) #메인메뉴 아래 들어갈 하위메뉴를 생설할것이다.
mainMenu.add_cascade(label="파일", menu=fileMenu) #메인 메뉴바에 파일이라는 이름의 메뉴를 넣을것이다.
fileMenu.add_command(label="열기" , command=func_open) #하위메뉴안에 열기라는 클릭가능한 메뉴 삽입
fileMenu.add_separator() #구분선을 추가
fileMenu.add_command(label="종료" , command=func_exit) # 


viewMenu = Menu(mainMenu)
mainMenu.add_cascade(label="보기", menu=viewMenu)
viewMenu.add_command(label="축소")
viewMenu.add_separator()
viewMenu.add_command(label="확대")
homeMenu = Menu(mainMenu)

mainMenu.add_cascade(label="홈", menu=homeMenu)
homeMenu.add_command(label="저장")
homeMenu.add_separator()
homeMenu.add_command(label="선택" )
homeMenu.add_separator()
homeMenu.add_command(label="축소")
window.mainloop()




from tkinter.filedialog import askopenfilename

def fun_open():
    filepath = askopenfilename(
        title="우사기 gif.gif",
        filetypes=(("gif이미지", "*.gif"), ("모든 파일", "*.*"))  
    )
    if filepath:
        tk_img = PhotoImage(file=filepath)  
        image_label.config(image=tk_img)
        image_label.image = tk_img

window = Tk()
window.title("우사기")

image_label = Label(window)
image_label.pack(expand=True)

fun_open()        
window.mainloop()  
