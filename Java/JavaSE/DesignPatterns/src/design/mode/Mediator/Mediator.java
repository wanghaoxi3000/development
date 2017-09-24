package design.mode.Mediator;

/**
 * Created by whx3000 on 2017/4/6
 * you can contact me at: wanghaoxi3000@163.com
 */

//抽象中介者
abstract class AbstractMediator {
    public abstract void Send(String message, Colleage colleage);
}

//抽象同事类
abstract class Colleage {
    protected AbstractMediator mediator;

    public Colleage(AbstractMediator mediator) {
        this.mediator = mediator;
    }
}


class ConcreteColleague1 extends Colleage {
    public ConcreteColleague1(AbstractMediator mediator) {
        super(mediator);
    }

    public void send(String message)
    {
        mediator.Send(message, this);
    }

    public void Notify(String message)
    {
        System.out.println("同事1得到消息: " + message);
    }
}

class ConcreteColleague2 extends Colleage {
    public ConcreteColleague2(AbstractMediator mediator) {
        super(mediator);
    }

    public void send(String message)
    {
        mediator.Send(message, this);
    }

    public void Notify(String message)
    {
        System.out.println("同事2得到消息: " + message);
    }
}

//具体中介者类
class ConcreteMediator extends AbstractMediator {
    private ConcreteColleague1 colleague1;
    private ConcreteColleague2 colleague2;

    public void setColleague1(ConcreteColleague1 colleague1) {
        this.colleague1 = colleague1;
    }

    public void setColleague2(ConcreteColleague2 colleague2) {
        this.colleague2 = colleague2;
    }

    @Override
    public void Send(String message, Colleage colleage) {
        if(colleage == colleague1)
        {
            colleague2.Notify(message);
        }
        else
        {
            colleague1.Notify(message);
        }
    }
}

public class Mediator {
    public static void main(String args[]) {
        ConcreteMediator m = new ConcreteMediator();

        ConcreteColleague1 c1 = new ConcreteColleague1(m);
        ConcreteColleague2 c2 = new ConcreteColleague2(m);

        m.setColleague1(c1);
        m.setColleague2(c2);

        c1.send("吃过饭了吗");
        c2.send("没有, 你请客?");
    }
}

