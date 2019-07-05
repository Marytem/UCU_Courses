package StrategyAndDecoratorTest;

import StoreItself.*;
import StrategyAndDecorator.Cart;
import StrategyAndDecorator.DiscountDecorator;
import org.junit.Test;

public class DiscountDecoratorTest {
    private Cart cart = new Cart();
    private Cart discCart = new DiscountDecorator(cart);

    @Test
    public void discountComputePrice_PriceIsAppropriate(){
        HatSpec hatSpec = new HatSpec(Colour.GREEN, Fabric.COTTON, Shape.BOWLER, "mymodel", 4);
        Hat hat = new Hat("1234", 12.8, hatSpec);
        discCart.putToCart(hat);
        assert (discCart.computeTotalPrice() == hat.getPrice()*0.5);
    }
}
