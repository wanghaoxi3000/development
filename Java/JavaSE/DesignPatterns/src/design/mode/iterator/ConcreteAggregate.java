package design.mode.iterator;

import java.util.LinkedList;
import java.util.List;

/**
 * Created by whx3000 on 2017/3/28
 * you can contact me at: wanghaoxi3000@163.com
 */
class ConcreteAggregate<T> extends Aggregate{
    private List<T> items = new LinkedList<>();
    public int Count;

    @Override
    public Iterator CreateIterator() {
        return new ConcreteIterator(this);
    }

    public int getCount() {
        Count = items.size();
        return Count;
    }

    public T getAggregate(int i) {
        return items.get(i);
    }

    public void addAggregate(int i, T value) {
        items.add(i, value);
    }

}
