package Observer;

import java.util.ArrayList;


public abstract class Observable {
    private ArrayList<Observer> observers = new ArrayList<>();

    public ArrayList<Observer> getObservers(){return observers;}

    public void addObserver(Observer observer){
        observers.add(observer);
    }

    public void removeObserver(Observer observer){
        observers.remove(observer);
    }

    public void notifyObservers(){
        for (Observer observer: observers){
            observer.update();
        }
    }
}
