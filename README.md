# BooksPython
* Database name - abstractproject
GET
/api/v1/get/users - vraca sve usere iz baze
/api/v1/get/one/user - vraca jednog usera kom odgovaraju email i password prosledjeni kroz parametre
/api/v1/get/book/<id> - vraca sve knjige koje odgovaraju ulogovanom korisniku
/api/v1/get/one/book/<id> - vraca podatke za jednu knjigu sa prosledjenim id-jem
POST
/api/v1/create/user - kreira novog usera sa prosledjenim parametrima
/api/v1/create/book - kreira novu knjigu sa prosledjenim parametrima
DELETE
/api/v1/delete/book/<id> - brise jednu knjigu kojoj odgovara dati id
PUT
/api/v1/edit/book - edituje knjigu kojoj odgovara dati id