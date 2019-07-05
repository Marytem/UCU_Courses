public class MailInfo {
    Client cl;
    MailCode mailCode;

    MailInfo(String name, String other, int age, boolean sex, String mailCode){
        this.cl = new Client(name, other, age, sex);
        this.mailCode = mailCode;
    }

}
