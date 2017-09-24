package design.mode.observer;

/**
 * Created by whx3000 on 2017/3/8
 * you can contact me at: wanghaoxi3000@163.com
 */
class ConcreteObserver extends Observer {
    private String name;
    private String observerState;

    public ConcreteSubject getSubject() {
        return subject;
    }

    public void setSubject(ConcreteSubject subject) {
        this.subject = subject;
    }

    private ConcreteSubject subject;

    public ConcreteObserver(ConcreteSubject subject, String name){
        this.subject = subject;
        this.name = name;
    }

    @Override
    public void update() {
        observerState = subject.getSubjectState();
        System.out.println("观察者:" + name + "新状态是:" + observerState);
    }


}
