package design.mode.proxy;

/**
 * Created by whx3000 on 2017/2/9
 * you can contact me at: wanghaoxi3000@163.com
 */
class Main {
    public static void main(String[] args){
        SchoolGirl mm = new SchoolGirl();
        mm.setName("LiJiaoJiao");

        Pursuit daili = new Pursuit(mm);

        daili.GiveDolls();
        daili.GiveFlowers();
        daili.GiveChocolate();
    }
}
