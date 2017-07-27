{
    let a, b, rest;
    [a, b]=[1, 2];

    console.log(a, b);
}

{
    let a, b, c, rest;
    [a, b, c]=[1, 2];

    console.log(a, b, c);
}
//output: 1 2 3

{
    let a, b, rest;
    [a, b, ...rest] = [1, 2, 3, 4, 5, 6];
    console.log(a, b, rest);
}


{
    function f(){
        return [1, 2, 3, 4, 5]
    }
    let a, b, c;
    [a, ...b] = f();
    console.log(a, b);
}
//output: 1 [2, 3, 4, 5]

{
    let metaData={
        title: 'abc',
        test: [{
            title: 'test',
            desc: 'description'
        }]
    }

    let {title:esTitle, test:[{title:cnTitle}]} = metaData;
    console.log(esTitle, cnTitle);
}

