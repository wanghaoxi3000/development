package design.mode.abstractfac;

/**
 * Created by whx3000 on 2017/2/26
 * you can contact me at: wanghaoxi3000@163.com
 */
interface IFactory {
    IUser CreateUser();
    IDepartment CreateDepartment();
}
