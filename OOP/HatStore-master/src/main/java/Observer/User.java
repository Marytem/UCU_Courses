package Observer;

public abstract class User implements Observer{

    private String name;
    private String phoneNumber;
    protected int timesUpdated;

    public User(String name, String phoneNumber){
        this.name = name;
        this.phoneNumber = phoneNumber;
    }

    @Override
    public void update() {
        timesUpdated += 1;
        System.out.println("User is updated.");
    }

    public String getName() {
        return name;
    }

    public User setName(String name) {
        this.name = name;
        return this;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public User setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
        return this;
    }

    public int getTimesUpdated() {
        return timesUpdated;
    }
}
