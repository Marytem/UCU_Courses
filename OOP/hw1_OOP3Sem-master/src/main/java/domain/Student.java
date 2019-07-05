package domain;

import json.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by Andrii_Rodionov on 1/3/2017.
 */
public class Student extends BasicStudent {
    private String name;
    private String surname;
    private Integer year;
    private List<Tuple<String, Integer>> exams;


    public Student(String name, String surname, Integer year, Tuple<String, Integer>... exams) {
        this.name = name;
        this.surname = surname;
        this.year = year;
        this.exams = new ArrayList<>();
        this.exams.addAll(Arrays.asList(exams));
    }

    public JsonObject toJsonObject() {
        JsonObject JObj = new JsonObject(
                new JsonPair("name", new JsonString(name)),
                new JsonPair("surname", new JsonString(surname)),
                new JsonPair("year", new JsonNumber(year))
        );
        JsonArray examArray = new JsonArray();
        for (Tuple<String, Integer> exam : exams){
            JsonObject jsonExam = new JsonObject(
                    new JsonPair("course", new JsonString(exam.key)),
                    new JsonPair("mark", new JsonNumber(exam.value))
            );
            if (exam.value < 3) { jsonExam.add(new JsonPair("passed", new JsonBoolean(false)));
            }
            else {jsonExam.add(new JsonPair("passed", new JsonBoolean(true)));
            }
            examArray.add(jsonExam);
        }
        JObj.add(new JsonPair("exams", examArray));
        return JObj;
    }
}
