Tema de project: Aplicatie Django de retete culinare.

Dezvolta o aplicatie Django, care sa contina urmatoarele functionalitati:
- Un sistem de autentificare utilizatori
- Un sistem de creare de retete culinare, editare reteta, stergere reteta.
- O pagina web care sa afiseze toate retetele culinare, sortate in ordine alfabetica.
- O pagina web care sa afiseze toate retele, sortate dupa data de creare.
- Doar un utilizator autentificat poate sa creeze sau sa editeze retete. Retetele se vor putea vedea chiar si daca nu este utilizatorul autentificat.
- Baza de date folosita poate fi sqlite3.

O reteta contine:
- Titlu (string)
- Descrierea retetei (string)
- Data de adaugare (string, folositi datetime pentru conversie)
- Timp de gatire (string)

Fiecare reteta apartine unui utilizator, create o legatura one-many in baza de date.
Scrieti teste unitare pentru partea de autentificare, CRUD reteta, si sortare retete, si orice functii utilitare pe care le mai folositi. Sa aveti cel putin 5 teste.

Proiectul o sa-l uploadati pe github, si puneti link-ul acestui proiect pe platforma, in sectiunea Tema Finala.
Sa aveti si un fisier readme.md cu detalii despre cum se instaleaza proiectul, paginile web incluse, si cum se ruleaza acest proiect.
Sa aveti si fișierul requirements.txt cu dependențele proiectului.

Pentru cei care vor sa lucreze la un proiect diferit, proiectul trebuie sa contina:
Sistemul de autentificare utilizatori.
Cel putin un model de django.db.models.
Cel putin doua pagini web care listeaza informatii stocate in baza de date.
O legatura one-many in baza de date, de exemplu intre User si modelul vostru ales.
Cel putin 5 teste unitare.


/ – Pagina principală, afișează lista de rețete.
/recipe/add/ – Form pentru adăugarea unei noi rețete.
/recipe/<int:id>/edit/ – Form pentru editarea unei rețete existente.
/recipe/<int:id>/delete/ – Ștergerea unei rețete.
/recipe/<int:id>/ – Pagina de detalii a unei rețete.
/login/ – Pagina de autentificare.
/logout/ – Redirecționare pentru delogare.




















e) Teste Unitare
Proiectul trebuie să includă teste unitare pentru a verifica funcționalitatea aplicației. Testele trebuie să fie implementate folosind framework-ul Django TestCase și să acopere următoarele scenarii:

Teste pentru Modelul Rețetă

Verificarea creării unei rețete valide (cu toate câmpurile corect completate).

Verificarea limitelor câmpurilor (de exemplu, lungimea minimă pentru titlu).

Teste pentru Vederi (Views)

Test pentru afișarea listei de rețete: Verificarea că ruta / returnează status code 200 și afișează toate rețetele existente.

Test pentru adăugarea unei rețete: Verificarea că utilizatorii autentificați pot adăuga rețete și că după trimiterea formularului datele sunt salvate în baza de date.

Test pentru acces restricționat: Verificarea că utilizatorii neautentificați nu pot accesa rutele de adăugare, editare sau ștergere.

Test pentru ștergerea unei rețete: Verificarea că ștergerea unei rețete funcționează corect și că aceasta nu mai există în baza de date.

Teste pentru Formulare

Verificarea validării câmpurilor din formularul de adăugare/editare rețetă (de exemplu, titlu obligatoriu, timp de gătit numeric pozitiv).

f) Interfața Utilizatorului
Pagină principală simplă, care listează rețetele existente într-un format clar, cu link-uri pentru vizualizare detalii, editare și ștergere.

Formularele de adăugare și editare rețete trebuie să fie user-friendly, cu validări pentru câmpuri obligatorii.

g) Cerințe Tehnice
Limbaj și framework: Python 3.x, Django

Baza de date: SQLite3

Utilizarea Django Admin pentru gestionarea ușoară a bazei de date.

Crearea unui fișier requirements.txt cu toate pachetele necesare (de exemplu: Django).

h) Validări și Restricții
Câmpul titlu trebuie să fie obligatoriu și să aibă o lungime minimă de 5 caractere.

Câmpul timp de gătit trebuie să accepte doar valori numerice pozitive.

Utilizatorii neautentificați nu trebuie să poată accesa rutele de adăugare, editare și ștergere.


La finalul proiectului, trebuie să fie livrate următoarele:

Codul sursă al aplicației Django.

Fișierul requirements.txt cu dependențele proiectului.

Testele unitare implementate și un raport sumar privind rezultatele acestora.

Instrucțiuni de rulare a proiectului (README.md), care să includă:

Pașii pentru setarea unui mediu virtual și instalarea dependențelor.

Comenzi pentru migrarea bazei de date și rularea serverului local.

Detalii despre accesul la interfața de administrare Django (opțional).
