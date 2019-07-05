package StoreItself;

public enum Shape {
    CAP, COWBOY, SOMBRERO, PANAMA, BOWLER, TOP, BEANIE;

    public String toString(){
        switch (this){
            case CAP: return "cap";
            case TOP: return "top";
            case BEANIE: return "beanie";
            case BOWLER: return "bowler";
            case COWBOY: return "cowboy";
            case PANAMA: return "panama";
            case SOMBRERO: return "sombrero";
            default: return null;
        }
    }

}
