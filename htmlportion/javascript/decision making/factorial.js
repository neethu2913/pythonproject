function fact(num){
    let res=1;
    for(let i=1;i<=num;i++)
    {
        res=res*i;
    }
    return res
}
let res= fact(4)
console.log(res);