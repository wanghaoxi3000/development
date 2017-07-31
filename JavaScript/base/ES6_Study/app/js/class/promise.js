{
    // 基本定义
    let ajax=function(callback){
        console.log('执行');
        setTimeout(function (){
            callback&&callback.call()
        }, 1000)
    };

    ajax(function(){
        console.log('timeout1');
    })
}

{
    let ajax=function(){
        console.log('执行2');
        return new Promise(function(resolve, reject){
            setTimeout(function () {
                resolve()
            })
        }, 1000)
    }

    ajax().then(function(){
        console.log('promise', 'timeout2');
    })
}

{
       let ajax=function(){
        console.log('执行3');
        return new Promise(function(resolve, reject){
            setTimeout(function () {
                resolve()
            })
        }, 1000)
    }

    ajax().then(function(){
        return new Promise(function(resolve, reject){
            setTimeout(function () {
                resolve()
            }, 2000);
        });
    })
        .then(function(){
            console.log('timeout3');
        })
}

{
    let ajax=function(num){
        console.log('执行4');
        return new Promise(function(resolve, reject){
            if(num > 5){
                resolve()
            }else{
                throw new Error('出错了')
            }
        })
    }

    ajax(6).then(function(){
        console.log('log', 6);
    }).catch(function(err){
        console.log('catch', err)
    })

    ajax(3).then(function(){
        console.log('log', 3);
    }).catch(function(err){
        console.log('catch', err)
    })
}

{
    // 所有图片加载完后再添加到页面
    function loadImag(src){
        return new Promise((resolve, reject)=>{
            let img=document.createElement('img');
            img.src=src;
            img.onload=function(){
                resolve(img);
            }
            img.onerror=function(err){
                reject(err);
            }
        })
    }

    function showImgs(imgs){
        imgs.forEach(function(img) {
            document.body.appendChild(img)
        })
    }

    // 将多个Promise实例转换成一个实例
    Promise.all([
        loadImag('http://i1.piimg.com/567571/342fa006602e030c.jpg'),
        loadImag('http://i1.piimg.com/567571/6f9db76e4824ae39.jpg'),
        loadImag('http://ohyn8f189.bkt.clouddn.com/17-2-8/8377678-file_1486565861206_19f8.jpg'),
    ]).then(showImgs)
}

{
    // 有一个图片加载完就添加到页面
    function loadImag(src){
        return new Promise((resolve, reject)=>{
            let img=document.createElement('img');
            img.src=src;
            img.onload=function(){
                resolve(img);
            }
            img.onerror=function(err){
                reject(err);
            }
        })
    }

    function showImgs(img){
        let p = document.createElement('p');
        p.appendChild(img);
        document.body.appendChild(p);
    }

    // 响应多个Promise实例中最先完成的那个
    Promise.race([
        loadImag('http://i1.piimg.com/567571/342fa006602e030c.jpg'),
        loadImag('http://i1.piimg.com/567571/6f9db76e4824ae39.jpg'),
        loadImag('http://ohyn8f189.bkt.clouddn.com/17-2-8/8377678-file_1486565861206_19f8.jpg'),
    ]).then(showImgs)
}