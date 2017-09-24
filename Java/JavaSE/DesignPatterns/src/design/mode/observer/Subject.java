package design.mode.observer;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by whx3000 on 2017/3/8
 * you can contact me at: wanghaoxi3000@163.com
 */
abstract class Subject {
    private List<Observer> observers = new ArrayList<>();

    public void attach(Observer observer){
        observers.add(observer);
    }

    public void detach(Observer observer){
        observers.remove(observer);
    }

    public void Notify(){
        for (Observer obs: observers) {
            obs.update();
        }
    }

}
