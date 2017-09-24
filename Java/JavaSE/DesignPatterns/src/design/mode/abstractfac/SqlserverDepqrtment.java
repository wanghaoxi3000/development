package design.mode.abstractfac;

/**
 * Created by wangh on 2017/3/14.
 * you can contact me at: wanghaoxi3000@163.com
 */
class SqlserverDepqrtment implements IDepartment {
    @Override
    public void Insert(Department department) {
        System.out.println("在SQL Server中User表增加一条记录");
    }

    @Override
    public Department GetDepartment(int id) {
        System.out.println("在SQL Server中根据ID得到User中一条记录");
        return null;
    }
}
