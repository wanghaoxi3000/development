package design.mode.strategy;

/**
 * Created by whx3000 on 2017/2/4
 * you can contact me at: wanghaoxi3000@163.com
 *
 * 策略模式上下文
 */
class CashContext {
    private CashSuper cs;

    public CashContext(String s){
        switch (s){
            case "1":
                cs = new CashNormal();
                break;

            case "2":
                cs = new CashRebate("0.8");
                break;

            case "3":
                cs = new CashReturn("300", "100");
                break;

            default:
                break;
        }
    }

    public double GetResult(double money){
        return cs.acceptCash(money);
    }
}
