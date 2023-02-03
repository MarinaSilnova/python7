import model
import view
from tkinter import *
from tkinter import ttk

elements={}

def add_contact():
    view.set_new_contact()

def add_to_listbox(contact):
    elements['all_List'].insert(END, contact)
    send_contacts_list_to_model()

def get_elements():
    return elements

def delete_contact():
    elements['all_List'].delete(elements['all_List'].curselection()[0])
    send_contacts_list_to_model()


def send_contacts_list_to_model():
    contacts_list = elements['all_List'].get(0, END)
    model.write_contacts(contacts_list)

def start():
   
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    Label(frm, text='Справочник').grid(row = 0, column = 0) 

    Label(frm, text='Введите имя').grid(row = 1, column = 0)
    name_ent = Entry(frm)
    name_ent.grid(row = 1, column = 1)
    elements['name']=name_ent

    Label(frm, text='Введите фамилию').grid(row = 2, column = 0)
    surname_ent = Entry(frm) 
    surname_ent.grid(row = 2, column = 1)
    elements['surname']=surname_ent

    Label(frm, text='Введите номер телефона').grid(row = 3, column = 0)
    phone_number_ent = Entry(frm)
    phone_number_ent.grid(row = 3, column = 1)
    elements['phone']=phone_number_ent

    add_contact_btn = Button(frm, text='Добавить контакт',command = add_contact).grid(row = 4, column = 0 )
    delete_contact_btn = Button(frm, text='Удалить контакт', command = delete_contact).grid(row = 4, column = 1)

    all_contacts_lbox = Listbox(frm)
    all_contacts_lbox.grid(row = 5, column = 0)
    elements['all_List'] = all_contacts_lbox
    model.read_contacts()
   

    root.mainloop()