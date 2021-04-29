var clck=document.getElementById("clkid")
function clickchange(){
    clck.textContent="clicked"
    
}
clck.addEventListener("click",clickchange)


var dbc=document.querySelector("#dbclk")
dbc.addEventListener("dblclick",()=>{
    dbc.textContent="double clicked";
    dbc.style.color="blue"
})

var moso=document.querySelector("#mo")
moso.addEventListener("mouseover",()=>{
moso.textContent="moved";

})
