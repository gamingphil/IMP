function getZufallszahl(min, max) {
    return Math.ceil(Math.random() * (max - min) + min);
  }

function erzeugeZufallsarray (LEN) {

    let laenge = LEN;
    if(isNaN(laenge)) return console.log("laenge muss eine Zahl sein");
    if(Math.sign(laenge) === -1 || Math.sign(laenge) === 0) return console.log("Zahl muss größer als 0 sein");
    var zahlen = new Array(laenge);
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