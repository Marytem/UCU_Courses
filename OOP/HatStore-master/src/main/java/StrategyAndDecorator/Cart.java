package StrategyAndDecorator;

import Observer.Observable;
import StoreItself.Hat;
import java.util.ArrayList;

public class Cart extends Observable{
    private ArrayList<Hat> hats = new ArrayList<>();
    private PaymentStrategy paymentStrategy;
    private DeliveryStrategy deliveryStrategy;

    public void putToCart(Hat hat){
        hats.add(hat);
    }

    public boolean ship(){
        System.out.println("your cart is cuccesfully shipped");
        return deliveryStrategy.deliver(hats);
    }

    public double computeTotalPrice(){
        double total = 0.0;
        for (Hat hat : hats) {
            total += hat.getPrice();
        }
        return total;
    }

    public ArrayList<Hat> getHats() {
        return hats;
    }

    public PaymentStrategy getPaymentStrategy() {
        return paymentStrategy;
    }

    public Cart setPaymentStrategy(PaymentStrategy paymentStrategy) {
        this.paymentStrategy = paymentStrategy;
        return this;
    }

    public DeliveryStrategy getDeliveryStrategy() {
        return deliveryStrategy;
    }

    public Cart setDeliveryStrategy(DeliveryStrategy deliveryStrategy) {
        this.deliveryStrategy = deliveryStrategy;
        return this;
    }
}
