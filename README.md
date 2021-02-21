# BooksPython
* Database name - abstractproject&nbsp;
GET&nbsp;
/api/v1/get/users - vraca sve usere iz baze&nbsp;
/api/v1/get/one/user - vraca jednog usera kom odgovaraju email i password prosledjeni kroz parametre&nbsp;
/api/v1/get/book/<id> - vraca sve knjige koje odgovaraju ulogovanom korisniku&nbsp;
/api/v1/get/one/book/<id> - vraca podatke za jednu knjigu sa prosledjenim id-jem&nbsp;
POST&nbsp;
/api/v1/create/user - kreira novog usera sa prosledjenim parametrima&nbsp;
/api/v1/create/book - kreira novu knjigu sa prosledjenim parametrima&nbsp;
DELETE&nbsp;
/api/v1/delete/book/<id> - brise jednu knjigu kojoj odgovara dati id&nbsp;
PUT&nbsp;
/api/v1/edit/book - edituje knjigu kojoj odgovara dati id
