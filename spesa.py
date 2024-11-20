#1.Inizializza la lista della spesa vuota
lista_spesa = []

#2.Crea un metodo che aggiunge elementi alla lista
def aggiungi_elemento():
    elemento = input("Inserisci l'elemento da aggiungere alla lista: ")
    lista_spesa.append(elemento)
    print(f"{elemento} è stato aggiunto alla lista.")

#3.Crea un metodo che visualizza gli elementi della lista
def visualizza_lista():
    if len(lista_spesa) == 0:
        print("La lista è vuota.")
    else:
        print("Gli elementi nella lista della spesa sono:")
        for idx, elemento in enumerate(lista_spesa):
            print(f"{idx + 1}. {elemento}")
#4.Crea un metodo che rimuove l’elemento selezionato dall’utente dalla lista (tramite indice + facile)
def rimuovi_elemento():
    if len(lista_spesa) == 0:
        print("La lista è vuota. Non puoi rimuovere nulla.")
    else:
        visualizza_lista()
        try:
            indice = int(input("Inserisci l'indice dell'elemento da rimuovere (1 per il primo elemento): ")) - 1
            if 0 <= indice < len(lista_spesa):
                elemento_rimosso = lista_spesa.pop(indice)
                print(f"{elemento_rimosso} è stato rimosso dalla lista.")
            else:
                print("Indice non valido.")
        except ValueError:
            print("Per favore, inserisci un numero valido.")

#5.Aggiungere un menu tramite un ciclo while che permettere all’utente di decidere a quale metodo accedere o se terminare (tipo la scorsa esercitazione)
def menu():
    while True:
        print("\nMenu:")
        print("1. Aggiungi un elemento alla lista")
        print("2. Visualizza la lista")
        print("3. Rimuovi un elemento dalla lista")
        print("4. Esci")

        scelta = input("Scegli un'opzione (1/2/3/4): ")

        if scelta == '1':
            aggiungi_elemento()
        elif scelta == '2':
            visualizza_lista()
        elif scelta == '3':
            rimuovi_elemento()
        elif scelta == '4':
            print("Arrivederci!")
            break
        else:
            print("Opzione non valida. Riprova.")

menu()
