package StoreItself;

public enum Fabric {
    SILK, JEANS, WOOL, COTTON, FELT, LEATHER;

    public String toString() {
        switch (this){
            case FELT: return "felt";
            case SILK: return "silk";
            case WOOL: return "wool";
            case JEANS: return "jeans";
            case COTTON: return "cotton";
            case LEATHER: return "leather";
            default: return null;
        }
    }
}
