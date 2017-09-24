package design.mode.command;

/**
 * Created by whx3000 on 2017/3/31
 * you can contact me at: wanghaoxi3000@163.com
 */
class Main {
    public static void main(String[] args) {
        Receiver r = new Receiver();
        Command c = new ConcreteCommand(r);
        Invoker i = new Invoker();

        i.setCommand(c);
        i.ExecuteCommand();
    }
}
