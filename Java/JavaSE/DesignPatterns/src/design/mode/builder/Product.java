package design.mode.builder;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by whx3000 on 2017/2/26
 * you can contact me at: wanghaoxi3000@163.com
 */
class Product {
    ArrayList<String> parts = new ArrayList<>();

    void Add(String part){
        parts.add(part);
    }

    void show(){
        System.out.println("\n 产品 创建---");
        for (String part: parts){
            System.out.println(part);
        }
    }
}
