package design.mode.bridge;

/**
 * Created by whx3000 on 2017/3/31
 * you can contact me at: wanghaoxi3000@163.com
 */
class RefinedAbstraction extends Abstraction {
    @Override
    public void Operation() {
        implementor.Operation();
    }
}
