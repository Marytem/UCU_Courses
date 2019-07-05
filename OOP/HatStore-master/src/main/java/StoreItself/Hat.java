package StoreItself;

public class Hat {

    private String serialNumber;
    private double price;
    private HatSpec hatSpec;

    public Hat(String serialNumber, double price, HatSpec hatSpec) {
        this.serialNumber = serialNumber;
        this.price = price;
        this.hatSpec = hatSpec;
    }

    public double getPrice() {
        return price;
    }

    public Hat setPrice(double price) {
        this.price = price;
        return this;
    }

    public String getSerialNumber() {
        return serialNumber;
    }


    public HatSpec getHatSpec() {
        return hatSpec;
    }
}
