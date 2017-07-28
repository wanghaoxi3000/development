{
    // 基本定义和生成实例
    class Parent{
        constructor(name='mukewang'){
            this.name = name;
        }
    }

    let v_parent = new Parent('v');
    console.log('构造函数和实例', v_parent);
}

{
    // 继承及传递参数
    class Parent{
        constructor(name='mukewang'){
            this.name = name;
        }
    }

    class Child extends Parent{
        constructor(name='child'){
            super(name);    // super必须在第一行
            this.type='child';
        }
    }

    console.log('继承', new Child('hello'));
}

{
    // 继承及传递参数
    class Parent{
        constructor(name='mukewang'){
            this.name = name;
        }

        get longName(){ // 属性非函数
            return 'mk' + this.name
        }

        set longName(value){
            this.name = value;
        }
    }

    let v = new Parent();
    console.log('getter', v.longName);
    v.longName = 'hello';
    console.log('setter', v.longName)
}

{
    // 静态方法
    class Parent{
        constructor(name='mukewang'){
            this.name = name;
        }

        static tell() {
            console.log('tell');
        }
    }

    Parent.tell();
}

{
    // 静态属性
    class Parent{
        constructor(name='mukewang'){
            this.name = name;
        }

        static tell() {
            console.log('tell');
        }
    }

    Parent.type = 'test';
    console.log('静态属性', Parent.type)
}