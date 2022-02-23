# BooksPython
* Database name - abstractproject</br>
GET</br>
/api/v1/get/users - vraca sve usere iz baze</br>
/api/v1/get/one/user - vraca jednog usera kom odgovaraju email i password prosledjeni kroz parametre</br>
/api/v1/get/book/<id> - vraca sve knjige koje odgovaraju ulogovanom korisniku</br>
/api/v1/get/one/book/<id> - vraca podatke za jednu knjigu sa prosledjenim id-jem</br>
POST</br>
/api/v1/create/user - kreira novog usera sa prosledjenim parametrima</br>
/api/v1/create/book - kreira novu knjigu sa prosledjenim parametrima</br>
DELETE</br>
/api/v1/delete/book/<id> - brise jednu knjigu kojoj odgovara dati id</br>
PUT</br>
/api/v1/edit/book - edituje knjigu kojoj odgovara dati id

# web aplikacija za vodjenje evidencije o procitanim knjigama.
Korisnik moze da kreira nalog (name, email, password) i da se uloguje sa istim (email/password).
Prilikom registracije uraditi validaciju
Duzina lozinke mora da bude veca od 6 karaktera
Lozinka mora da sadrzi najmanje jedan broj
Da li je validan email (koristiti vec postojece php metode)
Ime sme da sadrzi samo slova i brojeve, ali ne sme da pocinje sa brojem
Korisnik kad je ulogovan moze vidi svoje knjige, da doda knjigu koja je definisana naslovom i opisom, izmeni ili obrise postojecu knjigu
Moze da generise API kljuc za pristup svojim knjigama. Pristup moze biti full (ukljucuje add/edit/delete prava) ili read only (samo get prava)
Napraviti REST API sa GET (izlistavanje knjiga), ADD (dodavanja knjiga), DELETE (brisanje knjiga) i EDIT (izmena knjiga) metodama. API treba da podrzi autentifikaciju koristeci API kljuc. 
Omoguciti login uz pomoc Google naloga
