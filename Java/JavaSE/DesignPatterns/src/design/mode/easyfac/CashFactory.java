package design.mode.easyfac;

/**
 * Created by whx3000 on 2017/2/4
 * you can contact me at: wanghaoxi3000@163.com
 */
class CashFactory {
    public static CashSuper createCashAccept(int type){
        CashSuper cs = null;
        switch (type){
            case 1:
                cs = new CashNormal();
                break;
            case 2:
                cs = new CashReturn("300", "100");
                break;
            case 3:
                cs = new CashRebate("0.8");
                break;
            default:
                break;
        }

        return cs;
    }
}
