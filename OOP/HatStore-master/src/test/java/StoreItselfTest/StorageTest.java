package StoreItselfTest;

import StoreItself.*;
import org.junit.Test;
import static org.junit.Assert.assertTrue;


public class StorageTest {
    Storage storage = new Storage();
    @Test
    public void StorageAddHat_GetHatFromStorage(){
        storage.addHat("5678", Shape.TOP, "mymodel", Fabric.JEANS, Colour.ORANGE, 6.7, 8);

        assert (storage.getHat("5678").getSerialNumber().equals("5678"));
    }

    @Test
    public void searchTest(){
        HatSpec hatSpec = new HatSpec(Colour.PURPLE, Fabric.COTTON, Shape.BOWLER, "mymodel", 5);

        assert (storage.search(hatSpec).isEmpty());

        storage.addHat("4567", Shape.BOWLER, "mymodel", Fabric.COTTON, Colour.PURPLE, 6.7, 5);
        assert (!storage.search(hatSpec).isEmpty());
    }
}
