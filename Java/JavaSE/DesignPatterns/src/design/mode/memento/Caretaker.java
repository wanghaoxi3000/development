package design.mode.memento;

/**
 * Created by whx3000 on 2017/3/22
 * you can contact me at: wanghaoxi3000@163.com
 */
class Caretaker {
    private Memento memento;

    public Memento getMemento() {
        return memento;
    }

    public void setMemento(Memento memento) {
        this.memento = memento;
    }
}
