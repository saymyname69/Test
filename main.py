import tkinter


def first_second():
    label_first.place_forget()
    button_first.place_forget()
    label_second.place(x=100, y=100)
    button_second.place(x=180, y=300)
    rad1_second.place(x=170, y=200)
    rad2_second.place(x=170, y=225)
    rad3_second.place(x=170, y=250)


def second_third():
    label_second.place_forget()
    button_second.place_forget()
    rad1_second.place_forget()
    rad2_second.place_forget()
    rad3_second.place_forget()
    label_third.place(x=100, y=100)
    button_third.place(x=180, y=300)
    rad1_third.place(x=170, y=200)
    rad2_third.place(x=170, y=225)
    rad3_third.place(x=170, y=250)


def third_fourth():
    label_third.place_forget()
    button_third.place_forget()
    rad1_third.place_forget()
    rad2_third.place_forget()
    rad3_third.place_forget()
    label_fourth.place(x=120, y=100)
    button_fourth.place(x=180, y=300)
    rad1_fourth.place(x=170, y=200)
    rad2_fourth.place(x=170, y=225)
    rad3_fourth.place(x=170, y=250)


def fourth_fifth():
    label_fourth.place_forget()
    button_fourth.place_forget()
    rad1_fourth.place_forget()
    rad2_fourth.place_forget()
    rad3_fourth.place_forget()
    label_fifth.place(x=120, y=100)
    button_fifth.place(x=180, y=300)
    rad1_fifth.place(x=170, y=200)
    rad2_fifth.place(x=170, y=225)
    rad3_fifth.place(x=170, y=250)
    rad4_fifth.place(x=170, y=275)


def fifth_sixth():
    label_fifth.place_forget()
    button_fifth.place_forget()
    rad1_fifth.place_forget()
    rad2_fifth.place_forget()
    rad3_fifth.place_forget()
    rad4_fifth.place_forget()
    label_sixth.place(x=100, y=100)
    button_sixth.place(x=150, y=300)


def sixth_seventh():
    label_sixth.place_forget()
    button_sixth.place_forget()
    window.destroy()


res = 0
ans1 = 3
ans2 = 1
ans3 = 3
ans4 = 4


window = tkinter.Tk()
window.geometry("400x400")
label_first = tkinter.Label(window, text='Тестирование\n Для начала тестирования нажмите Начать')
label_first.place(x=80, y=100)
button_first = tkinter.Button(window, text='Начать', command=first_second)
button_first.place(x=180, y=300)

label_second = tkinter.Label(window, text='Вопрос 1.\n  Ваш любимый жанр фильмов?\n')
rad1_second = tkinter.Radiobutton(window, text='Боевики', value=1)
rad2_second = tkinter.Radiobutton(window, text='Детективы', value=2)
rad3_second = tkinter.Radiobutton(window, text='Фантастика', value=3)
button_second = tkinter.Button(window, text='Далее', command=second_third)

label_third = tkinter.Label(window, text='Вопрос 2.\n  Ваша любимая музыка? \n')
rad1_third = tkinter.Radiobutton(window, text='Классика', value=1)
rad2_third = tkinter.Radiobutton(window, text='Рэп', value=2)
rad3_third = tkinter.Radiobutton(window, text='Поп', value=3)
button_third = tkinter.Button(window, text='Далее', command=third_fourth)

label_fourth = tkinter.Label(window, text='Вопрос 3.\n  Ваш любимый цвет? \n')
rad1_fourth = tkinter.Radiobutton(window, text='Красный', value=1)
rad2_fourth = tkinter.Radiobutton(window, text='Жёлтый', value=2)
rad3_fourth = tkinter.Radiobutton(window, text='Зелёный', value=3)
button_fourth = tkinter.Button(window, text='Далее', command=fourth_fifth)

label_fifth = tkinter.Label(window, text='Вопрос 4.\n  Ваше любимое время года? \n')
rad1_fifth = tkinter.Radiobutton(window, text='Осень', value=1)
rad2_fifth = tkinter.Radiobutton(window, text='Зима', value=2)
rad3_fifth = tkinter.Radiobutton(window, text='Весна', value=3)
rad4_fifth = tkinter.Radiobutton(window, text='Лето', value=4)
button_fifth = tkinter.Button(window, text='Далее', command=fifth_sixth)

label_sixth = tkinter.Label(window, text='Ваш результат:')
button_sixth = tkinter.Button(window, text='Завершить', command=sixth_seventh)
window.mainloop()
