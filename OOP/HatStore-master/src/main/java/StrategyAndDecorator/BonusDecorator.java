package StrategyAndDecorator;

public class BonusDecorator extends CartDecorator {

     public BonusDecorator(Cart cart){
        super(cart);
    }

    @Override
    public boolean ship() {
        System.out.println("Get our new hat-antistatic spray for free as a bonus!");
        return super.ship();
    }
}
