package StoreItself;

import java.util.LinkedList;
import java.util.List;

public class Storage {
    private List hats;

    public Storage() {
        hats = new LinkedList();
    }

    public void addHat(String serialNumber, Shape shape, String model,
                       Fabric fabric, Colour colour, double price, int size){
        HatSpec hatSpec = new HatSpec(colour, fabric, shape, model, size);
        Hat hat = new Hat(serialNumber, price, hatSpec);
        hats.add(hat);
    }

    public Hat getHat(String serialNumber){
        for (Object hat1 : hats) {
            Hat hat = (Hat) hat1;
            if (hat.getSerialNumber().equals(serialNumber)) {
                return hat;
            }
        }
        return null;
    }

    public List search(HatSpec searchSpec){

        List matchingHats = new LinkedList();

        for (Object hat1 : hats) {
            Hat hat = (Hat) hat1;

            if (searchSpec.matches(hat.getHatSpec())) {
                matchingHats.add(hat);
            }
        }
        return matchingHats;
    }
}
