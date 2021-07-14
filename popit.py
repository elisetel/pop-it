import time
import datetime
import winsound

# Baner:
qvh3 = "QWEDSA"
qvh = "QWERTYUIOPLKJHGFDSAZXCVBNM"
numbers = "|1234567890+\\QWERTYUIOPÅ¨'ASDFGHJKLØÆZXCVBNM,.-"

# rekkefølgen er viktig
lvls = [
    qvh3,
    qvh,
    numbers,
]

lvls = {i:lvl for i,lvl in enumerate(lvls, 1)}

howto = """
    Hvordan spille:
    1. Trykk på 'enter' for å starte.
    2. Trykk på knappene i valgt nivå (etter >>> ).
    3. Trykk på 'enter' for å avslutte.
"""

def show_lvls(delimiter=" "):
    global lvls
    for k,v in lvls.items():
        print(f"({k}): {delimiter.join(v)}")
        
        
def countdown(n, sound=False):
    for x in range(n, 0, -1):
        if sound: 
            winsound.Beep(1000, 1000)
        else:
            time.sleep(1)
        print(x)
    if sound: winsound.Beep(2000, 1200)
    

def valid_lvl(lvl, exit=True):
    global lvls
    if lvl not in lvls:
        if exit:
            print("Du har ikke valgt et gyldig nivå...")
            exit()
        return False
    return True

def valid_attempt(attempt, lvl):
    global lvls
    return attempt.upper() == lvls[lvl]
    

def game():
    print("="*100)
    print("\tPop It")
    print("="*100)
    
    print(howto)
    
    # vis nivåer til spilleren som velger
    print("Tilgjengelige nivåer:")
    show_lvls(delimiter=" ")
    lvl = int( input("\nVelg nivå nr: ") )

    # sjekk gyldig nivå
    valid_lvl(lvl, exit=True)
    
    input("\nTrykk 'enter' for å starte ")
    countdown(3, sound=True)
    
    start = time.time()
    attempt = input("\n>>> ")
    end = time.time()
    
    # sjekk at spillerer trykket riktig
    if not valid_attempt(attempt, lvl):
        print()
        print("="*100)
        print("\tGAME OVER!")
        print("\tDu klarte det ikke, prøv igjen!")
        print("="*100)
        exit()

    elapsed = datetime.timedelta(seconds=end-start)
    millis = str(elapsed).split(":")[-1].split(".")[-1]
    
    print()
    print("="*100)
    print(f"\t{elapsed.seconds}.{millis} sekunder")
    print("="*100)
    
    

if __name__ == '__main__':
    game()
    # countdown(3, sound=True)
    # print(">>> ")
    
    
    
    