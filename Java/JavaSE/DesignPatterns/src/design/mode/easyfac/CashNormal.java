package design.mode.easyfac;

/**
 * Created by whx3000 on 2017/2/4
 * you can contact me at: wanghaoxi3000@163.com
 *
 * 正常收费子类
 */
class CashNormal extends CashSuper {

    @Override
    public double acceptCash(double money) {
        return money;
    }
}
