package design.mode.adapter;

/**
 * Created by whx3000 on 2017/3/20
 * you can contact me at: wanghaoxi3000@163.com
 */
class Adapter extends Target {
    private Adaptee adaptee = new Adaptee();

    @Override
    public void Request() {
        adaptee.SpecificRequest();
    }

    public static void main(String[] args) {
        Target target = new Adapter();
        target.Request();
    }
}
