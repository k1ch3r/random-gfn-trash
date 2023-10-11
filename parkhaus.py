Ausgabestatus = ['Parkhaus belegt', 'Parkhaus frei', 'Parkhaus gesperrt']

def status_anzeigen(anzahl_parkplaetze_belegt, eingang_frei, ausgang_frei, vermietet):

    Auslastung = anzahl_parkplaetze_belegt / 500

    if (eingang_frei == False or ausgang_frei == False) or vermietet == True:
        print(Ausgabestatus[2])
    elif Auslastung > 0.95:
        print(Ausgabestatus[0])
    else:
        print(Ausgabestatus[1])

# testen

# testcase vom fall
# anzahl_parkplaetze_belegt = 330, eingang_frei = True, ausgang_frei = True, vermietet = False
print('Testcase Aufgabenstellung:')
status_anzeigen(330, True, True, False)

# eingang versperrt
print('Testcase Eingang versperrt:')
status_anzeigen(200, False, True, False)

# vermietet
print('Testcase vermietet:')
status_anzeigen(100, True, True, True)

# ausgelastet
print('Testcase ausgelastet:')
status_anzeigen(497, True, True, False)