from generatory.generator_stron import strony
from collections import deque
def fifo(ilosc,max_iloscstron):
    bledy_stron=0 #zliczanie bledow stron
    dodatek=0 #zmienna do petli i indexu
    kolejka = deque() #tworzenie kolejki
    while (dodatek < ilosc):
        if not any(id['numer_id_strony'] == strony[dodatek]['numer_id_strony'] for id in kolejka): #sprawdzanie czy przychodzaca strona jest w kolejce
            if len(kolejka) >= max_iloscstron:#sprawdzenie czy mozna zaladowac jakas strone bez usuwania innej
                kolejka.popleft() #jesli nie usuwa pierwsza ktora przyszla
                kolejka.append(strony[dodatek]) #dodaje na koniec nastepna
                bledy_stron=bledy_stron+1 #zliczanie bledow stron
            else:
                kolejka.append(strony[dodatek]) #dodanie strony po prostu jak wolne miejsce
                bledy_stron = bledy_stron + 1 #dodanie mimo wszystko bledu
        dodatek = dodatek + 1 #dodanie do zmiennej sluzacej do iteracji
    return bledy_stron #zwrocenie wartosci bledow stron
def LRU(ilosc,max_iloscstron):
    dodatek = 0 #tworzenie zmiennej iteracyjnej
    kolejka = deque() #stworzenie kolejki
    bledy_stron=0 #zmienna do bledow stron
    while (dodatek < ilosc): #sprawdzenie czy nie wyszlismy poza index
        if not any(stron['numer_id_strony'] == strony[dodatek]['numer_id_strony'] for stron in kolejka): #sprawdzenie czy w kolejce nie ma juz zaladowanej strony
            bledy_stron = bledy_stron + 1 #zliczanie bledow stron
            if len(kolejka) >= max_iloscstron: #sprawdzenie czy kolejka jest pelna
                        kolejka.popleft() #wyrzucenie pierwszej strony w kolejce
                        kolejka.append(strony[dodatek]) #dodanie na koniec strony
            else:
                kolejka.append(strony[dodatek]) #po prostu dodanie strony bo pusta
        else:
            for str1 in kolejka: #iterowanie po kolejce
                if(str1['numer_id_strony']==strony[dodatek]['numer_id_strony']): #sprawdzenie na ktroym miejscu jest strona
                    kolejka.remove(str1) #usuniecie jej z tego miejsca i dodanie na koniec
                    break
            kolejka.append(strony[dodatek])#dodanie na konice
        dodatek=dodatek+1 #zmienianie iteracji na kolejna
    return bledy_stron #zwrocenie bledow stron

