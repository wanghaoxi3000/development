{
    // 两种构造方式，i表示忽略大小写
    let regex = new RegExp('xyz', 'i');
    let regex2 = new RegExp(/xyz/i);

    console.log(regex.test('xyz123'), regex2.test('xyz123'));

    // ES6中允许第二个参数再次指定修饰符，但是会覆盖第一个正则表达式中的修饰符
    let regex3 = new RegExp(/xyz/ig, 'i');
    console.log(regex3.flags);  //获取正则的修饰属性
}

{
    let s = 'bbb_bb_b';
    let a1 = /b+/g;
    let a2 = /b+/y;

    //g和y都是全局匹配，g在上一次匹配后的任意位置匹配，
    //y必须是上一次匹配后紧接着的位置匹配
    console.log('one', a1.exec(s), a2.exec(s));
    console.log('two', a1.exec(s), a2.exec(s));
    console.log(a1.sticky, a2.sticky);  //检查是否开启y修饰符
    
    //one ["bbb", index: 0, input: "bbb_bb_b"] ["bbb", index: 0, input: "bbb_bb_b"]
    //index.js:84 two ["bb", index: 4, input: "bbb_bb_b"] null
}

{
    //u会将'\uD83D\uDC2A'4字节当做一个字符，以适应Unicode
    console.log('u-1', /^\uD83D/.test('\uD83D\uDC2A'));
    console.log('u-2', /^\uD83D/u.test('\uD83D\uDC2A'));

    //u-1 true
    //u-2 false

    console.log(/\u{61}/.test('a'));
    console.log(/\u{61}/u.test('a'));

    //false
    //true

    //如果字符串中存在大于两个字节的字符，需要加u修饰符才能使.匹配任意字符
    console.log('\u{20BB7}');
    let s = '𠮷';
    console.log('u-3', /^.$/u.test(s));

    //false

    //使用u识别大于2个字节的字符
    console.log('u-4', /𠮷{2}/.test('𠮷𠮷'));;
    console.log('u-5', /𠮷{2}/u.test('𠮷𠮷'));;

    //false
    //true

    //换行符，回车符，行分隔符，段分隔符这些'.'也不能识别
    //需要通过s修饰符，但ES6尚未实现
}

