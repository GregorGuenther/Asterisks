def pattern1() :
    SIZE = 9
    print()
    print('Ausgabe Zifern in Rechsteck:\n')
    for zeile in range(SIZE) :
        print(zeile + 1, '  ', end='')
        for spalte in range(SIZE) :
            print('',spalte ,end='') 
        print()        
    print()
def pattern2() :
    SIZE = 9
    print()
    print('Ausgabe Rechtseck:\n')
    for zeile in range(SIZE) :
        print(zeile + 1, '  ', end='')
        for spalte in range(SIZE) :
            print(' *', end='')
        print() 
    print()
def pattern3() :
    SIZE = 9
    print('Viereck:\n')
    for zeile in range(SIZE) :
        print(zeile, '  ', end='')
        for spalte in range(SIZE) :
            if     spalte == 0 or spalte == 8 \
                or zeile == 0 or zeile == 8 :
                print(' *', end='') 
            else :
                print('  ', end='') 
        print()
    print()
def pattern4() :
    SIZE = 9
    print('Ausgabe von Links Oben nach Recht unten:\n')
    for zeile in range(9) :
        print(zeile, '  ', end='')
        for spalte in range(9) :
            if zeile == spalte :
                print(' *', end='')
            else :
                print(' ', end='') 
        print()
    print()
def pattern5() :
    SIZE = 9
    print('Ausgabe von Rechts Oben nach Links unten:\n')
    for zeile in range(SIZE) :
        print(zeile, '  ', end='')
        for spalte in range(SIZE) :
            if zeile + spalte == 8 :
                print(' *', end='')
            else :
                print(' ', end='') 
        print()
    print()
def pattern6() :
    SIZE = 9
    print('Ein \" X " :\n')
    for zeile in range(9) :
        print(zeile, ' ', end='')
        for spalte in range(9) :
            if zeile == spalte or zeile + spalte == 8 :
                # if zeile == spalte            (Alternative)
                # or zeile == 9 -spalte -1 :
                print(' *', end='')
            else :
                print('  ', end='') 
        print()
    print()
def pattern7() :
    SIZE = 9
    print('Ein \" + " :\n')
    for zeile in range(9) :
        print(zeile, '  ', end='')
        for spalte in range(9) :
            if zeile == 4 or spalte == 8 :
                print(' *', end='')
            else :
                print(' ', end='') 
        print()
    print()
def pattern8() :
    SIZE = 9
    print('Nord | Süd | West | Ost:\n')
    for zeile in range(SIZE) :
        print(zeile, '  ', end='')
        for spalte in range(SIZE) :
            if     zeile == 0 and spalte == 4 \
                or zeile == 4 and spalte == 0 \
                or zeile == 4 and spalte == 8 \
                or zeile == 8 and spalte == 4 :
                print(' *', end='') 
            else :
                print(' ', end='') 
        print()
    print()
def pattern9() :
    SIZE = 9
    print('Vier Punkte Aussen:\n')
    for zeile in range(SIZE) :
        print(zeile, '  ', end='')
        for spalte in range(SIZE) :
            if     zeile == 0 and spalte == 0 \
                or zeile == 0 and spalte == 8 \
                or zeile == 8 and spalte == 0 \
                or zeile == 8 and spalte == 8 \
                :
                print(' *', end='') 
            else :
                print(' ', end='') 
        print()
    print()
def pattern10() :
    SIZE = 9
    print('Punkt Unten Rechts:\n')
    for zeile in range(9) :
        print(zeile, '  ', end='')
        for spalte in range(9) :
            if     zeile == 0 and zeile == 8 \
                or zeile == 8 and spalte == 8 \
                :
                print(' *', end='') 
            else :
                print(' ', end='') 
        print()
    print()
def pattern11() :
    SIZE = 9
    print('Punkt Oben Links:\n')
    for zeile in range(9) :
        print(zeile, '  ', end='')
        for spalte in range(9) :
            if     zeile == 8 and zeile == 0 \
                or zeile == 0 and spalte == 0 \
                :
                print(' *', end='') 
            else :
                print(' ', end='') 
        print()
    print()
def pattern12() :
    SIZE = 9
    print('Halbe Tannenbaum:\n')
    for zeile in range(9) :
        print(zeile, '  ', end='')
        for spalte in range(zeile+1) :
                print(' *', end='') 
        print()
    print()
