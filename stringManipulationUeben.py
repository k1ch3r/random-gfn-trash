# string ist ein datentyp.
# ein string beinhaltet zeichen und behandelt diese NUR als zeichen.

# wir legen hier eine variable als leeren string fest

unserString = ''
print(unserString)

# das hier geht nicht weil python versucht eine mathematische rechnung
# mit zahlen zu machen und als zweiten summand eine zahl
# und keinen string erwartet:

unsereZahl = 5

# bearbeiteterString = unsereZahl + unserString

# variablen koennen manipuliert werden.
# eine einfache art bestehende strings zu manipulieren ist concatenation.
# das ist der name fuer den vorgang einen string
# mit einem weiteren string zu erweitern.
# dabei wird der hinzugefuegte string hinten an den
# bestehenden string angefuegt.

# probier das hier mal aus und haenge 'hallo' an unseren string an:

unserString = unserString + ''
print(unserString)

# jetzt fuege mal leerzeichen und welt an den selben string an

unserString