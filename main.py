from algorytmy.Algorytmy_procesow import fcfs, RR, koncowy_raportfc, koncowy_raport
from algorytmy.algorytmy_stron import fifo, LRU, strony
from generatory.generator import procesy
import pandas as pd
import os
if not os.path.exists('raporty'):
    os.makedirs('raporty')

ilosc = len(procesy)
fcfs(ilosc)
RR(ilosc)

# Zapis raportów z procesów
df1 = pd.DataFrame(koncowy_raportfc)
df2 = pd.DataFrame(koncowy_raport)
with pd.ExcelWriter('raporty/procesy_raport.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Raport FCFS', index=False)
    df2.to_excel(writer, sheet_name='Raport Round Robin', index=False)
ilosc=len(strony) #oblczenie ilosci stron
max_iloscstron=4 #maksymalna ilosc w pamieci ram
fifo_bledy=fifo(ilosc,max_iloscstron) #funkcja fifo
lru_bledy=LRU(ilosc,max_iloscstron) #funkcja LRU

# Zapis raportu z błędami stron
df3 = pd.DataFrame(strony)
with pd.ExcelWriter('raporty/procesy_raport.xlsx', mode='a', engine='openpyxl') as writer:
    df3.to_excel(writer, sheet_name='Raport Fifo i LRU', index=False)

print("Dane zapisane do raportów.")
print("Ilość błędów stron:")
print(f"fifo_bledy: {fifo_bledy}")
print(f"lru_bledy: {lru_bledy}")