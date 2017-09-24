package design.mode.memento;

/**
 * Created by whx3000 on 2017/3/22
 * you can contact me at: wanghaoxi3000@163.com
 */
class Memento {
    private String state;

    public Memento(String state) {
        this.state = state;
    }

    public String getState() {
        return state;
    }
}
