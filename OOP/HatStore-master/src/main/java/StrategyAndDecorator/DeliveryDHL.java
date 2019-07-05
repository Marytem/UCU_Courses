package StrategyAndDecorator;

import StoreItself.Hat;

import java.util.List;

public class DeliveryDHL implements DeliveryStrategy{
    @Override
    public boolean deliver(List<Hat> hats) {
        System.out.println("DHL deliver");
        return true;
    }
}
