package design.mode.decorator;

/**
 * Created by whx3000 on 2017/2/8
 * you can contact me at: wanghaoxi3000@163.com
 */
class Person
{
    private String name;

    Person() {

    }

    public Person(String name) {
        this.name = name;
    }

    public void show() {
        System.out.printf("装扮的%s\n", name);
    }
}
