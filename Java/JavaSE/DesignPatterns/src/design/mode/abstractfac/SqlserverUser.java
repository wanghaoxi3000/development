package design.mode.abstractfac;

/**
 * Created by wangh on 2017/3/14.
 * you can contact me at: wanghaoxi3000@163.com
 */

class SqlserverUser implements IUser{
    @Override
    public void Inset(User user) {
        System.out.println("在SQL Server中User表增加一条记录");
    }

    @Override
    public User GetUser(int id) {
        System.out.println("在SQL Server中根据ID得到User中一条记录");
        return null;
    }
}
