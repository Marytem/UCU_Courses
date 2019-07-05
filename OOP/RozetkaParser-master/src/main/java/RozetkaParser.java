import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

//import javax.swing.text.Document;
import java.io.IOException;
import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
//import java.nio.file.Files;
//import java.util.List;

public class RozetkaParser {
    public static void main(String[] args) throws  IOException{
        String url = "https://rozetka.com.ua/ua/all-tv/c80037/";
        parseCategory(url);
    }
    private static int FindSumOfPages(String url) throws IOException {
        Document doc = Jsoup.connect(url).get();
        Elements CatalogLinks = doc.getElementsByClass("paginator-catalog-l-link");
        return (CatalogLinks.size() == 0) ? 0 : Integer.parseInt(CatalogLinks.get(CatalogLinks.size() - 1).text());
    }

    private static void parseCategory(String url) throws IOException {
        File datafile = new File("data"); //create folder
        if (!datafile.exists()) {
            datafile.mkdir();
        }

        for(int i=0; i<FindSumOfPages(url); i++) {
            parseCategoryPage(url + "page=" + String.valueOf(i + 1) + "/");
        }
    }


    private static void parseCategoryPage(String url)throws IOException {
        Document doc = Jsoup.connect(url).get();
        Elements models = doc.select("div.g-i-tile-i-title");
        for (Element model : models) {
            String url2 = model.select("a").attr("href");
            parseReviews(url2 + "comments/");
        }
    }

    private static void parseReviews(String url)throws IOException {
        int pgnum = FindSumOfPages(url);

        ArrayList<ArrayList<ArrayList<String>>> sentiments = new ArrayList<ArrayList<ArrayList<String>>>();
        for(int i=0; i<pgnum; i++) {
            String link = url + "page=" + String.valueOf(i+1) + "/";
            sentiments.add(parseReviewsPage(link));
        }

        String filename = "data/" + url.split("/")[4] + ".csv";
        PrintWriter writer = new PrintWriter(filename, "UTF-8");
        for (ArrayList<ArrayList<String>> commentSet : sentiments){
            for (ArrayList<String> comment : commentSet){
                writer.println(comment.get(0) + "," + comment.get(1));
            }
        }
    }

    private static ArrayList<ArrayList<String>> parseReviewsPage(String url)throws IOException {
        Document doc = Jsoup.connect(url).get();
        Elements reviews = doc.select("article.pp-review-i");

        ArrayList<ArrayList<String>> sentiments = new ArrayList<ArrayList<String>>();

        for(Element review : reviews){
            Elements star = review.select("span.g-rating-stars-i");
            Elements text = review.select("div.pp-review-text");
            if (star.size() != 0){
                ArrayList<String> comment = new ArrayList<String>();
                Elements texts = text.select("div.pp-review-text-i");
                comment.add(star.attr("content"));
                comment.add(texts.text());
                sentiments.add(comment);
            }
        }
        return sentiments;
    }
}
