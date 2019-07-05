package StrategyAndDecorator;

public class Privat24Payment implements PaymentStrategy{
    @Override
    public boolean pay(double price) {
        System.out.println("paid with Privat24");
        return price != 0.0;
    }
}
