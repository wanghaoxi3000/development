package design.mode.proxy;

/**
 * Created by whx3000 on 2017/2/9
 * you can contact me at: wanghaoxi3000@163.com
 */
class Pursuit implements GiveGift {
    private SchoolGirl mm;

    public Pursuit(SchoolGirl mm) {
        this.mm = mm;
    }

    @Override
    public void GiveDolls() {
        System.out.println("Give " + mm.getName() + " dolls");
    }

    @Override
    public void GiveFlowers() {
        System.out.println("Give " + mm.getName() + " flowers");
    }

    @Override
    public void GiveChocolate() {
        System.out.println("Give " + mm.getName() + " chocolates");
    }
}
