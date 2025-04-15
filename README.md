# 🎭 Simulatore Teatro - Python OOP

Benvenuto nel **Simulatore di Teatro**! Questo progetto in Python simula un sistema di prenotazione di posti in un teatro, con gestione di **posti VIP**, **posti standard**, funzionalità extra come **servizi VIP**, **bar**, e un **menu interattivo** per l'utente.

## 🛠 Tecnologie Utilizzate

- Python 3.x
- Programmazione Orientata agli Oggetti (OOP)
- Terminale / Console interattiva

## 📦 Funzionalità

### 📌 Classi Implementate

#### `Posto`
- Attributi: numero, fila, stato (occupato/libero)
- Metodi: `prenota()`, `libera()`, `descrizione()`

#### `PostoVIP` *(deriva da Posto)*
- Attributi: saldo, servizi extra
- Metodi aggiuntivi: `bonus_vip()`, `bar()`, prenotazione con servizi

#### `PostoStandard` *(deriva da Posto)*
- Attributi: costo
- Prenotazione con maggiorazione se fatta online

#### `Teatro`
- Attributi: lista dei posti
- Metodi: aggiunta posto, prenotazione, stampa posti occupati

### 🧭 Menu Interattivo

- Aggiungi posto VIP
- Aggiungi posto standard
- Prenota posto
- Mostra posti occupati
- Accedi al bar per i VIP
- Ricarica saldo VIP
- Esci

