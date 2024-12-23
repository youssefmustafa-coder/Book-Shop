
const loginBtn = document.querySelector("#login");
const registerBtn = document.querySelector("#Register");
const loginform = document.querySelector(".login-form");
const Registerform = document.querySelector(".register-form");



loginBtn.addEventListener('click',()=>{
    loginBtn.style.background="#21264D";
    registerBtn.style.background="rgba(255, 255, 255, 0.2)";

    loginform.style.left = "50%";
    Registerform.style.left="-50%";

    loginform.style.opacity=1;
    Registerform.style.opacity=0;
})


registerBtn.addEventListener('click',()=>{
    loginBtn.style.background="rgba(255, 255, 255, 0.2)";
    registerBtn.style.background="#21264D";

    loginform.style.left = "150%";
    Registerform.style.left="50%";

    loginform.style.opacity=0;
    Registerform.style.opacity=1;
})


const logInputField=document.getElementById('logPassword');
const logInputIcon=document.getElementById('log-pass-icon');


const regInputField=document.getElementById('regPassword');
const regInputIcon=document.getElementById('reg-Pass-icon');


function myLogPassword(){
    if(logInputField.type === "password"){
        logInputField.type="text";

        logInputIcon.name="eye-off-outline";
        logInputIcon.style.cursor ="pointer";
    }

    else{
        logInputField.type="password";

        logInputIcon.name="eye-outline";
        logInputIcon.style.cursor ="pointer";
    }
}


function myRegPassword(){
    if(regInputField.type === "password"){
        regInputField.type="text";

        regInputIcon.name="eye-off-outline";
        regInputIcon.style.cursor ="pointer";
    }

    else{
        regInputField.type="password";

        regInputIcon.name="eye-outline";
        regInputIcon.style.cursor ="pointer";
    }
}


function changeIcon(value){
    if(value.length > 0){
        logInputIcon.name="eye-outline";
        regInputIcon.name="eye-outline";
    }

    else{
        logInputIcon.name="lock-closed-outline";
        regInputIcon.name="lock-closed-outline";
    }
}



