import controller
from tkinter import *

def set_new_contact():
    elements = controller.get_elements()
    name = elements['name'].get()
    surname = elements['surname'].get()
    phone_number = elements['phone'].get()
    contact = f' {name} {surname} {phone_number}'
    elements['all_List'].insert(END, contact)