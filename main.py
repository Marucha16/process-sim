from algorytmy.planowanie_procesow import fcfs, RR, koncowy_raportfc, koncowy_raport
from algorytmy.zarzadzanie_stronami import fifo, LRU, strony
from generatory.generator_procesow import procesy
import pandas as pd

ilosc = len(procesy)
fcfs(ilosc)
RR(ilosc)

# Zapis raportów z procesów
df1 = pd.DataFrame(koncowy_raportfc)
df2 = pd.DataFrame(koncowy_raport)
with pd.ExcelWriter('raporty/procesy_raport.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Raport FCFS', index=False)
    df2.to_excel(writer, sheet_name='Raport Round Robin', index=False)

# Zapis raportu z błędami stron
df3 = pd.DataFrame(strony)
with pd.ExcelWriter('raporty/procesy_raport.xlsx', mode='a', engine='openpyxl') as writer:
    df3.to_excel(writer, sheet_name='Raport Fifo i LRU', index=False)

print("Dane zapisane do raportów.")