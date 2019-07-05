package StoreItself;

public class HatSpec {

    private Colour colour;
    private Fabric fabric;
    private Shape shape;
    private String model;
    private int size;

    public HatSpec(Colour colour, Fabric fabric, Shape shape, String model, int size){
        this.colour = colour;
        this.fabric = fabric;
        this.model = model;
        this.shape = shape;
        this.size = size;
    }

    public boolean matches(HatSpec otherSpec){
        if ((model != null) && (!model.equals("")) && (!model.equals(otherSpec.model))) {
            return false;
        }
        if (colour != otherSpec.colour){
            return false;}
        if (shape != otherSpec.shape){
            return false;}
        if (fabric != otherSpec.fabric){
            return false;}
        if (size != otherSpec.size){
            return false;}
        return true;
    }

    public Colour getColour() {
        return colour;
    }

    public Fabric getFabric() {
        return fabric;
    }

    public Shape getShape() {
        return shape;
    }

    public String getModel() {
        return model;
    }

    public int getSize() {
        return size;
    }
}
