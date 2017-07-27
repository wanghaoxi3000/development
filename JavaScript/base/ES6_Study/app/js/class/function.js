{
    function test(x, y='world'){
        console.log('默认值', x, y);
    }
    test('hello');
    test('hello', 'kill');
}

{
    //x的作用域
    let x='test';
    function test2(x, y=x){
        console.log('作用域', x, y);
    }
    test2('kill');
}

{
    // ...arg将参数转换为数组
    function test3(...arg){
        for(let v of arg){
            console.log('rest', v);
        }
    }
    test3(1,2,3,4,'a');
}

{
    console.log(...[1,2,4]);
    console.log('a', ...[1,2,4]);
}

{
    let arrow=v => v*2;
    let arrow2 = (v,k) => v*k;

    console.log(arrow(3));
    console.log(arrow2(2, 3));
}

{
    //尾调用
    function tail(x){
        console.log('tail', x);
    }
    function fx(x){
        return tail(x);
    }
    fx(123)
}