var items = ["item1", "item2", "item3", "item4", "item5"]

for (var idx in items){
	var item = document.getElementById(items[idx])
	console.log(items[idx])
	console.log(item)
	item.ondragstart = function(event) {
		console.log("start")
		console.log(this.id)
		console.log(event)
	event.dataTransfer.setData("text", this.id) // require important
	var target = document.getElementById(this.id)
	target.style.opacity = ".5"
	target.style.zIndex = "100"
}
item.ondragend = function (event) {
	console.log("end")
	console.log(this.id)
	console.log(event)
	var target = document.getElementById(this.id)
	target.style.zIndex = ""
	target.style.opacity = ""
}
item.ondrag = function (event) {
	console.log("drag")
	console.log(event)
}
item.ondragover = function (event) {
	// console.log("over")
	event.preventDefault()	// and ondrop require important
}
item.ondrop = function (event) {
	event.preventDefault()	// and ondragover require important
	console.log("drop")
	console.log(event)
	var data = event.dataTransfer.getData("text");
	console.log("data")
	console.log( data )
}
}
