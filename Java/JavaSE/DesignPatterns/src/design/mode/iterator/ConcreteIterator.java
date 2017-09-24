package design.mode.iterator;

/**
 * Created by whx3000 on 2017/3/28
 * you can contact me at: wanghaoxi3000@163.com
 */
class ConcreteIterator implements Iterator {
    private ConcreteAggregate aggregate;
    private int current = 0;

    public ConcreteIterator(ConcreteAggregate aggregate) {
        this.aggregate = aggregate;
    }

    @Override
    public Object First() {
        return aggregate.getAggregate(0);
    }

    @Override
    public Object Next() {
        Object ret = null;
        current++;
        if (current < aggregate.getCount()) {
            ret = aggregate.getAggregate(current);
        }
        return ret;
    }

    @Override
    public boolean IsDone() {
        return current >= aggregate.getCount();
    }

    @Override
    public Object CurrentItem() {
        return aggregate.getAggregate(current);
    }
}
