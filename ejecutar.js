function ejecutar() {
    let entrada = document.getElementById("letra").value;
    let codigo = entrada.charCodeAt(0); 
    let binario = "";

    
    for (let i = 7; i >= 0; i--) {
        if (2 ** i <= codigo) {
            binario = binario + "1"; 
            codigo = codigo - (2 ** i); 
        } else {
            binario = binario + "0"; 
        }
    }

    
    document.getElementById("texto1").innerText = "El valor en ASCII es: " + entrada.charCodeAt(0) + " y en binario es: " + binario;
}

function ejecutar2() {
    let entrada=document.getElementById("binario").value;
    let caracter="";
    let suma=0;

    for(let vc=7; vc>=0; vc--) {
        if (entrada[7 - vc]=="1"){
            suma=suma+2**vc;
        }
    }
    caracter=String.fromCharCode(suma);

    document.getElementById("texto2").innerText="El valor en ASCII es: "+suma + " y el caracter es: " + caracter;
}

function limpiar() {
    document.getElementById("letra").value = "";  // Borra el input
    document.getElementById("texto1").innerText = ""; // Borra el resultado
}

function limpiar2() {
    document.getElementById("binario").value = "";  // Borra el input
    document.getElementById("texto2").innerText = ""; // Borra el resultado
}
