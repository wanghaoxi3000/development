package design.mode.template;

/**
 * Created by whx3000 on 2017/2/18
 * you can contact me at: wanghaoxi3000@163.com
 */
class Main {
    public static void main(String[] args){
        System.out.println("StudentA: ");
        TestQuestion studentA = new TestPaperA();
        studentA.TestQustion1();
        studentA.TestQustion2();

        System.out.println("\nStudentB: ");
        TestQuestion studentB = new TestPaperB();
        studentB.TestQustion1();
        studentB.TestQustion2();
    }
}
