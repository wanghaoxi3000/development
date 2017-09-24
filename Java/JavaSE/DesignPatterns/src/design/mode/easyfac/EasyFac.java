package design.mode.easyfac;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Created by whx3000 on 2017/2/4
 * you can contact me at: wanghaoxi3000@163.com
 *
 * 客户程序
 */
public class EasyFac {
    public static void main(String[] args){
        String total="0.0";
        String s = "1";

        try {
            System.out.print("请输入价格: ");
            BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
            total = stdin.readLine();
            System.out.println("价格: " + total);

            System.out.println("1.正常收费");
            System.out.println("2.满300返100");
            System.out.println("3.打8折");
            System.out.print("请输入计费方式: ");
            s = stdin.readLine();
            System.out.print("计费方式: " + s);
        } catch (IOException e) {
            e.printStackTrace();
        }

        double price;
        CashSuper csuper = CashFactory.createCashAccept(Integer.parseInt(s));
        price = csuper.acceptCash(Double.parseDouble(total));
        System.out.print("费用: " + price);

    }
}
