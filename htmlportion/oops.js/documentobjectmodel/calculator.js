function display(num) 
{
var inp=document.querySelector("#num")
var inpt=inp.value
inp.value=inpt+num
}
function evaluateExp(num)
{
    let inp=document.querySelector("#num").value
    let res=eval(inp)
    document.querySelector("#num").value=res
}
function clr(){
    document.querySelector("#num").value=" "
}
function cancel(){
    let data=document.querySelector("#num").value
    data=data.slice(0,-1)
    document.querySelector("#num").value=data
}