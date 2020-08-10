#coding:utf-8
from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')


def liste_populate():
    liste_produits.delete(0, END)
    for row in db.fetch():
        liste_produits.insert(END, row)

def ajouter_item():
    if texte_produit.get() == '' or texte_client.get() == '' or texte_magasin.get() == '' or texte_prix.get() == '':
        messagebox.showerror("incorrect","Remplissez les champ vide")
        return
        
    db.insert(texte_produit.get(),texte_client.get(), texte_magasin.get(), texte_prix.get())
    liste_produits.delete(0, END)
    liste_produits.insert(END, (texte_produit.get(), texte_client.get(),texte_magasin.get(), texte_prix.get()))
    effacer_text()
    liste_populate()


def select_item(event):
    try:
        global selected_item
        index = liste_produits.curselection()[0]
        selected_item = liste_produits.get(index)

        entre_produit.delete(0, END)
        entre_produit.insert(END, selected_item[1])
        entre_client.delete(0, END)
        entre_client.insert(END, selected_item[2])
        entre_magasin.delete(0, END)
        entre_magasin.insert(END, selected_item[3])
        entre_prix.delete(0, END)
        entre_prix.insert(END, selected_item[4])
    except IndexError:
        pass


def annuler_item():
    db.remove(selected_item[0])
    effacer_text()
    liste_populate()

def maj_item():
    db.update(selected_item[0],texte_produit.get(),texte_client.get(), texte_magasin.get(), texte_prix.get())
    liste_populate()

def effacer_text():
    entre_produit.delete(0, END)
    entre_client.delete(0, END)
    entre_magasin.delete(0, END)
    entre_prix.delete(0, END)




app = Tk()
app.title("Bon de commande ")



x_ecran = int(app.winfo_screenwidth())
y_ecran = int(app.winfo_screenheight())
xmin = 720
ymin = 480
pos_x = (x_ecran) // 2 - (xmin // 2)
pos_y = (y_ecran) // 2 - (ymin // 2)
# apropos du fenetre
app.resizable(width=FALSE,height=FALSE)
app.geometry(f"{xmin}x{ymin}+{pos_x}+{pos_y}")

#produit
texte_produit = StringVar()
label_produit = Label(app, text=' Nom du produit ', font=('bold',12), pady=20)
label_produit.grid(row=0,column=0, sticky=W)
entre_produit = Entry(app, textvariable=texte_produit)
entre_produit.grid(row=0,column=1)

#client
texte_client = StringVar()
label_client = Label(app, text=' Client ', font=('bold',12))
label_client.grid(row=0,column=2, sticky=W)
entre_client = Entry(app, textvariable=texte_client)
entre_client.grid(row=0,column=3)

#magasin
texte_magasin = StringVar()
label_magasin = Label(app, text=' Magasin ', font=('bold',12))
label_magasin.grid(row=1,column=0, sticky=W)
entre_magasin = Entry(app, textvariable=texte_magasin)
entre_magasin.grid(row=1,column=1)

#prix
texte_prix = StringVar()
label_prix = Label(app, text='  Prix ', font=('bold',12))
label_prix.grid(row=1,column=2, sticky=W)
entre_prix = Entry(app, textvariable=texte_prix)
entre_prix.grid(row=1,column=3)

#liste de stock
liste_produits = Listbox(app, height=8, width=50, border=0)
liste_produits.grid(row=3, column = 0, columnspan=3, rowspan=6, pady=20, padx=20)

#bar de scroll
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

#liée le scroll au listbox
liste_produits.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=liste_produits.yview)

#selection
liste_produits.bind('<<ListboxSelect>>', select_item)

#boutton
ajout_btn = Button(app, text='Ajout produit', width=12, command=ajouter_item)
ajout_btn.grid(row=2, column=0, pady=20)

annuler_btn = Button(app, text='Annuler produit', width=12, command=annuler_item)
annuler_btn.grid(row=2, column=1, pady=20)

maj_btn = Button(app, text='M A J produit', width=12, command=maj_item)
maj_btn.grid(row=2, column=2, pady=20)

effacer_btn = Button(app, text='Effacer texte', width=12, command=effacer_text)
effacer_btn.grid(row=2, column=3, pady=20)

liste_populate()

app.mainloop()