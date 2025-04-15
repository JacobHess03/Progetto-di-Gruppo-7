class Posto:
    def __init__(self, numero, fila, online = True):
        self.__numero = numero
        self.__fila = fila
        self.__occupato = False
        self.online = online

    def prenota(self):
        if not self.__occupato:
            self.__occupato = True
            print(f"Posto {self.__fila}-{self.__numero} prenotato con successo.")
        else:
            print(f"Posto {self.__fila}-{self.__numero} è già occupato.")

    def libera(self):
        if self.__occupato:
            self.__occupato = False
            print(f"Posto {self.__fila}-{self.__numero} liberato.")
        else:
            print(f"Posto {self.__fila}-{self.__numero} non era occupato.")

    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def is_occupato(self):
        return self.__occupato

    def descrizione(self):
        stato = "Occupato" if self.__occupato else "Libero"
        return f"Posto {self.__fila}-{self.__numero} - {stato}"



class PostoVIP(Posto):
    def __init__(self, numero, fila, saldo, online):
        super().__init__(numero, fila, online)
        self.__servizi_extra = True
        self.__saldo = saldo
        online = True

    def prenota(self):
        if not self.is_occupato():
            super().prenota()
            if self.online:
                print(f"Servizi VIP attivati con prenotazione online")
            else:
                print(f"Posto VIP {self.get_fila()}-{self.get_numero()} è già occupato.")
            
    def bonus_vip(self):
        bonus = 10 # bonus di 10 
        if self.__servizi_extra:
            self.__saldo += bonus
        else:
            self.__servizi_extra = False
    
    def bar(self, menu_bar):
            menu_bar = {"Caffè" : 1.20, "Cappuccino": 1.80, "Cornetto": 1.00, "Succo d'arancia": 2.00}
        
            nome = input("Inserisci il nome del prodotto: ").strip()
            for key, values in menu_bar.items():
                if key == nome:
                    self.__saldo -= values
                    print("Prodotto acquistato.")
                    return
                
            print("Prodotto non trovato.")




class PostoStandard(Posto):
    def __init__(self, numero, fila, costo, online):
        super().__init__(numero, fila, online)
        self.__costo = costo
        online = False

    def prenota(self):
        if not self.is_occupato() and self.online:
            costo_finale  = self.__costo * 1.1 # aumentiamo del 10 %
            print(f"Il costo della prenotazione è di €{costo_finale} aumentato del 10%")
            super().prenota()
        else:
            print(f"Posto Standard {self.get_fila()}-{self.get_numero()} è già occupato.")
            
    

class Teatro:
    def __init__(self):
        self.__posti = []

    def aggiungi_posto_vip(self):
        fila = input("Inserisci la fila del posto VIP: ").strip().upper()
        numero = int(input("Inserisci il numero del posto VIP: "))
        saldo = float(input("Inserisci il saldo iniziale del cliente VIP: "))
        posto = PostoVIP(numero, fila, saldo, online=True)
        self.__posti.append(posto)
        print("Posto VIP aggiunto con successo.")

    def aggiungi_posto_standard(self):
        fila = input("Inserisci la fila del posto standard: ").strip().upper()
        numero = int(input("Inserisci il numero del posto standard: "))
        costo = float(input("Inserisci il costo base del posto: "))
        posto = PostoStandard(numero, fila, costo, online=True)
        self.__posti.append(posto)
        print("Posto Standard aggiunto con successo.")

    def prenota_posto(self):
        fila = input("Inserisci la fila del posto da prenotare: ").strip().upper()
        numero = int(input("Inserisci il numero del posto da prenotare: "))
        for posto in self.__posti:
            if posto.get_fila() == fila and posto.get_numero() == numero:
                posto.prenota()
                return
        print("Posto non trovato.")

    def mostra_posti_occupati(self):
        trovati = False
        for posto in self.__posti:
            if posto.is_occupato():
                print(posto.descrizione())
                trovati = True
        if not trovati:
            print("Nessun posto è attualmente occupato.")

    def bonus_vip_a_tutti(self):
        for posto in self.__posti:
            if isinstance(posto, PostoVIP):
                posto.bonus_vip()
        print("Bonus VIP accreditati.")

    def usa_bar_vip(self):
        fila = input("Fila del VIP: ").strip().upper()
        numero = int(input("Numero del VIP: "))
        for posto in self.__posti:
            if posto.get_fila() == fila and posto.get_numero() == numero:
                if isinstance(posto, PostoVIP):
                    posto.bar({})
                    return
        print("Posto VIP non trovato.")
        
        



def menu_teatro():
    teatro = Teatro()
    while True:
        print("\n--- MENU TEATRO ---")
        print("1. Aggiungi posto VIP")
        print("2. Aggiungi posto Standard")
        print("3. Prenota un posto")
        print("4. Mostra posti occupati")
        print("5. Aggiungi bonus VIP")
        print("6. Ordina dal bar (VIP)")
        print("0. Esci")

        scelta = input("Seleziona un'opzione: ")

        match scelta:
            case "1":
                teatro.aggiungi_posto_vip()
            case "2":
                teatro.aggiungi_posto_standard()
            case "3":
                teatro.prenota_posto()
            case "4":
                teatro.mostra_posti_occupati()
            case "5":
                teatro.bonus_vip_a_tutti()
            case "6":
                teatro.usa_bar_vip()
            case "0":
                print("Chiusura del sistema teatro.")
                break
            case _:
                print("Scelta non valida.")
                
menu_teatro()
