package design.mode.facade;

/**
 * Created by whx3000 on 2017/2/25
 * you can contact me at: wanghaoxi3000@163.com
 */
class Facade {
    SubSystemOne one;
    SubSystemTwo two;
    SubSystemThree three;

    public Facade(){
        one = new SubSystemOne();
        two = new SubSystemTwo();
        three = new SubSystemThree();
    }

    public void MethodA(){
        System.out.println("方法组A");
        one.MethodOne();
        two.MethodTwo();
        three.MethodThree();
    }

    public void MethodB(){
        System.out.println("方法组B");
        three.MethodThree();
        two.MethodTwo();
        one.MethodOne();
    }

    public static void main(String[] args){
        Facade facade = new Facade();

        facade.MethodA();
        facade.MethodB();
    }

}
