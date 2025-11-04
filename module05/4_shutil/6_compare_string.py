w1 = "Straße"
w2 = "STRASSE"
print(w1.lower() == w2.lower())  # False
print(w1.casefold() == w2.casefold())  # True
