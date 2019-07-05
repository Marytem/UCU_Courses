package Observer;

public class Seller extends User {

    public Seller(String name, String phoneNumber){
        super(name,phoneNumber);
    }

    @Override
    public void update() {
        timesUpdated += 1;
        System.out.println("Seller was updated");
    }
}
