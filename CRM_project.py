from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

win = Tk()
win.title(' CRM system ')
win.config(bg='aliceblue')
win.geometry('1200x1000+260+20')
#win.iconbitmap('images/smile.ico')

# +++++++++++ FRAMES + LOGO +++++++++
proj_name = Label(win, text='Project Mini CRM System!', font=('Didot', 20, 'bold'), fg='Snow', bg='darkslategrey', bd=10, relief=GROOVE)
proj_name.pack(side=TOP, fill=X)

add_frame = LabelFrame(win, text='Add Records',font=('Didot', 12, 'bold'), fg='saddlebrown', bg='aliceblue', bd=3, relief=GROOVE)
add_frame.place(x=10, y=60, width=350, height=280)

com_frame = LabelFrame(win, text='Command Buttons',font=('Didot', 12, 'bold'), fg='saddlebrown', bg='aliceblue', bd=3, relief=GROOVE)
com_frame.place(x=370, y=60, width=170, height=160)

remove_frame = LabelFrame(win, text='Remove Buttons',font=('Didot', 12, 'bold'), fg='saddlebrown', bg='aliceblue', bd=3, relief=GROOVE)
remove_frame.place(x=10, y=350, width=530, height=90)

up_frame = LabelFrame(win, text='Move Up-Down Buttons',font=('Didot', 12, 'bold'), fg='saddlebrown', bg='aliceblue', bd=3, relief=GROOVE)
up_frame.place(x=10, y=450, width=530, height=100)

gallery_frame = Frame(win, bg='aliceblue')
gallery_frame.place(x=10, y=560, width=530, height=360)

inf_frame = LabelFrame(win, bg='white')
inf_frame.place(x=555, y=680, width=630, height=230)

pic_frame = Frame(win, bg='aliceblue')
pic_frame.place(x=555, y=60, width=630, height=600)

logo_frame = Frame(win, bg='aliceblue')
logo_frame.place(x=370, y=225, width=170, height=113)

logo = ImageTk.PhotoImage(Image.open('univ_foto/MIT_Logo.png').resize((167,110), Image.BILINEAR))   #, Image.ANTIALIAS
Label(logo_frame, image=logo).place(x=0, y=0)

picture = ImageTk.PhotoImage(Image.open('univ_foto/MIT3.jpg').resize((625,600), Image.BILINEAR))   #, Image.ANTIALIAS
Label(pic_frame, image=picture).place(x=0, y=0)

gallery = ImageTk.PhotoImage(Image.open('univ_foto/MIT.jpg').resize((525,355), Image.BILINEAR))   #, Image.ANTIALIAS
Label(gallery_frame, image=gallery).place(x=0, y=0)

# +++++++++++ TREEVIEW +++++++++

tree_scroll_x = Scrollbar(inf_frame, orient=HORIZONTAL)
tree_scroll_y = Scrollbar(inf_frame, orient=VERTICAL)

my_tree = ttk.Treeview(inf_frame, xscrollcommand=tree_scroll_x.set, yscrollcommand=tree_scroll_y, selectmode=EXTENDED)
my_tree['columns'] = ('ID', 'Fullname', 'Birth Data', 'Address', 'City', 'State', 'Country')

my_tree.pack()

tree_scroll_x.config(command=my_tree.xview)
tree_scroll_y.config(command=my_tree.yview)

tree_scroll_x.pack(side=BOTTOM, fill=X)
tree_scroll_y.pack(side=RIGHT, fill=Y)

# +++++++++++ create columns 
my_tree.column('#0', width=0, stretch= NO)         # show='headings'
my_tree.column('ID', anchor= CENTER, width=50, minwidth=25)
my_tree.column('Fullname', anchor= W, width=200)
my_tree.column('Birth Data', anchor= W, width=200)
my_tree.column('Address', anchor= W, width=100)
my_tree.column('City', anchor= W, width=100)
my_tree.column('State', anchor= W, width=100)
my_tree.column('Country', anchor= W, width=100)

# +++++++++++ create heading columns
my_tree.heading('#0', text='', anchor=W)
my_tree.heading('ID', anchor= CENTER, text='ID')
my_tree.heading('Fullname', anchor= CENTER, text='Fullname')
my_tree.heading('Birth Data', anchor= CENTER, text='Birth Data')
my_tree.heading('Address', anchor= CENTER, text='Address')
my_tree.heading('City', anchor= CENTER, text='City')
my_tree.heading('State', anchor= CENTER, text='State')
my_tree.heading('Country', anchor= CENTER, text='Country')

