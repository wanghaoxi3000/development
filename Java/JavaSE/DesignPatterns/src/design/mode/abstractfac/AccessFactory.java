package design.mode.abstractfac;

/**
 * Created by wangh on 2017/3/14.
 * you can contact me at: wanghaoxi3000@163.com
 */
class AccessFactory implements IFactory {
    @Override
    public IDepartment CreateDepartment() {
        return new AccessDepartment();
    }

    @Override
    public IUser CreateUser() {
        return new AccessUser();
    }
}
