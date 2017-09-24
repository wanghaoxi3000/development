package design.mode.factory;

/**
 * Created by whx3000 on 2017/2/13
 * you can contact me at: wanghaoxi3000@163.com
 */
class VolunteerFactory implements IFactory {
    @Override
    public LeiFeng CreateLeiFeng() {
        return new Volunteer();
    }
}
