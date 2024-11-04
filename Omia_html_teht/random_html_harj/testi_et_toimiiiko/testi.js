

function kortin_arvot(email, fanitaso) {
document.getElementById("email").innerHTML=email;
document.getElementById("fanitaso").innerHTML=fanitaso;

}
function parametrit() {
    const queryString = window.location.search;
    console.log(queryString);
    const urlParams = new URLSearchParams(queryString);
    const email = urlParams.get('email')
    const fanitaso = urlParams.get('fanitaso')
    console.log(email, fanitaso);
    kortin_arvot(email, fanitaso);

}



window.onload = parametrit;

