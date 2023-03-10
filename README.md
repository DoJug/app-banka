# app-banka

Pozdrav!

Ovo je moja prva aplikacija koja je, za razliku od prijašnjih (guessing game, tic tac toe...), podijeljena na GitHubu. 
Aplikacija sadržava sljedeće funkcionalnosti:
  1. Otvaranje računa banke
  2. Prikaz stanja računa
  3. Prikaz prometa po računu
  4. Polog novca na račun
  5. Podizanje novca s računa
  6. Povratak u log-in screen
  7. Izlazak iz aplikacije.

Aplikacija se bazira na tome da prilikom početnog pokretanja, ukoliko je korisnik sadašnji korisnik banke, unosi svoj broj kartice koji mu služi kao "autorizacija" i na taj način pristupa funkcionalnostima kao što su uvid u stanje računa, prikaz prometa i sl . Ako korisnik nije sadašnji klijent banke, otvara račun u banci i upisuje svoje osnovne podatke (ime i prezime, oib, početni ulog novca kod otvaranja računa). 

Registrirani korisnici zapisuju se u dictionary (rječnik) pod nazivom "banka".
Svaka aktivnost vezana za transakcije (početni polog novca, podizanje novca s računa ili polog novca na račun) zapisuje se u dictionary (rječnik) pod nazivom "transakcije".

Hope you like it!
