from collections import deque #biblioteka z kolejka
from  generatory.generator import procesy #modul z generatorem
from copy import deepcopy #do skopiowania listy
koncowy_raportfc = deepcopy(procesy) #kopiowanie
koncowy_raport= deepcopy(procesy)#kopiowanie
def fcfs(ilosc):
    czas=1 #zmienna z czasem
    dodatek=0 #ilosc petli -1 i za rowno index listy
    kolejka = deque()#stworzenie kolejki
    while(dodatek < ilosc): #petla do czasu skonczenia sie procesow
        while(czas>=procesy[dodatek]["czas_przyjscia"]): #sprawdzanie czy mozna dodac proces
            kolejka.append(procesy[dodatek]) #dodanie procesu
            dodatek=dodatek+1 #zmienianie o jeden proces do iterowania
            if(ilosc==dodatek): #sprawdzanie czy nie musimy wyjsc przypadkiem w while zeby nie wyjsc za index
                    break #wyjscie
        if (ilosc != dodatek):#sprawdzanie czy nie wyszlismy poza liste
            if (czas < procesy[dodatek]["czas_przyjscia"] and not kolejka): #jesli kolejka pusta i czas przyjscia mniejszy  to dziala
                czas=procesy[dodatek]["czas_przyjscia"] #zmienianie czasu jak nic sie nie dzieje
        while kolejka: #jesli jest cos w kolejce to wchodzimy do while
            proces=kolejka.popleft() #wyrzucanie procesu z poczatku kolejki
            czas=czas+proces['czas_trwania'] #zasymulowanie procesu(dodanie czasu trwania)
            nazwa = proces['numer_procesu'] #nazwa(numer procesu) do if
            for x in range(len(procesy)): #iterowanie po liczbie procesow
                if (procesy[x]['numer_procesu'] == nazwa): #sprawdzanie czy to jest proceso ktory nam chodzi
                    koncowy_raportfc[x]['czas_oczekiwania'] = czas - procesy[x]['czas_przyjscia'] - koncowy_raportfc[x]['czas_trwania'] #dodawanie czasu ile spedzil dany proces w kolejce
def RR(ilosc):
    czas=1 #zmienna z czasem
    dodatek=0 #zmienna ile iteracji i indexowanie
    kolejka = deque() #tworzenie kolejki
    kwant_czasu=4 #czas ile czasu ma byc poswiecane na proces maksymalnie za pierwszym wejsciem
    while (dodatek < ilosc): #petla do czasu skoneczenia sie procesow
        while (czas >= procesy[dodatek]["czas_przyjscia"]): #petla do dodawanie procesow do kolejki jesli nadszedl ich czas
            kolejka.append(procesy[dodatek]) #dodawanie procesow do kolejki
            dodatek = dodatek + 1 #zmienianie na nastepny proces do dodania
            if (ilosc == dodatek): #moment by wyjsc z petli by nie wyjsc za index listy
                break
        if (ilosc != dodatek): #sprawdzenie czy nie jestesmy poza indexem
            if (czas < procesy[dodatek]["czas_przyjscia"] and not kolejka): #w razie gdy kolejka pusta i nie mozna dodac zadnego procesu bo jeszcze nie przyszedl
                czas=procesy[dodatek]["czas_przyjscia"] #zasymulowanie mijania czasu gdy nie ma zadnego procesu w kolejce
        while kolejka: #petla dziala jak cos jest w kolejce
            proces=kolejka.popleft() #wyrzucanie pierwszego procesu
            if(proces['czas_trwania'] <= kwant_czasu): #sprawdzanie czy maksymalna czas na wykonanie w jednej petli sie zgadza
                czas=czas+proces['czas_trwania'] #dodanie tego czasu
                nazwa=proces['numer_procesu'] #zmienna pomocnicza z numerem procesu
                for x in range(len(procesy)): #iterowanie po liczbie procesow
                    if(procesy[x]['numer_procesu']==nazwa): #sprawdzanie czy jestemy na procesie o ktroy nam chodzi
                        koncowy_raport[x]['czas_oczekiwania']=czas-koncowy_raport[x]['czas_przyjscia']-koncowy_raport[x]['czas_trwania'] #dodawanie czasu oczekiwania do tego procesu
            else:
                czas=czas+kwant_czasu #tutaj dodajemy maksymalny czas jaki mozemy przeznaczyc na proces w jednej petli
                proces['czas_trwania']=proces['czas_trwania']-kwant_czasu #odejmujemy czas by moc wrzucic na koniec kolejki
                if (ilosc != dodatek): #sprawdzamy czy nie wyszlismy poza index
                    while (czas >= procesy[dodatek]["czas_przyjscia"]): #petla ktora ponownie dodaje zeby najpierw wpadaly do kolejki procesy ktore maja przyjsc a dopiero potem ten ktory przedchwila dzialal
                        kolejka.append(procesy[dodatek]) #dodanie procesow ktore przyszly
                        dodatek = dodatek + 1 #dodanie do indexu i petli
                        if (ilosc == dodatek): #sprawdzenie czy nie wyszlismy poza zakres
                            break
                    if (ilosc != dodatek): #sprawdzenie czy nie wyszlismy poza zakres
                        if(czas < procesy[dodatek]["czas_przyjscia"] and not kolejka): #sprawdzenie czy zadne procesy nie sa w kolejce i nie maja zamiaru wejs do niej
                            czas = procesy[dodatek]["czas_przyjscia"] #symulowanie mijania czasu
                kolejka.append(proces)#dodanie procesu ktory juz raz dzialal ale sie nie zakonczyl na koniec kolejki
            if(ilosc!=dodatek): #sprawdzenie czy nie wszyslismy poza zakres
                if(czas >= procesy[dodatek]["czas_przyjscia"]): #w razie gdy procesu maja mozliwosc wejscia do kolejki
                    break
