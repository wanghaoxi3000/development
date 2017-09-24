package design.mode.composite;

/**
 * Created by whx3000 on 2017/3/23
 * you can contact me at: wanghaoxi3000@163.com
 */
class Main {
    public static void main(String[] args){
        ConcreteCompany root = new ConcreteCompany("北京总公司");
        root.Add(new HRDepartment("总公司人力资源部"));
        root.Add(new FinanceDepartment("总公司财务部"));

        ConcreteCompany comp = new ConcreteCompany("上海华东分公司");
        comp.Add(new HRDepartment("华东分公司人力资源部"));
        comp.Add(new FinanceDepartment("华东分公司财务部"));
        root.Add(comp);

        ConcreteCompany comp1 = new ConcreteCompany("南京分公司");
        comp1.Add(new HRDepartment("南京公司人力资源部"));
        comp1.Add(new FinanceDepartment("南京公司财务部"));
        root.Add(comp1);

        ConcreteCompany comp2 = new ConcreteCompany("杭州分公司");
        comp2.Add(new HRDepartment("杭州分公司人力资源部"));
        comp2.Add(new FinanceDepartment("杭州分公司财务部"));
        root.Add(comp2);

        System.out.println("结构图:");
        root.Display(1);

        System.out.println("职责:");
        root.LineOfDuty();
    }

}
