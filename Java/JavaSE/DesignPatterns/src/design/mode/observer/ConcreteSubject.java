package design.mode.observer;

/**
 * Created by whx3000 on 2017/3/8
 * you can contact me at: wanghaoxi3000@163.com
 */
class ConcreteSubject extends Subject {
    private String subjectState;

    public String getSubjectState() {
        return subjectState;
    }

    public void setSubjectState(String subjectState) {
        this.subjectState = subjectState;
    }
}
