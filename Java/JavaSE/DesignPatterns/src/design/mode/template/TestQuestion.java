package design.mode.template;

/**
 * Created by whx3000 on 2017/2/18
 * you can contact me at: wanghaoxi3000@163.com
 */
abstract class TestQuestion
{
    void TestQustion1() {
        System.out.println("Question 1");
        System.out.println("Answer1: " + Answer1());
    }

    void TestQustion2() {
        System.out.println("Question 2");
        System.out.println("Answer2: " + Answer2());
    }

    protected abstract String Answer1();
    protected abstract String Answer2();
}
