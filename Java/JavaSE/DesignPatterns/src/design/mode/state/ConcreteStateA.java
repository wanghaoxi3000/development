package design.mode.state;

/**
 * Created by wangh on 2017/3/18.
 * you can contact me at: wanghaoxi3000@163.com
 */
class ConcreteStateA extends State{
    @Override
    public void Handle(Context context) {
        context.setState(new ConcreteStateB());
    }
}
