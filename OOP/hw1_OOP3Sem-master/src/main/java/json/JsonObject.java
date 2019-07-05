package json;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

/**
 * Created by Andrii_Rodionov on 1/3/2017.
 */
public class JsonObject extends Json {
    private List<JsonPair> jsonPairs;

    public JsonObject(JsonPair... jsonPairs) {
        this.jsonPairs = new ArrayList<>();
        this.jsonPairs.addAll(Arrays.asList(jsonPairs));
    }

    @Override
    public String toJson() {
        return "{" + getJsonObjBody() + "}";
    }

    private String getJsonObjBody() {
        String jsonStr = "";
        Iterator<JsonPair> jsonPairIterator = jsonPairs.iterator();
        while (jsonPairIterator.hasNext()) {
            JsonPair jsonPair = jsonPairIterator.next();
            jsonStr += jsonPair.toString();
            if (jsonPairIterator.hasNext())
                jsonStr += ", ";
        }
        return jsonStr;
    }

    public void add(JsonPair jsonPair) {
        jsonPairs.add(jsonPair);
    }

    public Json find(String name) {
        for (JsonPair jsonP : jsonPairs){
            if (jsonP.key.equals(name)){return jsonP.value;}
        }
        return null;
    }

    public JsonObject projection(String... names) {
        JsonObject projObj = new JsonObject();
        for (String name: names) {
            if (this.find(name) != null){
                projObj.add(new JsonPair(name, this.find(name)));
            }
        }
        return projObj;
    }
}
