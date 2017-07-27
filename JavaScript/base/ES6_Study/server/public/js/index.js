/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};

/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {

/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;

/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};

/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;

/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}


/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;

/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;

/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";

/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports, __webpack_require__) {

	module.exports = __webpack_require__(1);


/***/ }),
/* 1 */
/***/ (function(module, exports, __webpack_require__) {

	'use strict';

	__webpack_require__(2);

/***/ }),
/* 2 */
/***/ (function(module, exports) {

	'use strict';

	var _slicedToArray = function () { function sliceIterator(arr, i) { var _arr = []; var _n = true; var _d = false; var _e = undefined; try { for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"]) _i["return"](); } finally { if (_d) throw _e; } } return _arr; } return function (arr, i) { if (Array.isArray(arr)) { return arr; } else if (Symbol.iterator in Object(arr)) { return sliceIterator(arr, i); } else { throw new TypeError("Invalid attempt to destructure non-iterable instance"); } }; }();

	{
	    var list = new Set();

	    list.add(5);
	    list.add(7);

	    console.log('size', list.size);
	}

	{
	    var arr = [1, 2, 3, 4, 5];
	    var _list = new Set(arr);

	    console.log('size', _list.size);
	}

	{
	    var _list2 = new Set();

	    _list2.add(1);
	    _list2.add(2);
	    _list2.add(1);
	    console.log('list', _list2);

	    var _arr = [1, 2, 3, 1, 2];
	    var list2 = new Set(_arr);
	    console.log('list', list2);

	    var arr2 = [1, 2, 3, 1, '2'];
	    var list3 = new Set(arr2);
	    console.log('list', list3);
	}

	{
	    var _arr2 = ['add', 'delete', 'clear', 'has'];
	    var _list3 = new Set(_arr2);

	    console.log('has', _list3.has('add'));
	    console.log('delete', _list3.delete('add'), _list3);
	    _list3.clear();
	    console.log('clear', _list3);
	}

	{
	    var _arr3 = ['add', 'delete', 'clear', 'has'];
	    var _list4 = new Set(_arr3);

	    var _iteratorNormalCompletion = true;
	    var _didIteratorError = false;
	    var _iteratorError = undefined;

	    try {
	        for (var _iterator = _list4.keys()[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
	            var key = _step.value;

	            console.log('keys', key);
	        }
	    } catch (err) {
	        _didIteratorError = true;
	        _iteratorError = err;
	    } finally {
	        try {
	            if (!_iteratorNormalCompletion && _iterator.return) {
	                _iterator.return();
	            }
	        } finally {
	            if (_didIteratorError) {
	                throw _iteratorError;
	            }
	        }
	    }

	    var _iteratorNormalCompletion2 = true;
	    var _didIteratorError2 = false;
	    var _iteratorError2 = undefined;

	    try {
	        for (var _iterator2 = _list4.values()[Symbol.iterator](), _step2; !(_iteratorNormalCompletion2 = (_step2 = _iterator2.next()).done); _iteratorNormalCompletion2 = true) {
	            var value = _step2.value;

	            console.log('value', value);
	        }
	    } catch (err) {
	        _didIteratorError2 = true;
	        _iteratorError2 = err;
	    } finally {
	        try {
	            if (!_iteratorNormalCompletion2 && _iterator2.return) {
	                _iterator2.return();
	            }
	        } finally {
	            if (_didIteratorError2) {
	                throw _iteratorError2;
	            }
	        }
	    }

	    var _iteratorNormalCompletion3 = true;
	    var _didIteratorError3 = false;
	    var _iteratorError3 = undefined;

	    try {
	        for (var _iterator3 = _list4.entries()[Symbol.iterator](), _step3; !(_iteratorNormalCompletion3 = (_step3 = _iterator3.next()).done); _iteratorNormalCompletion3 = true) {
	            var _step3$value = _slicedToArray(_step3.value, 2),
	                _key = _step3$value[0],
	                _value = _step3$value[1];

	            console.log('entries', _key, _value);
	        }
	    } catch (err) {
	        _didIteratorError3 = true;
	        _iteratorError3 = err;
	    } finally {
	        try {
	            if (!_iteratorNormalCompletion3 && _iterator3.return) {
	                _iterator3.return();
	            }
	        } finally {
	            if (_didIteratorError3) {
	                throw _iteratorError3;
	            }
	        }
	    }

	    _list4.forEach(function (item) {
	        console.log(item);
	    });
	}

	{
	    // WeakSet
	    // 1. 元素只能是对象
	    // 2. WeakSet中都是地址拷贝，并且不会检查是否已被垃圾回收
	    var weakList = new WeakSet();

	    var arg = {};
	    weakList.add(arg);
	}

	{
	    var map = new Map();
	    var _arr4 = ['123'];

	    map.set(_arr4, 456);
	    console.log('map', map, map.get(_arr4));
	}

	{
	    var _map = new Map([['a', 123], ['b', 456]]);
	    console.log('map args', _map);
	    console.log('map size', _map.size);
	    console.log('map delete', _map.delete('a'), _map);
	    console.log('map clear', _map.clear(), _map);
	}

	{
	    var weakmap = new WeakMap();

	    var o = {};
	    weakmap.set(o, 123);
	    console.log(weakmap.get(o));
	}

	{
	    // 数据结构横向对比，增，查，改，删
	    var _map2 = new Map();
	    var array = [];

	    // 增
	    _map2.set('t', 1);
	    array.push({ t: 1 });
	    console.info('map-array', _map2, array);

	    // 查
	    var map_exist = _map2.has('t');
	    var array_exist = array.find(function (item) {
	        return item.t;
	    });
	    console.info('map-array', map_exist, array_exist);

	    // 改
	    _map2.set('t', 2);
	    array.forEach(function (item) {
	        return item.t ? item.t = 2 : '';
	    });
	    console.info('map-modify', _map2, array);

	    // 删除
	    _map2.delete('t');
	    var index = array.findIndex(function (item) {
	        return item.t;
	    });
	    array.splice(index, 1);
	    console.info('map-array-empty', _map2, array);
	}

	{
	    // set和array的对比
	    var set = new Set();
	    var _array = [];

	    // 增
	    set.add({ t: 1 });
	    _array.push({ t: 1 });
	    console.info('set-array', set, _array);

	    // 查
	    var set_exist = set.has({ t: 1 }); // 新的引用，结果为false
	    var _array_exist = _array.find(function (item) {
	        return item.t;
	    });
	    console.info('set-array', set_exist, _array_exist);

	    // 改
	    set.forEach(function (item) {
	        return item.t ? item.t = 2 : '';
	    });
	    _array.forEach(function (item) {
	        return item.t ? item.t = 2 : '';
	    });
	    console.info('set-array', set, _array);

	    // 删
	    set.forEach(function (item) {
	        return item.t ? set.delete(item) : '';
	    });
	    var _index = _array.findIndex(function (item) {
	        return item.t;
	    });
	    _array.splice(_index, 1);
	    console.info('set-array-empty', set, _array);
	}

	{
	    // map, set, object对比
	    var item = { t: 1 };
	    var _map3 = new Map();
	    var _set = new Set();
	    var obj = {};

	    // 增
	    _map3.set('t', 1);
	    _set.add(item);
	    obj['t'] = 1;
	    console.log('map-set-obj', obj, _map3, _set);

	    // 查
	    console.info({
	        map_exist: _map3.has('t'),
	        set_exist: _set.has(item),
	        obj_exist: 't' in obj
	    });

	    // 改
	    _map3.set('t', 2);
	    item.t = 2;
	    obj['t'] = 2;
	    console.log('map-set-obj', obj, _map3, _set);

	    // 删除
	    _map3.delete('t');
	    _set.delete(item);
	    delete obj['t'];
	    console.log('map-set-obj', obj, _map3, _set);
	}

	// 数据结构优先考虑map set，放弃使用object和array来做存储

/***/ })
/******/ ]);