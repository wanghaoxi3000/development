package design.mode.easyfac;

/**
 * Created by whx3000 on 2017/2/4
 * you can contact me at: wanghaoxi3000@163.com
 *
 * 打折收费子类
 */
class CashRebate extends CashSuper {

    private double moneyRebate = 1d;

    public CashRebate(String moneyRebate){
        this.moneyRebate = Double.parseDouble(moneyRebate);
    }

    @Override
    public double acceptCash(double money) {
        return money * moneyRebate;
    }
}
