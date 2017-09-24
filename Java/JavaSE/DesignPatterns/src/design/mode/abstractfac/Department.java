package design.mode.abstractfac;

/**
 * Created by wangh on 2017/3/14.
 * you can contact me at: wanghaoxi3000@163.com
 */
class Department {
    public int get_id() {
        return _id;
    }

    public void set_id(int _id) {
        this._id = _id;
    }

    private int _id;

    public String get_name() {
        return _name;
    }

    public void set_name(String _name) {
        this._name = _name;
    }

    private String _name;
}
