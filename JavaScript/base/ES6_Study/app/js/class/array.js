{
    let arr = Array.of(3, 4, 5, 9, 11);
    console.log(arr);

    //of参数为空时，返回空数组
    let empty = Array.of();
    console.log(empty);
}

{
    let p = document.querySelectorAll('p'); //返回一组集合
    let pArr = Array.from(p);   //将集合转换成数据
    pArr.forEach(function(item){
        console.log(item.textContent);
    })

    console.log(Array.from([1, 3, 5], function(item){return item*2}));
}

{
    console.log('fill-7', [1, 'a', undefined].fill(7));
    console.log('fill, pos', ['a', 'b', 'c'].fill(7, 1, 3));    //替换
}

{
    for(let index of ['1', 'c', 'ks'].keys()){
        console.log('keys', index);
    }

    for(let values of ['1', 'c', 'ks'].values()){
        console.log('values', values);
    }

        for(let [index, value] of ['1', 'c', 'ks'].entries()){
        console.log('values', index, value);
    }
}

{
    console.log([1, 2, 3, 4, 5, 6].copyWithin(0, 3, 5));
}

{
    //find 查找符合条件的第一个元素
    console.log([1, 2, 3, 4, 5, 6].find(function(item){return item>3}));

    console.log([1, 2, 3, 4, 5, 6].findIndex(function(item){return item>3}));
}

{
    console.log('number', [1,2,NaN].includes(1));
    console.log('number', [1,2,NaN].includes(NaN));
}