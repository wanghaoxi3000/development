package design.mode.Flyweight;

import java.util.Hashtable;

/**
 * Created by whx3000 on 2017/4/9
 * you can contact me at: wanghaoxi3000@163.com
 */

//所有具体享元类的超类或接口, 接受并作用于外部状态
abstract class AbstractFlyweight {
    public abstract void Operation(int extrinsictate);
}

//继承AbstractFlyweight超类或实现AbstractFlyweight接口, 为内部增加存储空间
class ConcreteFlyweight extends AbstractFlyweight {
    @Override
    public void Operation(int extrinsictate) {
        System.out.println("具体Flyweight: " + extrinsictate);
    }
}

//UnsharedConcteteFlyweight是指那些不需要共享的Flyweight子类, 因为Flyweight接口共享成员, 但它并不强制共享
class UnsharedConcreteFlyweight extends AbstractFlyweight {
    @Override
    public void Operation(int extrinsictate) {
        System.out.println("具体Flyweight: " + extrinsictate);
    }
}

//享元工厂, 用来创建并管理Flyweight对象. 它主要用来确保合理地共享Flyweight, 当用户请求一个Flyweight时,
//FlyweightFactory对象提供一个已创建的实例或者创建一个(不存在的话)
class FlyweightFactory {
    private Hashtable<String, ConcreteFlyweight> flyweight = new Hashtable<>();

    public FlyweightFactory() {
        flyweight.put("X", new ConcreteFlyweight());
        flyweight.put("Y", new ConcreteFlyweight());
        flyweight.put("Z", new ConcreteFlyweight());
    }

    public AbstractFlyweight GetFlyweight(String key) {
        return (AbstractFlyweight)flyweight.get(key);
    }
}

public class Flyweight {
    public static void main(String[] agrs) {
        int extrinsicstate = 22; //代码外部状态

        FlyweightFactory f = new FlyweightFactory();

        AbstractFlyweight fx = f.GetFlyweight("X");
        fx.Operation(--extrinsicstate);

        AbstractFlyweight fy = f.GetFlyweight("Y");
        fy.Operation(--extrinsicstate);

        AbstractFlyweight fz = f.GetFlyweight("Z");
        fz.Operation(--extrinsicstate);

        UnsharedConcreteFlyweight uf = new UnsharedConcreteFlyweight();
        uf.Operation(--extrinsicstate);
    }
}
