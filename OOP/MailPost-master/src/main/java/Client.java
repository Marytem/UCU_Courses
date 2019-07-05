public class Client {

    String name = new String();
    String other = new String();
    int age;
    boolean sex;
    MailBox mailBox;

    Client(String name, String other, int age, boolean sex){
        this.name = name;
        this.other = other;
        this.age = age;
        this.sex = sex;
        this.mailBox = new MailBox();
    }

}
