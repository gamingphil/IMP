function getZufallszahl(min, max) {
    return Math.random() * (max - min) + min;
  }

function erzeugeZufallsarray () {

    let laenge = 4
    if(isNaN(laenge)) return console.log("laenge muss eine Zahl sein");
    if(Math.sign(laenge) === -1 || Math.sign(laenge) === 0) return console.log("Zahl muss größer als 0 sein")
    let zahlen = new Array(laenge);
    zahlen[0] = 20;
    zahlen[1] = 50;
    zahlen[2] = 30;
    zahlen[3] = 100;


    for(let i = 0; i > zahlen.length; i++) {
        zahlen[i] = getZufallszahl(1, 300);
    }

    return zahlen;

}

console.log(erzeugeZufallsarray());