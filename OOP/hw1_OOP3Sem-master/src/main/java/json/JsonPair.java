package json;

/**
 * Created by Andrii_Rodionov on 1/3/2017.
 */
public class JsonPair extends Tuple<String, Json>{

    private String name;
    private Json val;

    public JsonPair(String name, Json value) {
        super(name, value);
        this.name = name;
        this.val = value;
    }

    @Override
    public String toString() {
        return "'" + name + "'" + ": " + val.toJson();
    }
}