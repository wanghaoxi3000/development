package design.mode.bridge;

/**
 * Created by whx3000 on 2017/3/31
 * you can contact me at: wanghaoxi3000@163.com
 */
class Main {
    public static void main(String[] args) {
        Abstraction ab = new RefinedAbstraction();

        ab.SetImplementor(new ConcreteImplementorA());
        ab.Operation();

        ab.SetImplementor(new ConcreteImplementorB());
        ab.Operation();
    }
}