my_tree.tag_configure('oddrow', background='white')
my_tree.tag_configure('evenrow', background='lightblue')


data = [
    [1, 'Berdi Nuryyew', '12.08.99', 'shayoly', 'Ashgabat', 'Kopetdag', 'Turkmenistan'],
    [2, 'Mahri Nuryyewa', '04.01.01', 'shayoly', 'Ahal', 'Bagtyyarlyk', 'Turkmenistan'],
    [3, 'Aylar Nuryyew', '07.12.98', 'shayoly', 'Mary', "Berkararlyk", 'Turkmenistan'],
    [4, 'Lachyn Ahmedowa', '15.07.97', 'shayoly', 'Lebap', 'Azatlyk', 'Turkmenistan'],
    [5, 'Nury Nuryyew', '03.07.92', 'shayoly', 'Balkan', 'Kopetdag', 'Turkmenistan'],
    [6, 'Berdi Nuryyew', '12.08.99', 'shayoly', 'Ashgabat', 'Kopetdag', 'Turkmenistan'],
    [7, 'Mahri Nuryyewa', '04.01.01', 'shayoly', 'Ahal', 'Bagtyyarlyk', 'Turkmenistan'],
    [8, 'Aylar Nuryyew', '07.12.98', 'shayoly', 'Mary', "Berkararlyk", 'Turkmenistan'],
    [9, 'Lachyn Ahmedowa', '15.07.97', 'shayoly', 'Lebap', 'Azatlyk', 'Turkmenistan'],
    [10, 'Nury Nuryyew', '03.07.92', 'shayoly', 'Balkan', 'Kopetdag', 'Turkmenistan'],
    [11, 'Berdi Nuryyew', '12.08.99', 'shayoly', 'Ashgabat', 'Kopetdag', 'Turkmenistan'],
    [12, 'Mahri Nuryyewa', '04.01.01', 'shayoly', 'Ahal', 'Bagtyyarlyk', 'Turkmenistan'],
    [13, 'Aylar Nuryyew', '07.12.98', 'shayoly', 'Mary', "Berkararlyk", 'Turkmenistan'],
    [14, 'Lachyn Ahmedowa', '15.07.97', 'shayoly', 'Lebap', 'Azatlyk', 'Turkmenistan'],
    [15, 'Nury Nuryyew', '03.07.92', 'shayoly', 'Balkan', 'Kopetdag', 'Turkmenistan'],
    [16, 'Berdi Nuryyew', '12.08.99', 'shayoly', 'Ashgabat', 'Kopetdag', 'Turkmenistan'],
    [17, 'Mahri Nuryyewa', '04.01.01', 'shayoly', 'Ahal', 'Bagtyyarlyk', 'Turkmenistan'],
    [18, 'Aylar Nuryyew', '07.12.98', 'shayoly', 'Mary', "Berkararlyk", 'Turkmenistan'],
    [19, 'Lachyn Ahmedowa', '15.07.97', 'shayoly', 'Lebap', 'Azatlyk', 'Turkmenistan'],
    [20, 'Nury Nuryyew', '03.07.92', 'shayoly', 'Balkan', 'Kopetdag', 'Turkmenistan']
]

count = 0
for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text='',
                   values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow'))
    else:
        my_tree.insert(parent='', index='end', iid=count, text='',
                   values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow'))
    count += 1


# +++++++++++ Command button def +++++++++
def add():
    global count
    my_tree.insert(parent='', index='end', iid=count, text='', values=(id_ent.get(), fname.get(), date.get(), addr.get(), cit.get(), stat.get(), coun.get()))
    count += 1

def update_record():
    selected = my_tree.focus()
    my_tree.item(selected, text='', values = (id_ent.get(), fname.get(), date.get(), addr.get(), cit.get(), stat.get(), coun.get()))

def clear():
    id_ent.delete(0, 'end')
    fname.delete(0, 'end')
    date.delete(0, 'end')
    addr.delete(0, 'end')
    cit.delete(0, 'end')
    stat.delete(0, 'end')
    coun.delete(0, 'end')

# +++++++++++ Remove button def +++++++++

def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)

def remove_one():
    x = my_tree.selection()[0]
    for record in x:
        my_tree.delete(x)

def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(x)

# +++++++++++ Move up-down button def +++++++++

def move_up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

def move_down():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

