from tkinter import*
from PIL import Image
from PIL import ImageTk
el = Tk()
el.title("Історія")
el.geometry("800x600")
text3 = ""
mark = 0
mark = 0
intvar1 = IntVar()
intvar2 = IntVar()
var3 = IntVar()
var4 = IntVar()
def funktion_mark():
    global mark
    mark += 2
def first_screen(el):
    Button(el, text= "Почати тест", command=lambda:q1(el)).pack()
def q1(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="1.Коли з'явилося слово _Україна_?").pack()
    Radiobutton(el, text = "1113", variable = intvar1, value = 1).pack()
    Radiobutton(el, text="1187", variable=intvar1, value=2, command=funktion_mark).pack()
    Radiobutton(el, text="991", variable=intvar1, value=3).pack()
    Radiobutton(el, text="1117", variable=intvar1, value=4).pack()
    Button(el, text="Наступне", command=lambda: q2(el)).pack()
def q2(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="2.В якому році Київська Русь прийняла християнство?").pack()
    Radiobutton(el, text = "1018", variable = intvar2, value = 1).pack()
    Radiobutton(el, text="999", variable=intvar2, value=2).pack()
    Radiobutton(el, text="988", variable=intvar2, value=3, command=funktion_mark).pack()
    Radiobutton(el, text="1014", variable=intvar2, value=4).pack()
    Button(el, text = "Наступне", command = lambda:q3(el)).pack()
def q3(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="3.Хто такі козаки?").pack()
    Radiobutton(el, text="об'єднання тюркських та інших племен, що вперше згадується у VIII столітті",variable=var3, value=1).pack()
    Radiobutton(el,text="Члени самоврядних чоловічих військових, згодом і територіальних громад, що з 15 століття існували на теренах Українського _Дикого поля_",variable=var3, value=2, command=funktion_mark).pack()
    Radiobutton(el,text="Незаможні селяни, наймані робітники, дрібна шляхта й нижче духовенство, які були борцями проти польської неволі.",variable=var3, value=3).pack()
    Radiobutton(el,text="це середньовічна народність тюркської групи. Цей народ населяв Євразійський степ у XI-XII століттях, відомий у той час як Дешт-і Кипчак.",variable=var3, value=4).pack()
    Button(el, text="Наступне", command=lambda:q4(el)).pack()
def q4(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="4.Назвіть першого гетьмана Запорозької Січі").pack()
    Radiobutton(el, text="Богдан Хмельницький", variable=var4, value=1).pack()
    Radiobutton(el, text="Дмитро Вишнивецький (Байда)", variable=var4, value=2, command=funktion_mark).pack()
    Radiobutton(el, text="Петро Калнишевський", variable=var4, value=3).pack()
    Radiobutton(el,
                           text="Іван Виговський",
                           variable=var4, value=4, command=funktion_mark).pack()
    Button(el, text="Наступне", command=lambda: q5(el)).pack()
def q5(el):
    global mark
    for widget in el.winfo_children():
        widget.destroy()
    image = Image.open("1.jpg")
    image = image.resize((200,200))
    bogdan = ImageTk.PhotoImage(image)
    image_label = Label(el, image=bogdan)
    image_label.image = bogdan
    image_label.place(x=580, y=10)
    label2 = Label(el, text = "2", font="5")
    label2.place(x=575,y=10)

    image = Image.open("2.jpg")
    image = image.resize((200, 200))
    pavlo = ImageTk.PhotoImage(image)
    image_label = Label(el, image=pavlo)
    image_label.image = pavlo
    image_label.place(x=580, y=220)
    label3 = Label(el, text = "4", font="5")
    label3.place(x=575,y=220)

    image = Image.open("3.jpg")
    image = image.resize((200, 200))
    petro = ImageTk.PhotoImage(image)
    image_label = Label(el, image=petro)
    image_label.image = petro
    image_label.place(x=370, y=220)
    label4 = Label(el, text = "3", font="5")
    label4.place(x=365,y=220)

    image = Image.open("4.jpg")
    image = image.resize((200, 200))
    severin = ImageTk.PhotoImage(image)
    image_label = Label(el, image=severin)
    label1 = Label(el, text = "1", font="5")
    label1.place(x=365,y=10)
    image_label.image = severin
    image_label.place(x=370, y=10)

    result1 = Button(el, text="Показати результат", command=result)
    result1.place(x=380, y=430)

    name1 = Label(el, text="Богдан Хмельницький")
    name1.place(x=10,y=10)
    enter1 = Entry(el, width = 5)
    enter1.place(x = 150, y=10)

    name2 = Label(el, text="Петро Дорошенко")
    name2.place(x=10, y=40)
    enter2 = Entry(el, width=5)
    enter2.place(x=150, y=40)

    name3 = Label(el, text="Северин Наливайко")
    name3.place(x=10, y=70)
    enter3 = Entry(el, width=5)
    enter3.place(x=150, y=70)

    name4 = Label(el, text="Павло Полуботок")
    name4.place(x=10, y=100)
    enter4 = Entry(el, width=5)
    enter4.place(x=150, y=100)

    button12 = Button(el, text="Зберегти", command=lambda: mark_1(el, enter1, enter2, enter3, enter4))
    button12.place(x=190, y=50)
