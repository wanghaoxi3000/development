package design.mode.bridge;

/**
 * Created by whx3000 on 2017/3/31
 * you can contact me at: wanghaoxi3000@163.com
 */
class ConcreteImplementorA extends Implementor {
    @Override
    public void Operation() {
        System.out.println("具体实现A类的方法执行");
    }
}
