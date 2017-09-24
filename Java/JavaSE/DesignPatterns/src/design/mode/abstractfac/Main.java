package design.mode.abstractfac;

import com.sun.xml.internal.bind.v2.model.core.ID;

/**
 * Created by wangh on 2017/3/14.
 * you can contact me at: wanghaoxi3000@163.com
 */
class Main {
    public static void main(String[] args){
        User user = new User();
        Department dept = new Department();

        IFactory factory = new AccessFactory();
        IUser iu = factory.CreateUser();
        iu.Inset(user);
        iu.GetUser(1);

        IDepartment id = factory.CreateDepartment();
        id.Insert(dept);
        id.GetDepartment(1);

        factory = new SqlServerFactory();
        iu = factory.CreateUser();
        iu.Inset(user);
        iu.GetUser(1);

        id = factory.CreateDepartment();
        id.Insert(dept);
        id.GetDepartment(1);
    }
}
