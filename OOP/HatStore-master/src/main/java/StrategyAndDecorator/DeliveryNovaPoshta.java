package StrategyAndDecorator;

import StoreItself.Hat;

import java.util.List;

public class DeliveryNovaPoshta implements DeliveryStrategy{
    @Override
    public boolean deliver(List<Hat> hats) {
        System.out.println("Nova poshta delivery is waiting for you");
        return true;
    }
}
