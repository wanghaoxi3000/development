{
    let list = new Set();

    list.add(5);
    list.add(7);

    console.log('size', list.size);
}

{
    let arr = [1,2,3,4,5];
    let list = new Set(arr);

    console.log('size', list.size);
}

{
    let list = new Set();

    list.add(1);
    list.add(2);
    list.add(1);
    console.log('list', list);

    let arr = [1, 2, 3, 1, 2];
    let list2 = new Set(arr);
    console.log('list', list2);

    let arr2 = [1, 2, 3, 1, '2'];
    let list3 = new Set(arr2);
    console.log('list', list3);
}

{
    let arr = ['add', 'delete', 'clear', 'has'];
    let list = new Set(arr);

    console.log('has', list.has('add'));
    console.log('delete', list.delete('add'), list);
    list.clear();
    console.log('clear', list);
}

{
    let arr = ['add', 'delete', 'clear', 'has'];
    let list = new Set(arr);

    for(let key of list.keys()){
        console.log('keys', key);
    }

    for(let value of list.values()){
        console.log('value', value);
    }

    for(let [key, value] of list.entries()){
        console.log('entries', key, value);
    }

    list.forEach(function(item){console.log(item);})
}

{
    // WeakSet
    // 1. 元素只能是对象
    // 2. WeakSet中都是地址拷贝，并且不会检查是否已被垃圾回收
    let weakList = new WeakSet();

    let arg={};
    weakList.add(arg);
}

{
    let map = new Map();
    let arr = ['123'];

    map.set(arr, 456);
    console.log('map', map, map.get(arr));
}

{
    let map = new Map([['a', 123], ['b', 456]]);
    console.log('map args', map);
    console.log('map size', map.size);
    console.log('map delete', map.delete('a'), map);
    console.log('map clear', map.clear(), map);
}

{
    let weakmap = new WeakMap();

    let o = {};
    weakmap.set(o, 123);
    console.log(weakmap.get(o));
}

{
    // 数据结构横向对比，增，查，改，删
    let map = new Map;
    let array = [];

    // 增
    map.set('t', 1);
    array.push({t:1});
    console.info('map-array', map, array);

    // 查
    let map_exist = map.has('t');
    let array_exist = array.find(item=>item.t);
    console.info('map-array', map_exist, array_exist);

    // 改
    map.set('t', 2);
    array.forEach(item=>item.t?item.t=2:'');
    console.info('map-modify', map, array);

    // 删除
    map.delete('t')
    let index = array.findIndex(item=>item.t);
    array.splice(index, 1);
    console.info('map-array-empty', map, array);
}

{
    // set和array的对比
    let set = new Set();
    let array = [];

    // 增
    set.add({t:1})
    array.push({t:1});
    console.info('set-array', set, array);

    // 查
    let set_exist = set.has({t:1}); // 新的引用，结果为false
    let array_exist = array.find(item=>item.t);
    console.info('set-array', set_exist, array_exist);

    // 改
    set.forEach(item=>item.t?item.t=2:'');
    array.forEach(item=>item.t?item.t=2:'');
    console.info('set-array', set, array);

    // 删
    set.forEach(item=>item.t?set.delete(item):'');
    let index = array.findIndex(item=>item.t);
    array.splice(index, 1);
    console.info('set-array-empty', set, array);
}

{
    // map, set, object对比
    let item={t:1};
    let map = new Map();
    let set = new Set();
    let obj = {};

    // 增
    map.set('t', 1);
    set.add(item);
    obj['t'] = 1;
    console.log('map-set-obj', obj, map, set);

    // 查
    console.info({
        map_exist: map.has('t'),
        set_exist:set.has(item),
        obj_exist:'t' in obj
    })

    // 改
    map.set('t', 2);
    item.t = 2;
    obj['t'] = 2;
    console.log('map-set-obj', obj, map, set);

    // 删除
    map.delete('t');
    set.delete(item);
    delete obj['t'];
    console.log('map-set-obj', obj, map, set);
}

// 数据结构优先考虑map set，放弃使用object和array来做存储
