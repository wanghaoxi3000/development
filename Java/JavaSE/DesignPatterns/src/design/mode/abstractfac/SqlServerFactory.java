package design.mode.abstractfac;

/**
 * Created by wangh on 2017/3/14.
 * you can contact me at: wanghaoxi3000@163.com
 */
class SqlServerFactory implements IFactory {
    @Override
    public IDepartment CreateDepartment() {
        return new SqlserverDepqrtment();
    }

    @Override
    public IUser CreateUser() {
        return new SqlserverUser();
    }
}
