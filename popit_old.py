import time
import datetime

# Baner:
# Q, W, E, D, S, A
# ...
qvh3 = "QWEDSA"
qvh = "QWERTYUIOPLKJHGFDSAZXCVBNM"
numbers = "|1234567890+\\QWERTYUIOPÅ¨'ASDFGHJKLØÆZXCVBNM,.-"

lvls = {
    1: qvh3,
    2: qvh,
    3: numbers,
}

if __name__ == '__main__':
    print("===========================================")
    print("Pop It")
    print("===========================================")
    
    print(
    """
    Hvordan spille:
    1. Trykk på 'enter' for å starte.
    2. Trykk på knappene i valgt nivå (etter >>> ).
    3. Trykk på 'enter' for å avslutte.
    """)
    
    # START SPILL:
    
    
    # velge bane
    print("Tilgjengelige nivåer:")
    
    # print(f"(1): {' - '.join(qvh3)}")
    for k,v in lvls.items():
        print(f"({k}): {' '.join(v)}")
    lvl = int( input("\nVelg nivå nr: ") )
    
    
    if lvl in lvls:
        print(f"Du har valgt nivå {lvl}")
        print( lvls[lvl].upper() )
    else:
        print("Du har ikke valgt nivå...")
        exit()
    
    # start spill: trykk 'enter' 
    
    input("Trykk 'enter' for å starte ")
    
    # start tidspunkt
    start = time.time()
    
    # spiller man, trykker på knapper i banen
    attempt = input("\n>>> ")
    # ferdig: trykk på 'enter'
    
    # slutt tidspunkt
    end = time.time()
    
    # sjekk at spillerer trykket riktig
    # hvis nei: du feilet, prøv igjen
    if attempt.upper() != lvls[lvl]:
        print("GAME OVER!")
        print("Du klarte det ikke, prøv igjen")
        exit()
        
    # hvis ja: fortsett
    print("\nGrattis, du klarte det!")
    # tidsbruk = slutt - start
    elapsed = datetime.timedelta(seconds=end-start)
    
    # printe resultatet
    millis = str(elapsed).split(":")[-1].split(".")[-1]
    # print(f"Du brukte {elapsed} sekunder")
    print(f"Du brukte {elapsed.seconds}.{millis} sekunder")
    
    print()
    print("===========================================")
    print("FERDIG!")
    print("===========================================")
    
    
    
    
    
    