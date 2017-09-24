package design.mode.composite;

/**
 * Created by whx3000 on 2017/3/23
 * you can contact me at: wanghaoxi3000@163.com
 */
abstract class Company {
    protected String name;

    public Company(String name) {
        this.name = name;
    }

    public abstract void Add(Company c);
    public abstract void Remove(Company c);
    public abstract void Display(int depth);
    public abstract void LineOfDuty(); //履行职责
}
