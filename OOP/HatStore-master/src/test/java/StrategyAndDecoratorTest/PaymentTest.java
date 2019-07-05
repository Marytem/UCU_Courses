package StrategyAndDecoratorTest;

import StrategyAndDecorator.*;
import org.junit.Test;

public class PaymentTest {
    private Cart cart = new Cart();
    private PaymentStrategy paymentStrategy1 = new Privat24Payment();
    private PaymentStrategy paymentStrategy2 = new CashPayment();

    @Test
    public void PayByPrivat_PaidSuccesfully(){
        cart.setPaymentStrategy(paymentStrategy1);

        assert (cart.getPaymentStrategy() == paymentStrategy1);
        assert (!cart.getPaymentStrategy().pay(0.0));
        assert (cart.getPaymentStrategy().pay(12.8));
    }

    @Test
    public void PayByCash_PaidSuccesfully(){
        cart.setPaymentStrategy(paymentStrategy2);

        assert (cart.getPaymentStrategy() == paymentStrategy2);
        assert (!cart.getPaymentStrategy().pay(0.0));
        assert (cart.getPaymentStrategy().pay(12.8));
    }
}
