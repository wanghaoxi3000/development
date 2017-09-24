package design.mode.state;

/**
 * Created by wangh on 2017/3/18.
 * you can contact me at: wanghaoxi3000@163.com
 */
class Main {
    public static void main(String[] args) {
        Context c = new Context(new ConcreteStateA());

        c.Requset();
        c.Requset();
        c.Requset();
        c.Requset();
    }
}
