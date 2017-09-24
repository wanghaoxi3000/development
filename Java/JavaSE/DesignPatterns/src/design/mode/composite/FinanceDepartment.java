package design.mode.composite;




/**
 * Created by whx3000 on 2017/3/23
 * you can contact me at: wanghaoxi3000@163.com
 */
class FinanceDepartment extends Company {
    public FinanceDepartment(String name) {
        super(name);
    }

    @Override
    public void Add(Company c) {

    }

    @Override
    public void Remove(Company c) {

    }

    @Override
    public void Display(int depth) {
        String  de = "-";
        for (int i=0; i<depth; i++) {
            de += "-";
        }

        System.out.println(de + name);
    }

    @Override
    public void LineOfDuty() {
        System.out.println(name + ": 公司收支管理");
    }
}
