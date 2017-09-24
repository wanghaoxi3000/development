package design.mode.factory;

/**
 * Created by whx3000 on 2017/2/13
 * you can contact me at: wanghaoxi3000@163.com
 */
class Main {
    public static void main(String[] args) {
        IFactory factory = new UndergraduateFactory();
        //IFactory factory = new VolunteerFactory();
        //换成社区志愿者时仅需修改一处就可以了
        LeiFeng student = factory.CreateLeiFeng();

        student.sweep();
        student.wash();
        student.buyRice();
    }
}
