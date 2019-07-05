package StrategyAndDecorator;

public class DiscountDecorator extends CartDecorator{

    public DiscountDecorator(Cart cart){
        super(cart);
    }

    @Override
    public double computeTotalPrice() {
        System.out.println("Get our discount! -50%");
        return super.computeTotalPrice() * 0.5;
    }
}
