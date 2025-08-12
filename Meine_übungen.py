# Ein ganz einfacher Taschenrechner

zahl1 = input("Erste Zahl eingeben: ")
zahl2 = input("Zweite Zahl eingeben: ")
operator = input("Operator (+, -, *, /) auswählen: ")

# Umwandeln in Zahlen
zahl1 = float(zahl1)
zahl2 = float(zahl2)

if operator == "+":
    ergebnis = zahl1 + zahl2
elif operator == "-":
    ergebnis = zahl1 - zahl2
elif operator == "*":
    ergebnis = zahl1 * zahl2
elif operator == "/":
    if zahl2 != 0:
        ergebnis = zahl1 / zahl2
    else:
        ergebnis = "Fehler: Division durch 0"
else:
    ergebnis = "Ungültiger Operator"

print("Ergebnis:", ergebnis)