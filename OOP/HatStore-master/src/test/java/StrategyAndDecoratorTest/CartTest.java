package StrategyAndDecoratorTest;

import StoreItself.*;
import StrategyAndDecorator.Cart;
import StrategyAndDecorator.DeliveryDHL;
import org.junit.Test;

public class CartTest {
    private Cart cart = new Cart();
    private HatSpec hatSpec = new HatSpec(Colour.GREEN, Fabric.COTTON, Shape.BOWLER, "mymodel", 4);
    private Hat hat = new Hat("1234", 12.8, hatSpec);

    @Test
    public void putToCart_hatInHats(){
        cart.putToCart(hat);

        assert (cart.getHats().contains(hat));
    }

    @Test
    public void computeTotalPrice_priceIsRight(){
        cart.putToCart(hat);
        assert (cart.computeTotalPrice() == cart.getHats().get(0).getPrice());
    }

    @Test
    public void shipTest(){
        cart.setDeliveryStrategy(new DeliveryDHL());
        assert (cart.ship());
    }

}
