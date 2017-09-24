package design.mode.builder;

/**
 * Created by whx3000 on 2017/2/26
 * you can contact me at: wanghaoxi3000@163.com
 */
class Director {
    public void construct(Builder builder){
        builder.BuildA();
        builder.BuildB();
    }

    //客户端代码，客户不知道具体的建造过程
    public static void main(String[] args){
        Director director = new Director();
        Builder b1 = new ConcreteBuilder1();
        Builder b2 = new ConcreteBuilder2();

        director.construct(b1);
        Product p1 = b1.GetResult();
        p1.show();

        director.construct(b2);
        Product p2 = b2.GetResult();
        p2.show();
    }
}
