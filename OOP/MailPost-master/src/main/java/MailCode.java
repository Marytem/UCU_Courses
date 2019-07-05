import java.util.ArrayList;

public class MailCode {

    public ArrayList<ArrayList<String>> templates = new ArrayList<ArrayList<String>>();

    public void addTemplate(String greet, String plot, String goodb){
        ArrayList<String> text = new ArrayList<String>();
        text.add(greet);
        text.add(plot);
        text.add(goodb);
        templates.add(text);
    }
}
