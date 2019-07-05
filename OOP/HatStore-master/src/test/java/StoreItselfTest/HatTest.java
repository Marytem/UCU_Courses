package StoreItselfTest;

import StoreItself.*;
import org.junit.Test;

public class HatTest {

    @Test
    public void hatInit_GetAllProps(){
        HatSpec hatSpec = new HatSpec(Colour.PINK, Fabric.WOOL, Shape.TOP, "mymodel", 5);
        Hat hat = new Hat("0987", 2.3, hatSpec);

        assert (hat.getHatSpec() == hatSpec);
        assert (hat.getPrice() == 2.3);
        assert (hat.getSerialNumber() == "0987");
    }

    @Test
    public void setPrice_priceDifferent(){
        HatSpec hatSpec = new HatSpec(Colour.PINK, Fabric.WOOL, Shape.TOP, "mymodel", 5);
        Hat hat = new Hat("0987", 2.3, hatSpec);
        hat.setPrice(3.4);

        assert (hat.getPrice() == 3.4);
    }

}