package design.mode.prototype;

/**
 * Created by whx3000 on 2017/2/15
 * you can contact me at: wanghaoxi3000@163.com
 */
class Main {
    public static void main(String[] args) {
        Prototype p1 = new Prototype("I");
        Prototype p2 = (Prototype)p1.clone();

        p2.setId("O");

        System.out.println("p1: " + p1.getId());
        System.out.println("p2: " + p2.getId());
    }
}
