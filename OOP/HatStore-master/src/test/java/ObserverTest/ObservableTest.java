package ObserverTest;

import Observer.Customer;
import Observer.Seller;
import StrategyAndDecorator.Cart;
import org.junit.Test;

public class ObservableTest {
    private Cart cart = new Cart();

    @Test
    public void addObservers_observersInList(){
        Customer customer = new Customer("name1", "number1");
        Seller seller = new Seller("name2", "number2");

        cart.addObserver(customer);
        cart.addObserver(seller);

        assert (cart.getObservers().contains(customer));
        assert (cart.getObservers().contains(seller));

        cart.removeObserver(seller);

        assert (!cart.getObservers().contains(seller));
    }

    @Test
    public void notifyObservers_observersUpdated(){
        Customer customer = new Customer("name1", "number1");
        Seller seller = new Seller("name2", "number2");
        cart.addObserver(customer);
        cart.addObserver(seller);

        cart.notifyObservers();

        assert (customer.getTimesUpdated() == seller.getTimesUpdated());
        assert (seller.getTimesUpdated() == 1);
    }
}
