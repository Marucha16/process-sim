import numpy as np
def generator(max_przyjscia,max_trwanie,ilosc):
    przyjscie = np.random.randint(1, max_przyjscia + 1, size=ilosc) #losowy czas pojawiania sie
    trwanie = np.random.randint(1, max_trwanie + 1, size=ilosc) #dane losowe (czas trwania)
    trwanie=np.full(ilosc, 12) #dane stałe jesli sie chce
    procesy =[] #stworzenie listy
    for x in range(ilosc): #iterowanie by dodawac slowniki do listy
        proces = {
            'numer_procesu': x+1,
            'czas_przyjscia': int(przyjscie[x]),
            'czas_trwania': int(trwanie[x]),
            'czas_oczekiwania': 0
        }
        procesy.append(proces)#dodanie slownika
    procesy.sort(key=lambda x:x['czas_przyjscia']) #sortowanie w zaleznosci od czasu przyjscia
    for x in range(ilosc):
        procesy[x]['numer_procesu']=x+1 #własciwe numerowanie

    return procesy
procesy=generator(10,20,20) #dobieranie danych