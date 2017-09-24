package design.mode.bridge;

/**
 * Created by whx3000 on 2017/3/31
 * you can contact me at: wanghaoxi3000@163.com
 */
class Abstraction {
    protected Implementor implementor;

    public void SetImplementor(Implementor implementor) {
        this.implementor = implementor;
    }

    public void Operation() {
        implementor.Operation();
    }
}
