import numpy as np
def generator(max_przyjscia,ktora_strona,ilosc):
    przyjscie = np.random.randint(1, max_przyjscia + 1, size=ilosc) #losowanie czasu przyjscia
    strona = np.random.randint(1, ktora_strona + 1, size=ilosc) #losowanie id strony
    strona = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5] #tutaj dane na cele sprawozdania
    strony =[] #stworzenie listy
    for x in range(ilosc): #iterowanie by dodac slowniki do listy
        strona1 = {
            'numer_przyjscia': x+1,
            'czas_przyjscia': int(przyjscie[x]),
            'numer_id_strony': int(strona[x])
        }
        strony.append(strona1) #dodawanie
    strony.sort(key=lambda x:x['czas_przyjscia']) #sortowanie wzgledem czasu przyjscia strony
    for x in range(ilosc):
        strony[x]['numer_przyjscia']=x+1 #zamienenie numeru przyjscia by numer byl uszeregowany od czasu przyjscia
        strony[x]['numer_id_strony']=strona[x] #to na cele sprawozdania
    return strony
strony=generator(25,10,12) #dobieranie danych