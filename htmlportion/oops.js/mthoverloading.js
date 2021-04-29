// same method name with different no of paramenters
// rectently implamented  code will only be execute .
class calculation{
    add(){
        console.log("inside single method");
    }
    add(num1,num2){
        console.log("inside two arg method");
    }
}
var obj= new calculation()
obj.add()
obj.add(10,20)