def q6(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="6. Які території контролювали запорозькі козаки?").pack()
    Radiobutton(el, text="Лівобережна Україна", variable=var6, value=1).pack()
    Radiobutton(el, text="Правобережна Україна", variable=var6, value=2).pack()
    Radiobutton(el, text="Запорізька Січ", variable=var6, value=3).pack()
    Radiobutton(el, text="Кримське ханство", variable=var6, value=4).pack()
    Button(el, text="Наступне", command=lambda: q7(el)).pack()

def q7(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="7. Хто був автором козацької гімназії у Чигирині?").pack()
    Radiobutton(el, text="Іван Виговський", variable=var7, value=1).pack()
    Radiobutton(el, text="Петро Дорошенко", variable=var7, value=2).pack()
    Radiobutton(el, text="Богдан Хмельницький", variable=var7, value=3).pack()
    Radiobutton(el, text="Петро Могила", variable=var7, value=4).pack()
    Button(el, text="Наступне", command=lambda: q8(el)).pack()

def q8(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="8. Яка подія відбулася під час Хмельниччини 1648-1654 років?").pack()
    Radiobutton(el, text="Битва під Жовтими Водами", variable=var8, value=1, command=funktion_mark).pack()
    Radiobutton(el, text="Визнання козацтва в офіційному статусі", variable=var8, value=2).pack()
    Radiobutton(el, text="Закінчення війни з Російським царством", variable=var8, value=3).pack()
    Radiobutton(el, text="Прийняття Конституції Пилипа Орлика", variable=var8, value=4).pack()
    Button(el, text="Наступне", command=lambda: q9(el)).pack()

def q9(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="9. Яка подія вважається початком козацького руху?").pack()
    Radiobutton(el, text="Укладання Хмельницьким угод з Російським царством", variable=var9, value=1).pack()
    Radiobutton(el, text="Заснування Запорозької Січі", variable=var9, value=2, command=funktion_mark).pack()
    Radiobutton(el, text="Битва під Жовтими Водами", variable=var9, value=3).pack()
    Radiobutton(el, text="Відновлення козацької держави в Україні", variable=var9, value=4).pack()
    Button(el, text="Наступне", command=lambda: q10(el)).pack()

def q10(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="10. Хто був гетьманом Запорозької Січі під час Коліївщини?").pack()
    Radiobutton(el, text="Павло Полуботок", variable=var10, value=1).pack()
    Radiobutton(el, text="Максим Залізняк", variable=var10, value=2).pack()
    Radiobutton(el, text="Семен Палий", variable=var10, value=3).pack()
    Radiobutton(el, text="Максим Кривоніс", variable=var10, value=4, command=funktion_mark).pack()
    Button(el, text="Завершити тест", command=lambda: result(el)).pack()

var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()

def mark_1(el, enter1, enter2, enter3, enter4):
    global mark
    answer = enter1.get()
    answer1 = enter2.get()
    answer2 = enter3.get()
    answer3 = enter4.get()
    if answer == "2":
        mark += 1
        print(answer)
    if answer1 == "3":
        mark += 1
    if answer2 == "1":
        mark += 1
    if answer3 == "4":
        mark += 1
def result():
    global mark
    mark1 = Label(el, text="Ваша оцінка - " + str(mark) + "!")
    mark1.grid(column=2, row=8)
first_screen(el)
el.mainloop()