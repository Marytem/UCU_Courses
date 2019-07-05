package game;

public abstract class Character {

    protected int power;
    protected int hp = 2;

    public abstract void kick(Character c);

    public boolean isAlive() {
        return hp > 0;
    }

    public int getPower() {
        return power;
    }

    public int getHp() {
        return hp;
    }

}
