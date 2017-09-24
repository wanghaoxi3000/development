package design.mode.memento;

/**
 * Created by whx3000 on 2017/3/22
 * you can contact me at: wanghaoxi3000@163.com
 */
class Main {
    public static void main(String[] args){
        Originator o = new Originator();
        o.setState("On");
        o.Show();

        Caretaker c = new Caretaker();
        c.setMemento(o.CreateMemento());

        o.setState("Off");
        o.Show();

        o.SetMemento(c.getMemento());
        o.Show();
    }
}
