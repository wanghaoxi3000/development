{
    // 声明独一无二的变量
    let a1 = Symbol();
    let a2 = Symbol();
    console.log(a1 === a2);

    let a3 = Symbol.for('a3'); //检查a3是否在全局注册过，未注册过时返回新的Symbol,否则返回那个值，
    let a4 = Symbol.for('a3');
    console.log(a3 === a4);
}

{
    let a1=Symbol.for('abc');
    let obj={
        [a1]:'abc',
        'abc':345,
        'c':456
    };
    console.log('obk', obj);

    // 对象中的sybol属性通过let of无法取到
    for(let [key,value] of Object.entries(obj)){
        console.log('let of',key,value);
    }

    //取得Symbol方法
    Object.getOwnPropertySymbols(obj).forEach(function(item){
        console.log(obj[item]);
    })

    // 一起取得的办法
    Reflect.ownKeys(obj).forEach(function(item){
        console.log('ownkeys',item,obj[item]);
    })
}