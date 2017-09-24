package design.mode.command;

/**
 * Created by whx3000 on 2017/3/31
 * you can contact me at: wanghaoxi3000@163.com
 */

//Command类, 用来声明执行操作的接口
abstract class Command {
    protected Receiver receiver;

    public Command(Receiver receiver) {
        this.receiver = receiver;
    }
    abstract public void Execute();
}


//Receiver类, 知道如何施行与执行一个与请求相关的操作,任何类都可能作为一个接收者
class Receiver {
    public void Action() {
        System.out.println("Exec Command !");
    }
}


//Invoker类, 要求该命令执行这个请求
class Invoker {
    private Command command;

    public void setCommand(Command command) {
        this.command = command;
    }

    public void ExecuteCommand() {
        command.Execute();
    }
}

//ConcreteCommand类, 将一个接收者对象绑定一个动作, 调用接收者相应的操作, 以实现Execute
class ConcreteCommand extends Command{
    public ConcreteCommand(Receiver receiver) {
        super(receiver);
    }

    @Override
    public void Execute() {
        receiver.Action();
    }
}

