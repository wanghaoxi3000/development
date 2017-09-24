package design.mode.builder;

/**
 * Created by whx3000 on 2017/2/26
 * you can contact me at: wanghaoxi3000@163.com
 */
class ConcreteBuilder1 extends Builder{
    private Product product = new Product();

    @Override
    public void BuildA() {
        product.Add("部件A");
    }

    @Override
    public void BuildB() {
        product.Add("部件B");
    }

    @Override
    public Product GetResult() {
        return product;
    }
}
