package StrategyAndDecoratorTest;

import StrategyAndDecorator.*;
import org.junit.Test;


public class DeliveryTest {
    private Cart cart = new Cart();
    private DeliveryStrategy deliveryStrategy1 = new DeliveryNovaPoshta();
    private DeliveryStrategy deliveryStrategy2 = new DeliveryDHL();

    @Test
    public void deliverByNovaPoshta_deliveredSuccesfully(){
        cart.setDeliveryStrategy(deliveryStrategy1);

        assert (cart.getDeliveryStrategy() == deliveryStrategy1);
        assert (cart.getDeliveryStrategy().deliver(cart.getHats()));
    }

    @Test
    public void deliverByDHL_deliveredSuccesfully(){
        cart.setDeliveryStrategy(deliveryStrategy2);

        assert (cart.getDeliveryStrategy() == deliveryStrategy2);
        assert (cart.getDeliveryStrategy().deliver(cart.getHats()));
    }

}
