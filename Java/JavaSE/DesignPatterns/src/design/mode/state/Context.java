package design.mode.state;

/**
 * Created by wangh on 2017/3/18.
 * you can contact me at: wanghaoxi3000@163.com
 */
class Context {
    private State state;

    public Context(State state) {
        this.state = state;
    }

    public State getState() {
        return state;
    }

    public void setState(State state) {
        this.state = state;
        System.out.println("当前状态: " + state.getClass().getName());
    }

    public void Requset() {
        state.Handle(this);
    }
}
