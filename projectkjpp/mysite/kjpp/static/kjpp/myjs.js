// TEST JAVASCRIPT

// function myFunction() {
//     alert("Hello from a static file!");
//   }

// var totalluas = document.getElementById("totalluas")
// var luassusuailist = document.getElementsByClassName("luassesuailist")
// function luasfunc(l){
//     // console.log(l.parentElement.children[11].value)
//     var luasValue = l.parentElement.children[11].value 
//     // ini buat grab elementnya, yg bawah ini juga sama aja soalnya cuma ngambil 1 value
//     // console.log(l.value)
//     // console.log(l.parentElement.parentElement.children[1].children[1])
//     l.parentElement.parentElement.children[1].children[1].innerHTML = luasValue
//     // console.log(luasValue)
// }

var totalluas = document.getElementById("totalluas")
var luassusuailist = document.getElementsByClassName("luassesuailist")
function luasfunc(l){
    var luasValue = l.parentElement.children[11].value 
    // Check if luasValue is null, empty, or consists only of whitespace
    if (!luasValue.trim()) {
        luasValue = '0';
    }
    l.parentElement.parentElement.children[1].children[1].innerHTML = luasValue
}