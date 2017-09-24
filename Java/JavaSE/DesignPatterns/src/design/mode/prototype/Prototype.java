package design.mode.prototype;

/**
 * Created by whx3000 on 2017/2/15
 * you can contact me at: wanghaoxi3000@163.com
 */
class Prototype implements Cloneable {
    private String id;

    Prototype(String id) {
        this.id = id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getId() {
        return id;
    }

    @Override
    protected Object clone() {
        Object object = null;
        try {
            object = super.clone();
        } catch (CloneNotSupportedException e) {
            System.err.println("Prototype is not Cloneable");
        }
        return object;
    }
}
