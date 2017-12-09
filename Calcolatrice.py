while True:
    print("""
Benvenuto sulla calcolatrice!
Per iniziare indica cosa vuoi fare:

-Per un'addizione, digita 1;
-Per una sottrazione, digita 2;
-Per una moltiplicazione, digita 3;
-Per una divisione, digita 4;
-Per uscire dall'applicazione digita ESC.
""")
    operazione = input("Dopo aver digitato il numero premi INVIO" + " --> ")

    if operazione == "1":
       print("Hai scelto Addizione")
       x = float (input("Digita il primo numero:"))
       y = float (input("Digita il secondo numero:"))
       z = float (input("Digita il terzo numero(se non è presente digita 0):"))
       print("Il risultato è: " + str(x + y + z))
   
    elif operazione == "2":
       print("Hai scelto Sottrazione")
       x = float (input("Digita il primo numero:"))
       y = float (input("Digita il secondo numero:"))
       z = float (input("Digita il terzo numero(se non è presente digita 0):"))
       print("Il risultato è: " + str(x - y - z))
    elif operazione == "3":
       print("Hai scelto Moltiplicazione")
       x = float (input("Digita il primo numero:"))
       y = float (input("Digita il secondo numero:"))
       print("Il risultato è: " + str(x * y))
    elif operazione == "4":
       print("Hai scelto Divisione")
       x = float (input("Digita il primo numero:"))
       y = float (input("Digita il secondo numero:"))
       print("Il risultato è: " + str(x / y))
    elif operazione == "ESC" or operazione== "esc":
        print("Grazie e arrivederci!")
        break
    else:
        print("Scusa, non ho capito, potresti ripetere?")
        operazione = input("Dopo aver digitato il numero premi INVIO" + " --> ")
    loop = input("\nDesideri continuare ad usare l'applicazione? S/N ")
    if loop == "S" or loop == "s":
        print('''Sto tornando al Menù principale!''')
        continue
    elif loop == "N" or loop == "n":
        print("Grazie e arrivederci!")
        break
    else:
        print('''Grazie e arrivederci!''')
        break
