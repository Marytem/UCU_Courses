package Observer;

public class Customer extends User{

    public Customer(String name, String phoneNumber){ super(name,phoneNumber); }

    @Override
    public void update() {
        timesUpdated += 1;
        System.out.println("Customer was updated");
    }
}
