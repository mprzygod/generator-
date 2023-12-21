
import random
#pierwszy program

znaki="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
licznik = -1
for i in znaki:
    licznik += 1
dlugiscHasla = int(input("ile znaków ma mieć hasło?"))
haslo = ""
for i in range(dlugiscHasla):
    haslo += znaki[random.randint(0,licznik)]
print(haslo)