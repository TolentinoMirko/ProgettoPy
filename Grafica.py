from tkinter import messagebox
import pyodbc
from tkinter import *
import tkinter.ttk as ttk


# Connessione al database SQL Server
server = '5.172.64.20\sqlexpress'  # indirizzo del server
database = 'riva.valentino'  # nome del database
username = 'riva.valentino'  # nome utente del database
password = 'xxx123##'  # password di accesso al database
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE=' +
                      database+';UID='+username+';PWD='+password)  # collegamento al server

root = Tk()  # creazione di una nuova finestra con tkinter
root.geometry("400x300")  # dimensioni della finestra
root.title("Musica")  # titolo della finestra

# -------------------------------------------------Artisti------------------------------------------------------#


def artisti_new_tab():
    root = Tk()
    root.geometry("400x300")
    root.title("Collegamento con database in artisti")
    titolo_artisti = Label(
        root, text="Che azione desideri effettuare con gli artisti?")
    titolo_artisti.grid(row=0, column=0, padx=10, pady=10)

    def mostra():
        root = Tk()
        root.geometry("400x300")
        root.title("aggiuta artista")
        # Creazione delle label
        # creazione label "Titolo"
        nome_d_arte = ttk.Label(root, text="nome d'arte:")
        # posizione della label
        nome_d_arte.grid(row=0, column=0, padx=10, pady=10)

        nome = ttk.Label(root, text="nome:")  # creazione label "Artista"
        nome.grid(row=1, column=0, padx=10, pady=10)  # posizione della label

        cognome = ttk.Label(root, text="cognome:")  # creazione label "Anno"
        # posizione della label
        cognome.grid(row=2, column=0, padx=10, pady=10)

        v_arte = StringVar(root)
        v_nome = StringVar(root)
        v_cognome = StringVar(root)

        entry_nome_d_arte = ttk.Entry(root, width=30, textvariable=v_arte)
        entry_nome_d_arte.grid(row=0, column=1, padx=10, pady=10)

        entry_nome = ttk.Entry(root, width=30, textvariable=v_nome)
        entry_nome.grid(row=1, column=1, padx=10, pady=10)

        entry_cognome = ttk.Entry(root, width=30, textvariable=v_cognome)
        entry_cognome.grid(row=2, column=1, padx=10, pady=10)

        button_Nuovo_artista = ttk.Button(
            root, text="Inserisci nel db", command=lambda: insert_into_database_cantante(v_arte.get(), v_nome.get(), v_cognome.get()))
        button_Nuovo_artista.grid(
            row=8, column=0, columnspan=2, padx=10, pady=10)

    def insert_into_database_cantante(nome_d_arte, nome, cognome):
        if nome_d_arte == "" :
            return messagebox.showerror("Inserimento dati",
            "tutti i cantanti hanno un nome") 
        # Connessione al database SQL Server

        print(nome_d_arte, nome, cognome)

        conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server +
                              ';DATABASE='+database+';UID='+username+';PWD=' + password)

        # Esecuzione della query SQL per l'inserimento dei dati nella tabella
        cursor = conn.cursor()
        cursor.execute("INSERT INTO artisti (nome_d_arte, nome, cognome) VALUES (?, ?, ?)", (nome_d_arte, nome, cognome))
        conn.commit()
        cursor.close()
        # Messaggio di conferma dell'inserimento dei dati
        messagebox.showinfo(
            "Inserimento dati", "I dati sono stati inseriti con successo nel database")

    titolo_artisti = ttk.Label(
        root, text="Che azione desideri effettuare con gli artisti?")
    titolo_artisti.grid(row=0, column=0, padx=10, pady=10)

    buttonaggiungi = ttk.Button(root, text="Aggiungi", command=mostra)
    buttonaggiungi.grid(row=1, column=3, columnspan=2, padx=10, pady=10)

# -------------------------------------------------genere------------------------------------------------------#



def generi_new_tab():
    root = Tk()
    root.geometry("400x300")
    root.title("Collegamento con database in generi")
    titolo_generi = ttk.Label(root, text="Che azione desideri effettuare con i generi?")
    titolo_generi.grid(row=0, column=0, padx=10, pady=10)

    def mostra():
        root = Tk()
        root.geometry("400x300")
        root.title("Aggiungi genere")

        # Creazione delle label
        nome_genere = ttk.Label(root, text="Nome genere:")
        nome_genere.grid(row=0, column=0, padx=10, pady=10)

        # Creazione delle entry per l'inserimento dei dati
        v_genere = StringVar(root)
        entry_genere = ttk.Entry(root, width=30, textvariable=v_genere)
        entry_genere.grid(row=0, column=1, padx=10, pady=10)

        # Creazione del bottone per l'inserimento dei dati nel database
        button_Nuovo_genere = ttk.Button(
            root, text="Inserisci nel db", command=lambda: insert_into_database_genere(v_genere.get()))
        button_Nuovo_genere.grid(
            row=8, column=0, columnspan=2, padx=10, pady=10)

    def insert_into_database_genere(nome_genere):
        if nome_genere == "":
            return messagebox.showerror("Inserimento dati",
                                         "Il nome del genere non può essere vuoto")

        # Esecuzione della query SQL per l'inserimento dei dati nella tabella
        cursor = conn.cursor()
        cursor.execute("INSERT INTO genere (nome) VALUES (?)",
                       (nome_genere,))
        conn.commit()
        cursor.close()

        # Messaggio di conferma dell'inserimento dei dati
        messagebox.showinfo(
            "Inserimento dati", "I dati sono stati inseriti con successo nel database")

    titolo_generi = ttk.Label(root, text="Che azione desideri effettuare con i generi?")
    titolo_generi.grid(row=0, column=0, padx=10, pady=10)

    buttonaggiungi = ttk.Button(root, text="Aggiungi", command=mostra)
    buttonaggiungi.grid(row=1, column=3, columnspan=2, padx=10, pady=10)


