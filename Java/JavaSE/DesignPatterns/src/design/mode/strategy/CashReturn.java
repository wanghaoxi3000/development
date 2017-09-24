package design.mode.strategy;

/**
 * Created by whx3000 on 2017/2/4
 * you can contact me at: wanghaoxi3000@163.com
 *
 * 返利收费子类
 */
class CashReturn extends CashSuper {
    private double moneyCondition = 0.0d;
    private double moneyReturn = 0.0d;

    public CashReturn(String moneyCondition, String moneyReturn){
        this.moneyCondition = Double.parseDouble(moneyCondition);
        this.moneyReturn = Double.parseDouble(moneyReturn);
    }

    @Override
    public double acceptCash(double money) {
        double result = money;
        if (money >= moneyCondition){
            result = money - Math.floor(money / moneyCondition) * moneyReturn;
        }

        return result;
    }
}
