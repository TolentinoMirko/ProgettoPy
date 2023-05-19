from tkinter import messagebox
import pyodbc
from tkinter import *

# Connessione al database SQL Server
server = '192.168.40.16\SQLEXPRESS'
database = 'riva.valentino'
username = 'riva.valentino'
password = 'xxx123##'
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Collegamento con database")



# Creazione delle label
titolo = Label(root, text="Titolo:")
titolo.grid(row=0, column=0, padx=10, pady=10)

artista = Label(root, text="Artista:")
artista.grid(row=1, column=0, padx=10, pady=10)

anno = Label(root, text="Anno:")
anno.grid(row=2, column=0, padx=10, pady=10)

genere = Label(root, text="Genere:")
genere.grid(row=3, column=0, padx=10, pady=10)

# Creazione dei campi di input
entry_titolo = Entry(root, width=30)
entry_titolo.grid(row=0, column=1, padx=10, pady=10)

entry_artista = Entry(root, width=30)
entry_artista.grid(row=1, column=1, padx=10, pady=10)

entry_anno = Entry(root, width=30)
entry_anno.grid(row=2, column=1, padx=10, pady=10)

entry_genere = Entry(root, width=30, )
entry_genere.grid(row=3, column=1, padx=10, pady=10)

# Definizione della funzione per l'inserimento dei dati nel database
def insert_into_database():
    # Connessione al database SQL Server
    
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

    # Recupero dei dati dai campi di input
    titolo = entry_titolo.get()
    artista = entry_artista.get()
    anno = entry_anno.get()
    genere = entry_genere.get()

    # Controllo se tutti i campi sono stati riempiti
    if titolo and artista and anno and genere:
    # Esecuzione della query SQL per l'inserimento dei dati nella tabella
        cursor.execute("INSERT INTO Musica (titolo, artista, anno, genere) VALUES (?, ?, ?, ?)", (titolo, artista, anno, genere))
        conn.commit()
    else:
        print("Errore: tutti i campi devono essere riempiti")

    

    # Esecuzione della query SQL per l'inserimento dei dati nella tabella
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Musica (titolo, artista, anno, genere) VALUES (?, ?, ?, ?)", (titolo, artista, anno, genere))
    conn.commit()
    cursor.close()

    # Chiusura della connessione al database
    conn.close()

    # Messaggio di conferma dell'inserimento dei dati
    messagebox.showinfo("Inserimento dati", "I dati sono stati inseriti con successo nel database")

# Creazione del pulsante per l'inserimento dei dati nel database
button = Button(root, text="Salva", command=insert_into_database)
button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()