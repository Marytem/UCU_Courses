package StrategyAndDecoratorTest;

import StrategyAndDecorator.BonusDecorator;
import StrategyAndDecorator.Cart;
import StrategyAndDecorator.DeliveryDHL;
import org.junit.Test;

public class BonusDecoratorTest {
    private Cart cart = new Cart();
    private Cart BonusCart = new BonusDecorator(cart);

    @Test
    public void BonusShipTest(){
        BonusCart.setDeliveryStrategy(new DeliveryDHL());
        assert (BonusCart.ship());
    }
}