def select_rec():
    id_ent.delete(0, 'end')
    fname.delete(0, 'end')
    date.delete(0, 'end')
    addr.delete(0, 'end')
    cit.delete(0, 'end')
    stat.delete(0, 'end')
    coun.delete(0, 'end')

    selected = my_tree.focus()
    values = my_tree.item(selected, 'values')

    id_ent.insert(0, values[0])
    fname.insert(0, values[1])
    date.insert(0, values[2])
    addr.insert(0, values[3])
    cit.insert(0, values[4])
    stat.insert(0, values[5])
    coun.insert(0, values[6])

# +++++++++++ Label + Entry +++++++++
id = Label(add_frame, text='ID', font=('Times', 18, 'bold'), fg='saddlebrown', bg='aliceblue', width=10)
fullname = Label(add_frame, text='Fullname', font=('Times', 18, 'bold'), fg='saddlebrown', bg='aliceblue', width=10)
b_date = Label(add_frame, text='Birth Data', font=('Times', 18, 'bold'), fg='saddlebrown', bg='aliceblue', width=10)
address = Label(add_frame, text='Address', font=('Times', 18, 'bold'), fg='saddlebrown', bg='aliceblue', width=10)
city = Label(add_frame, text='City', font=('Times', 18, 'bold'), fg='saddlebrown', bg='aliceblue', width=10)
state = Label(add_frame, text='State', font=('Times', 18, 'bold'), fg='saddlebrown', bg='aliceblue', width=10)
country = Label(add_frame, text='Country', font=('Times', 18, 'bold'), fg='saddlebrown', bg='aliceblue', width=10)

# Entries
id_ent = Entry(add_frame, font=('Times', 16), width=16)
fname = Entry(add_frame, font=('Times', 16), width=16)
date = Entry(add_frame, font=('Times', 16), width=16)
addr = Entry(add_frame, font=('Times', 16), width=16)
cit = Entry(add_frame, font=('Times', 16), width=16)
stat = Entry(add_frame, font=('Times', 16), width=16)
coun = Entry(add_frame, font=('Times', 16), width=16)

id.grid(row=0, column=0)
id_ent.grid(row=0, column=1)
fullname.grid(row=1, column=0)
fname.grid(row=1, column=1)
b_date.grid(row=2, column=0)
date.grid(row=2, column=1)
address.grid(row=3, column=0)
addr.grid(row=3, column=1)
city.grid(row=4, column=0)
cit.grid(row=4, column=1)
state.grid(row=5, column=0)
stat.grid(row=5, column=1)
country.grid(row=6, column=0)
coun.grid(row=6, column=1)

# +++++++++++ BUTTONS +++++++++
# COMMAND BUTTON
btn_add = Button(com_frame, text='Add Record', font=('Times', 14, 'bold'), command=add, fg='saddlebrown', width=12)
btn_add.grid(row=0, column=0, padx=10, pady=1)
btn_up = Button(com_frame, text='Update Record', font=('Times', 14, 'bold'), command=update_record, fg='saddlebrown', width=12)
btn_up.grid(row=1, column=0)
btn_up = Button(com_frame, text='Reset Boxes', font=('Times', 14, 'bold'),command=clear, fg='saddlebrown',width=12)
btn_up.grid(row=2, column=0, pady=1)

# REMOVE BUTTON
btn_move_up = Button(remove_frame, text='Remove all', font=('Times', 16, 'bold'), command=remove_all, fg='saddlebrown', width=12)
btn_move_up.grid(row=0, column=0, padx=10, pady=10)
btn_move_down = Button(remove_frame, text='Remove one', font=('Times', 16, 'bold'), command=remove_one, fg='saddlebrown', width=12)
btn_move_down.grid(row=0, column=1, padx=10, pady=10)
btn_select = Button(remove_frame, text='Remove many', font=('Times', 16, 'bold'), command=remove_many, fg='saddlebrown',width=12)
btn_select.grid(row=0, column=2, padx=10, pady=10)

# MOVE UP_DOWN BUTTON
btn_move_up = Button(up_frame, text='Move up', font=('Times', 16, 'bold'), command=move_up, fg='saddlebrown', width=12)
btn_move_up.grid(row=0, column=0, padx=10, pady=10)
btn_move_down = Button(up_frame, text='Move down', font=('Times', 16, 'bold'), command=move_down, fg='saddlebrown', width=12)
btn_move_down.grid(row=0, column=1, padx=10, pady=10)
btn_select = Button(up_frame, text='Selected record', font=('Times', 16, 'bold'), command=select_rec, fg='saddlebrown',width=12)
btn_select.grid(row=0, column=2, padx=10, pady=10)

win.mainloop()