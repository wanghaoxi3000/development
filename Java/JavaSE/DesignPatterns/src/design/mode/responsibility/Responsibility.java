package design.mode.responsibility;

/**
 * Created by whx3000 on 2017/4/6
 * you can contact me at: wanghaoxi3000@163.com
 */

// 处理请示的接口
abstract class Handler {
    protected Handler successor;

    public void setSuccessor(Handler successor) {
        this.successor = successor;
    }

    public abstract void HandleRequest(int request);
}

// 具体处理者类, 处理0-10之前的请求, 否则转交下一位
class ConcreteHandler1 extends Handler {
    @Override
    public void HandleRequest(int request) {
        if (request >= 0 && request < 10) {
            System.out.println(this.getClass().getSimpleName() + "处理请求" + request);
        }
        else if (successor != null) {
            successor.HandleRequest(request);
        }
    }
}

// 具体处理者类, 处理10-20之前的请求, 否则转交下一位
class ConcreteHandler2 extends Handler {
    @Override
    public void HandleRequest(int request) {
        if (request >= 10 && request < 20) {
            System.out.println(this.getClass().getSimpleName() + "处理请求" + request);
        }
        else if (successor != null) {
            successor.HandleRequest(request);
        }
    }
}

// 具体处理者类, 处理20-30之前的请求, 否则转交下一位
class ConcreteHandler3 extends Handler {
    @Override
    public void HandleRequest(int request) {
        if (request >= 20 && request < 30) {
            System.out.println(this.getClass().getSimpleName() + "处理请求" + request);
        }
        else if (successor != null) {
            successor.HandleRequest(request);
        }
    }
}

class Responsibility {
    public static void main(String args[]) {
        Handler h1 = new ConcreteHandler1();
        Handler h2 = new ConcreteHandler2();
        Handler h3 = new ConcreteHandler3();

        h1.setSuccessor(h2);
        h2.setSuccessor(h3);

        int[] requests = {2, 5, 14, 22, 18, 3, 27, 20};
        for(int request: requests){
            h1.HandleRequest(request);
        }
    }
}
