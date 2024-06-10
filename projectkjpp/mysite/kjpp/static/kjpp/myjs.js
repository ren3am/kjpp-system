// TEST JAVASCRIPT

// function myFunction() {
//     alert("Hello from a static file!");
//   }

// var totalluas = document.getElementById("totalluas")
// var luassusuailist = document.getElementsByClassName("luassesuailist")
// function luasfunc(l){
//     console.log(l.parentElement.children[11].value)
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

    // var result = luasValue*2 (INI TEST)

    l.parentElement.parentElement.children[1].children[1].innerHTML = luasValue;
}

// T = tipe bangunan
function updateTipe(tipeBangunan) {
    // console.log(tipeBangunan.value)
    // console.log(tipeBangunan.parentElement.parentElement.parentElement.children[2].children[0].children[0].children[0].children[0].children[2].children[1])
    var tipeBangunan = tipeBangunan.value;
    var label = document.getElementById("pondasi_tipe_1");
    

    if (tipeBangunan === 'tipe_rumahmewah') {
        label.textContent = "Rumah Mewah";
        var hasil = "01";
    }
    else if (tipeBangunan === 'tipe_rumahmenengah') {
        label.textContent = "Rumah Menengah" ;
    }
    else if (tipeBangunan === 'tipe_rumahsederhana') {
        label.textContent = "Rumah Sederhana" ;
    }
    else if (tipeBangunan === 'tipe_bangunansemipermanen') {
        label.textContent = "Bangunan Semi Permanen" ;
    }
    else if (tipeBangunan === 'tipe_gudang') {
        label.textContent = "Gudang" ;
    }
    else if (tipeBangunan === 'tipe_bangunanlowrise') {
        label.textContent = "Bangunan Low Rise" ;
    }
    else if (tipeBangunan === 'tipe_bangunanmidrise') {
        label.textContent = "Bangunan Mid Rise" ;
    }
    else if (tipeBangunan === 'tipe_bangunanhighrise') {
        label.textContent = "Bangunan High Rise" ;
    }
    else if (tipeBangunan === 'tipe_mallgradeb') {
        label.textContent = "Mall Grade B" ;
    }
    else if (tipeBangunan === 'tipe_hotelbintang3') {
        label.textContent = "Hotel Bintang 3" ;
    }
    else if (tipeBangunan === 'tipe_apartemengradeb') {
        label.textContent = "Apartemen Grade B" ;
    }
    else if (tipeBangunan === 'tipe_lainnya') {
        label.textContent = "Lainnya" ;
    }

    // tipeBangunan.parentElement.parentElement.parentElement.children[2].children[0].children[0].children[0].children[0].children[2].children[1].innerHTML = tipeBangunan



    
}