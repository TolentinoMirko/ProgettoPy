from tkinter import messagebox
import pyodbc
from tkinter import *

# Connessione al database SQL Server
server = '192.168.40.16\SQLEXPRESS' #variabile che contiene l'indirizzo del server
database = 'riva.valentino' #variabile che contiene il nome del database 
username = 'riva.valentino' #variabile che contiene il nome utente del database
password = 'xxx123##' #password di accesso al database
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password) #collegamento al server 

from tkinter import * 

root = Tk() #creazione di una nuova finestra con tkinter
root.geometry("400x300") #dimensioni della finestra
root.title("Collegamento con database") #titolo della finestra



def artisti_new_tab():
    root = Tk()
    root.geometry("400x300")
    root.title("Collegamento con database in artisti")
    titolo_artisti= Label(root,text="Artisti:")
    titolo_artisti.grid(row=0,column=0,padx=10,pady=10) 
    
    def mostra():
        #conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        #cursor = conn.cursor()
        #cursor.execute("Select ")
        #conn.commit()
        #cursor.close()
        #conn.close()
        meringa= Label(root,text="funzia")  
        meringa.grid(row=4,column=5,padx=10,pady=10)


    buttonMostra = Button(root, text="Mostra", command=mostra)
    buttonMostra.grid(row=1, column=3, columnspan=2, padx=10, pady=10)

buttonArtisti = Button(root, text="Artisti", command=artisti_new_tab)
buttonArtisti.grid(row=1, column=3, columnspan=2, padx=10, pady=10)

def generi_new_tab():
     root = Tk()
     root.geometry("400x300")
     root.title("Collegamento con database in generi")
     titolo_generi= Label(root,text="Generi:")  
     titolo_generi.grid(row=0,column=0,padx=10,pady=10)



buttonGeneri = Button(root, text="Generi", command=generi_new_tab)
buttonGeneri.grid(row=3, column=3, columnspan=2, padx=10, pady=10)


def canzoni_new_tab():
    root = Tk()
    root.geometry("400x300")
    root.title("Collegamento con database in generi")
    titolo_canzoni= Label(root,text="Canzoni:")  
    titolo_canzoni.grid(row=0,column=0,padx=10,pady=10)

buttonCanzoni=Button(root, text="Canzoni", command=canzoni_new_tab)
buttonCanzoni.grid(row=4, column=3, columnspan=2, padx=10, pady=10)


# Definizione della funzione per l'inserimento dei dati nel database
#def insert_into_database():
    # Connessione al database SQL Server
    
    #conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

    # Recupero dei dati dai campi di input
    #titolo = entry_titolo.get()
    #artista = entry_artista.get()
    #anno = entry_anno.get()
    #genere = entry_genere.get()


    # Esecuzione della query SQL per l'inserimento dei dati nella tabella
    #cursor = conn.cursor()
    #cursor.execute("INSERT INTO Musica (titolo, artista, anno, genere) VALUES (?, ?, ?, ?)", (titolo, artista, anno, genere))
    #conn.commit()
    #cursor.close()

    # Chiusura della connessione al database
    #conn.close()

    # Messaggio di conferma dell'inserimento dei dati
    #messagebox.showinfo("Inserimento dati", "I dati sono stati inseriti con successo nel database")


root.mainloop()
