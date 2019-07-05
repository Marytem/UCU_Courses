package game;

public class Hobbit extends Character{
    public Hobbit(){
        hp = 3;
        power = 0;
    }

    public void kick(Character c) {
        toCry();
    }

    private void toCry(){
        System.out.println("Aaaaaaaaaaaaargh..");
    }
}
