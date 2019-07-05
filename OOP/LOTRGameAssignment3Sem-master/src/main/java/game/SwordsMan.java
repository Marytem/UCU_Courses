package game;

import java.util.Random;

public abstract class SwordsMan extends Character{

    protected int MAX_POWER;
    protected int MIN_POWER;

    SwordsMan(int MAX_POWER, int MIN_POWER){
        this.MAX_POWER = MAX_POWER;
        this.MIN_POWER = MIN_POWER;
        this.power = setPowerHpVal();
        this.hp = setPowerHpVal();
    }

    private int setPowerHpVal(){
        Random rand = new Random();
        return rand.nextInt(MAX_POWER - MIN_POWER + 1) + MIN_POWER;
    }

    @Override
    public void kick(Character c){
        Random rand = new Random();
        c.hp -= rand.nextInt(power - MIN_POWER + 1) + MIN_POWER;
    }
}