def pattern13() :
    SIZE = 9
    print('Halbe Umgekehrte Tannenbaum:\n')
    for zeile in range(9) :
        print(zeile, '  ', end='')
        for spalte in range(9-zeile) :
                print(' *', end='') 
        print()
    print()
def pattern14() :
    SIZE = 9
    for y in range(SIZE) :
        for x in range(SIZE) :
            if y < (SIZE / 2) and x < (SIZE / 2) :
                print(' *', end='')
            elif y == 4 or x == 4 :
                print(' *', end='')
            elif y > (SIZE / 2) and x > (SIZE / 2) :
                print(' *', end='')
            else :
                print('  ', end='')    
        print()
def pattern15() :
    SIZE = 9
    print('Balken\n')
    for zeile in range(SIZE):
        print(zeile, '  ', end='')
        for spalte in range (SIZE):
            if      zeile == 0 and spalte < 2 \
                or  zeile == 1 and spalte < 3 \
                or  zeile == 2 and spalte > 0 and spalte < 4 \
                or  zeile == 3 and spalte > 1 and spalte < 5 \
                or  zeile == 4 and spalte > 2 and spalte < 6 \
                or  zeile == 5 and spalte > 3 and spalte < 7 \
                or  zeile == 6 and spalte > 4 and spalte < 8 \
                or  zeile == 7 and spalte > 5 and spalte < 9 \
                or  zeile == 8 and spalte > 6:
                print(" *", end='')
            else: 
                print("  ", end='')
        print()
    print()
def pattern16() :
    SIZE = 9
    print('Verschobene Dreiecke\n')
    for zeile in range(SIZE):
        print(zeile, '  ', end='')
        for spalte in range (SIZE):
            if      zeile < 5 and spalte == 0 \
                or  zeile < 5 and zeile > 0 and spalte == 1 \
                or  zeile < 5 and zeile > 1 and spalte == 2 \
                or  zeile < 5 and zeile > 2 and spalte == 3 \
                or  zeile < 6 and zeile > 4 and spalte == 5 \
                or  zeile < 7 and zeile > 4 and spalte == 6 \
                or  zeile < 8 and zeile > 4 and spalte == 7 \
                or  zeile < 9 and zeile > 4 and spalte == 8 \
                or  zeile < 5 and zeile > 3  and spalte < 9 :
                print(" *", end='')
            else: 
                print("  ", end='')
        print()
    print()

bContinue = True    # Dauerschleife
while (bContinue) :
    print()
    print('-----------------------------------------------')
    print("1.Ausgabe Zifern in Rechsteck\n", end='')
    print("2.Ausgabe Rechtseck\n", end='')
    print("3.Ausgabe Viereck\n", end='')
    print("4.Ausgabe von Links Oben nach Recht unten\n", end='')
    print("5.Ausgabe von Links Oben nach Recht unten\n", end='')
    print("6.Ausgabe X \n", end='')
    print("7.Ausgabe Plus\n", end='')
    print("8.Ausgabe Nord | Süd | West | Ost\n", end='')
    print("9.Ausgabe Vier Punkte Aussen\n", end='')
    print("10.Ausgabe Punkt Unten Rechts\n", end='')
    print("11.Ausgabe Punkt Oben Links\n", end='')
    print("12.Ausgabe Halbe Tannenbaum \n", end='')
    print("13.Ausgabe Halbe Umgekehrte Tannenbaum\n", end='')
    print("14.Ausgabe Versätzte Vieräcke \n", end='')
    print("15.Ausgabe Balken \n", end='')
    print("16.Ausgabe Verschobene Dreiecke\n", end='')
    print('\nx = Exit:  ', end='')
    
    x = input()

    if x == "1" :
        pattern1()
    elif x == "2" :
        pattern2()
    elif x == "3" :
        pattern3()
    elif x == "4" :
        pattern4()
    elif x == "5" :
        pattern5()
    elif x == "6" :
        pattern6()
    elif x == "7" :
        pattern7()
    elif x == "8" :
        pattern8()
    elif x == "9" :
        pattern9()
    elif x == "10" :
        pattern10()
    elif x == "11" :
        pattern11()
    elif x == "12" :
        pattern12()
    elif x == "13" :
        pattern13()
    elif x == "14" :
        pattern14()
    elif x == "15" :
        pattern15()
    elif x == "16" :
        pattern16()
    elif x == "x":
        bContinue = False
    else :
        print(' Falsche Eingabe: "' + x + '"')

print('\nTschüss')



