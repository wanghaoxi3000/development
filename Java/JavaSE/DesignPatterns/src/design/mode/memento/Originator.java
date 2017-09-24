package design.mode.memento;

/**
 * Created by whx3000 on 2017/3/22
 * you can contact me at: wanghaoxi3000@163.com
 */
class Originator {
    private String state;

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public Memento CreateMemento() {
        return (new Memento(state));
    }

    public void SetMemento(Memento memento) {
        state = memento.getState();
    }

    public void Show() {
        System.out.println("State=" + state);
    }
}
