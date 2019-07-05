package StrategyAndDecorator;

import StoreItself.Hat;
import java.util.List;

public interface DeliveryStrategy {
    boolean deliver(List<Hat> hats);
}
