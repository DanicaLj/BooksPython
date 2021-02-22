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
