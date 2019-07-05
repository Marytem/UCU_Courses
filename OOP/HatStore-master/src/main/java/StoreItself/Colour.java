package StoreItself;

public enum Colour {
    RED, WHITE, GREY, BLACK, BLUE, PURPLE, PINK, GREEN, YELLOW, ORANGE;

    public String toString(){
        switch (this){
            case RED: return "red";
            case BLUE: return "blue";
            case BLACK: return "black";
            case GREY: return "grey";
            case PURPLE: return "purple";
            case GREEN: return "green";
            case PINK: return "pink";
            case YELLOW: return "yellow";
            case ORANGE: return "orange";
            case WHITE: return "white";
            default: return null;
        }
    }
}
