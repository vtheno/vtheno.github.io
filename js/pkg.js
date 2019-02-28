var Pkg = {
    print: function (obj) {
	console.log(obj)
    },
    getElementById: function (id) {
	return function () { return document.getElementById(id) }
    },
    Task: function (ms) {
	let _ret = {
	    _ms: typeof ms == 'number' ? ms : 10,
	    tasks: [],
	}
	function addTask(handler) {
            if (typeof handler == 'function' && handler.length == 0) {
		_ret.tasks.push(handler)
		return _ret.tasks.length - 1
            } else {
		throw "addTask: (unit -> unit) -> int; handler: unit -> unit"
            }
	}
	function removeTask(id) {
            if (typeof id == 'number') {
		_ret.tasks.splice(id, 1)
		return null
            } else {
		throw 'removeTask: int -> unit'
            }
	}
	_ret.add = addTask
	_ret.remove = removeTask
	function mainThread() {
            for (var i in _ret.tasks) {
		_ret.tasks[i]()
            }
	}
	let main = setInterval(mainThread, ms)
	function stop() {
            clearInterval(main)
	}
	_ret.stop = stop
	return _ret
    },
    Element: function(data) {
	let _self = null
	if (data.id){
	    _self = Pkg.getElementById(_data.id)
	}
	let _ret = {}
	_ret.then = function(handler){
	    handler(_self())
	    return _ret
	}
	return _ret
    },
    is_mobile: function () {
	return document.getElementsByTagName("body")[0].clientWidth < 678
    },
    Request: function () {
	let httpRequest = new XMLHttpRequest()
	let obj = {
            url: "/",
            method: "GET",
            data: null,
            stack: [],
	}
	obj.then = function (handler) {
	    if (typeof handler != 'function'){
		throw "handler : Response -> unit"
	    }
            httpRequest.open(obj.method, obj.url, true)
            for (var i in obj.stack) {
		obj.stack[i]()
            }
            httpRequest.onreadystatechange = function () {
		print(httpRequest.readyState)
		if (httpRequest.readyState == XMLHttpRequest.DONE && httpRequest.status == 200) {
                    handler(JSON.parse(httpRequest.responseText))
		}
            }
            httpRequest.send(obj.data)
	}
	obj.push = function (key, value) {
            obj.stack.push(function () {
		httpRequest.setRequestHeader(key, value)
            })
	}
	obj.set = function (handler) {
	    if (typeof handler != 'function'){
		throw "handler : Request -> Request"
	    }
            handler(obj)
            return obj
	}
	return obj
    },
    $: function(id_name) {
	return Pkg.Element({id: id_name})
    }
}
