package StrategyAndDecorator;

public class CashPayment implements PaymentStrategy{
    @Override
    public boolean pay(double price) {
        System.out.println("paid with cash");
        return price != 0.0;
    }
}

