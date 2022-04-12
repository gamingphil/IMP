function getZufallszahl(min, max) {
    return Math.ceil(Math.random() * (max - min) + min);
  }

function erzeugeZufallsarray (LEN) {

    if(isNaN(LEN)) return console.log("laenge muss eine Zahl sein");
    if(Math.sign(LEN) === -1 || Math.sign(LEN) === 0) return console.log("Zahl muss größer als 0 sein");
    var zahlen = new Array(LEN);
    // zahlen[0] = 20;
    // zahlen[1] = 50;
    // zahlen[2] = 30;
    // zahlen[3] = 100;


    for(let i = 0; i < zahlen.length; i++) {
        zahlen[i] = getZufallszahl(1, 300);
    }

    return zahlen;
}

console.log(erzeugeZufallsarray(4));