# -------------------------------------------------canzoni------------------------------------------------------#


def canzoni_new_tab():
    root = Tk()
    root.geometry("400x300")
    root.title("Collegamento con database in canzoni")
    titolo_canzoni = ttk.Label(root, text="Che azione desideri effettuare con le canzoni?")
    titolo_canzoni.grid(row=0, column=0, padx=10, pady=10)

    def mostra():
        root = Tk()
        root.geometry("400x300")
        root.title("Aggiungi canzone")

        # Creazione delle label
        titolo_canzoni = ttk.Label(root, text="Titolo canzone:")
        titolo_canzoni.grid(row=0, column=0, padx=10, pady=10)
        artista_canzoni = ttk.Label(root, text="Artista:")
        artista_canzoni.grid(row=1, column=0, padx=10, pady=10)
        genere_canzoni = ttk.Label(root, text="Genere:")
        genere_canzoni.grid(row=2, column=0, padx=10, pady=10)
        anno_canzoni = ttk.Label(root, text="anno:")
        anno_canzoni.grid(row=3, column=0, padx=10, pady=10)
        

        # Creazione delle entry per l'inserimento dei dati
        v_titolo = StringVar(root)
        entry_canzoni_titolo = ttk.Entry(root, width=30, textvariable=v_titolo)
        entry_canzoni_titolo.grid(row=0, column=1, padx=10, pady=10)
        v_artista = StringVar(root)
        entry_canzoni_artista = ttk.Entry(root, width=30, textvariable=v_artista)
        entry_canzoni_artista.grid(row=1, column=1, padx=10, pady=10)
        v_genere = StringVar(root)
        entry_canzoni_genere = ttk.Entry(root, width=30, textvariable=v_genere)
        entry_canzoni_genere.grid(row=2, column=1, padx=10, pady=10)
        v_anno = StringVar(root)
        entry_anno = ttk.Entry(root, width=30, textvariable=v_anno)
        entry_anno.grid(row=3, column=1, padx=10, pady=10)

        # Creazione del bottone per l'inserimento dei dati nel database
        button_nuova_canzoni = ttk.Button(
            root, text="Inserisci nel db", command=lambda: insert_into_database_canzoni(v_titolo.get(), v_artista.get(), v_genere.get(),v_anno.get()))
        button_nuova_canzoni.grid(
            row=8, column=0, columnspan=2, padx=10, pady=10)

    def insert_into_database_canzoni(titolo_canzoni, artista_canzoni, genere_canzoni, anno_canzoni):
        if titolo_canzoni == "" or artista_canzoni == "" or genere_canzoni == "" or anno_canzoni =="":
            return messagebox.showerror("Inserimento dati",
                                         "I campi Titolo, Artista e Genere non possono essere vuoti")

        # Esecuzione della query SQL per l'inserimento dei dati nella tabella
        cursor = conn.cursor()
        cursor.execute("INSERT INTO canzoni (artista_id , genere_id , anno ,nome_canzone ) VALUES (?, ?, ?,?)",
                       (artista_canzoni,genere_canzoni, anno_canzoni, 
                        titolo_canzoni))
        conn.commit()
        cursor.close()

        # Messaggio di conferma dell'inserimento dei dati
        messagebox.showinfo(
            "Inserimento dati", "I dati sono stati inseriti con successo nel database")

    titolo_canzoni = ttk.Label(root, text="Che azione desideri effettuare con le canzoni?")
    titolo_canzoni.grid(row=0, column=0, padx=10, pady=10)

    buttonaggiungi = ttk.Button(root, text="Aggiungi", command=mostra)
    buttonaggiungi.grid(row=1, column=3, columnspan=2, padx=10, pady=10)


button_artisti = ttk.Button(root, text="Artisti", command=artisti_new_tab)
button_artisti.grid(row=1, column=3, columnspan=2, padx=10, pady=10)
buttonGeneri = ttk.Button(root, text="Generi", command=generi_new_tab)
buttonGeneri.grid(row=3, column=3, columnspan=2, padx=10, pady=10)
buttonCanzoni = ttk.Button(root, text="Canzoni", command=canzoni_new_tab)
buttonCanzoni.grid(row=4, column=3, columnspan=2, padx=10, pady=10)


root.mainloop()
