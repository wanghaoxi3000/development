package design.mode.strategy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Created by whx3000 on 2017/2/4
 * you can contact me at: wanghaoxi3000@163.com
 */
public class Strategy {
    public static void main(String[] args){
        CashContext cc;
        String total = "0.0";
        String s = "1";

        BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));

        try {
            System.out.print("请输入价格: ");
            total = stdin.readLine();

            System.out.print("请输入计费方式: ");
            s = stdin.readLine();
            System.out.println("价格: " + total + "策略: " + s);

        } catch (IOException e){
            e.printStackTrace();
        }

        cc = new CashContext(s);

        double price;
        price = cc.GetResult(Double.parseDouble(total));
        System.out.println("费用: " + price);
    }
}
