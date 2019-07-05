package game;

import java.util.Random;

public class CharacterFactory {
    private Random rand = new Random();
    private int charNum = rand.nextInt(4);

    public Character makeChar(){
        switch(charNum) {
            case 0:
                return new Hobbit();
            case 1:
                return new Elf();
            case 2:
                return new King();
            case 3:
                return new Knight();
            default:
                return new Knight();
        }
    }
}
