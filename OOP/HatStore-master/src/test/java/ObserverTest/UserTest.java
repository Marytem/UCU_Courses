package ObserverTest;

import Observer.Customer;
import org.junit.Test;

import java.util.Objects;

public class UserTest {
    private Customer customer = new Customer("name", "number");

    @Test
    public void testUser(){
        String name = "name1";
        String number = "number1";

        customer.setName(name);
        customer.setPhoneNumber(number);

        assert (Objects.equals(customer.getName(), name));
        assert (Objects.equals(customer.getPhoneNumber(), number));
    }

}
