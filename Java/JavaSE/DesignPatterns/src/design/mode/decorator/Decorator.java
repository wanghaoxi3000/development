package design.mode.decorator;

/**
 * Created by whx3000 on 2017/2/8
 * you can contact me at: wanghaoxi3000@163.com
 */
public class Decorator {
    public static void main(String[] args) {
        Person xc = new Person("小菜");
        System.out.println("第一种穿法:");

        TShirts ts1 = new TShirts();
        BigTrouser bi2 = new BigTrouser();

        ts1.Decorator(xc);
        bi2.Decorator(ts1);
        bi2.show();

        System.out.println("\n第二种穿法:");

        TShirts ts2 = new TShirts();
        BigTrouser bi1 = new BigTrouser();

        bi1.Decorator(xc);
        ts2.Decorator(bi1);
        ts2.show();
    }
}
