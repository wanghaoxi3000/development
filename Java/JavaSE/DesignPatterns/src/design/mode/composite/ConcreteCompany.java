package design.mode.composite;

import java.util.LinkedList;
import java.util.List;

/**
 * Created by whx3000 on 2017/3/23
 * you can contact me at: wanghaoxi3000@163.com
 */
class ConcreteCompany extends Company{
    private List<Company> children = new LinkedList<>();

    public ConcreteCompany(String name) {
        super(name);
    }

    @Override
    public void Add(Company c) {
        children.add(c);
    }

    @Override
    public void Remove(Company c) {
        children.remove(c);
    }

    @Override
    public void Display(int depth) {
        String  de = "-";
        for (int i=0; i<depth; i++) {
            de += "-";
        }

        System.out.println(de + name);

        for (Company component: children) {
            component.Display(depth + 2);
        }
    }

    @Override
    public void LineOfDuty() {
        for (Company component: children) {
            component.LineOfDuty();
        }
    }
}
