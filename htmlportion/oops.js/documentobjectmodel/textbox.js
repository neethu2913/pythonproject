
function button(){
var one=document.querySelector("button")
one.addEventListener("click",()=>{
var name=document.getElementById("#name").value;
var age=document.getElementById("#age").value;
if(age < 18)
{
    window.alert(name+"eligible")
}
else
{
    window.alert(name+"not eligible")
}
})
}