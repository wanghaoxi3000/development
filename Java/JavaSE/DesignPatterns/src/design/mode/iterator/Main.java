package design.mode.iterator;

/**
 * Created by whx3000 on 2017/3/28
 * you can contact me at: wanghaoxi3000@163.com
 */
class Main {
    public static void main(String[] args){
        ConcreteAggregate<String> a = new ConcreteAggregate<String>();

        a.addAggregate(0, "大鸟");
        a.addAggregate(1, "小菜");
        a.addAggregate(2, "行李");
        a.addAggregate(3, "老外");
        a.addAggregate(4, "公交内部员工");
        a.addAggregate(5, "小偷");

        Iterator i = new ConcreteIterator(a);
        Object item = i.First();
        System.out.println("第一位乘客: " + item);

        while (!i.IsDone()) {
            System.out.println(i.CurrentItem() + "请购买车票");
            i.Next();
        }
    }
}
