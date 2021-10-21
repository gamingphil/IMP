public void setup() {
    size(500, 500);
    whileLoop();
    forLoop();
    arrays();
    ifSchleife();
}

public void whileLoop() {
    int n = 0;
    while(n < 5) {
        print("Hallo!\n");
        n++;
    }
}

public void forLoop() {
    for(int i = 0; i < 5; i++) {
        print("Hallo!\n");
    }
}

public void arrays() {
    int[] zahlen = {5, 10, 27, 1, 13};
    zahlen[1] = 9;

    
    String[] tiere = {"Gorilla", "Bieber", "Koala"};
    // print(tiere[2]);

    int[] dreiZahlen = new int[3];
    // print(zahlen.length);

    for(int i = 0; i < dreiZahlen.length; i++) {
        dreiZahlen[i] = 3;
    }
}

public void ifSchleife() {
    int x = 314;
    int y = 4000;
    if(x > y) {
        print("x ist größer als y");
    }else if(y > x){
        print("y ist größer als x");
    }else {
        print("x und y sind gleich groß");
    }
}