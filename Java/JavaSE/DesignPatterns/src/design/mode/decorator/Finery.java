package design.mode.decorator;

/**
 * Created by whx3000 on 2017/2/8
 * you can contact me at: wanghaoxi3000@163.com
 */
class Finery extends Person {
    protected Person component;

    public void Decorator(Person component) {
        this.component = component;
    }

    @Override
    public void show(){
        if (component != null) {
            component.show();
        }
    }
}
