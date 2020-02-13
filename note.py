from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Блокнот')
root.geometry('1000x600+100+300')

# создаем главное меню
main_menu = Menu(root)
root.config(menu=main_menu)


# Открыть //функция открытия файла
def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы', '*.txt'),
                                                                           ('Все файлы', '*.*')))
    if file_path:
        main_text_window.delete('1.0', END)
        main_text_window.insert('1.0', open(file_path, encoding='utf-8').read())


# Сохранить //функция сохранения файла
def save_file():
    file_path = filedialog.asksaveasfilename(title='Выбор имени файла', filetypes=(('Текстовые документы', '*.txt'),
                                                                                   ('Все файлы', '*.*')))
    get_save = open(file_path, 'w', encoding='utf-8')
    save_text = main_text_window.get('1.0', END)
    get_save.write(save_text)
    get_save.close()


# Выход // Функция выхода из программы
def quit_note():
    if messagebox.askyesno(title='Выйти', message='Вы уверены что хотите выйти?'):
        root.destroy()


# в главное меню добавляем его первый пункт "Файл"
file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Файл', menu=file_menu)
# в пункт меню "файл" добавряем его содержимое
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=quit_note)


# О программе // фенкция вызова окна
def about_program():
    messagebox.showinfo(title='О програме', message='Глупо канеш было добавлять этот раздел в обычный блокнот, '
                                                    'но а вдруг ты не знаешь что с ним днлать. Я вот тоже не знаю.\n\n'
                                                    'Version: 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1')


# в главное меню добавляем его Второй пункт "Темы"
theme_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Настройки', menu=theme_menu)
# в пункт меню "Справка" добавряем его содержимое
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label='Темная тема', command=lambda: change_theme('dark'))
theme_menu_sub.add_command(label='Светлая тема', command=lambda: change_theme('light'))
theme_menu.add_cascade(label='Оформление', menu=theme_menu_sub)
theme_menu.add_command(label='О программе', command=about_program)


# рисуем фрейм для меню и текста и выводим их упаковщиком pack
frame_text = Frame(root)
frame_text.pack(fill=BOTH, expand=1)

# Theme // создаем словарь с параметрами темы

theme_colors = {
    'dark': {
      'text_bg': '#343D46', 'text_fg': '#FFF', 'cursor': '#EDA756', 'select_bg': '#4E5A65'
    },

    'light': {
        'text_bg': '#FFF', 'text_fg': '#000', 'cursor': '#8000FF', 'select_bg': '#777'
    }
}


# определяем функцию для смены тем
def change_theme(theme):
    main_text_window['bg'] = theme_colors[theme]['text_bg']
    main_text_window['fg'] = theme_colors[theme]['text_fg']
    main_text_window['insertbackground'] = theme_colors[theme]['cursor']
    main_text_window['selectbackground'] = theme_colors[theme]['select_bg']


# текстовое поле, его параметры и скролбар
main_text_window = Text(frame_text, bg=theme_colors['dark']['text_bg'], fg=theme_colors['dark']['text_fg'],
                        insertbackground=theme_colors['dark']['cursor'],
                        selectbackground=theme_colors['dark']['select_bg'],
                        padx=10, pady=10, wrap=WORD, spacing3=5, font=('Courier New', 12))
main_text_window.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(frame_text, command=main_text_window.yview)
scroll.pack(fill=Y, side=LEFT)
main_text_window.config(yscrollcommand=scroll.set)


root.mainloop()