package design.mode.iterator;

/**
 * Created by whx3000 on 2017/3/28
 * you can contact me at: wanghaoxi3000@163.com
 */
interface Iterator {
    Object First();
    Object Next();
    boolean IsDone();
    Object CurrentItem();
}
