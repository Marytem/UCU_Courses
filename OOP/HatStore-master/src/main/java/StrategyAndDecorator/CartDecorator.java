package StrategyAndDecorator;

public class CartDecorator extends Cart{
    protected Cart cart;

    public CartDecorator(Cart cart){
        this.cart = cart;
    }

    @Override
    public double computeTotalPrice() {
        return super.computeTotalPrice();
    }

    @Override
    public boolean ship() {
        return super.ship();
    }
}
