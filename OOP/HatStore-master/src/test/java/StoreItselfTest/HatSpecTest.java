package StoreItselfTest;

import StoreItself.Colour;
import StoreItself.Fabric;
import StoreItself.HatSpec;
import StoreItself.Shape;
import org.junit.Test;

public class HatSpecTest {

    @Test
    public void hatSpecInit_GetAllProps(){

        HatSpec spec = new HatSpec(Colour.RED, Fabric.JEANS, Shape.CAP, "model1", 4);
        assert (spec.getColour() == Colour.RED);
        assert (spec.getFabric() == Fabric.JEANS);
        assert (spec.getShape() == Shape.CAP);
        assert (spec.getModel().equals("model1"));
        assert (spec.getSize() == 4);
    }

    @Test
    public void matchesTest(){
        HatSpec spec1 = new HatSpec(Colour.GREEN, Fabric.FELT, Shape.COWBOY, "mymodel0", 3);
        HatSpec spec2 = new HatSpec(Colour.GREEN, Fabric.FELT, Shape.COWBOY, "mymodel0", 3);
        HatSpec otherSpec = new HatSpec(Colour.GREY, Fabric.LEATHER, Shape.PANAMA, "mymodel1", 4);

        assert (spec1.matches(spec2));
        assert (spec2.matches(spec1));
        assert (!spec1.matches(otherSpec));
        assert (!otherSpec.matches(spec2));
    }
}
