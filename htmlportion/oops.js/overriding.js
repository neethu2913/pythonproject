//overriding 
class Parent{
    phone(){
        console.log("inside the parent method");
    }
}
class Child extends Parent{
    phone(){
        console.log("inside the child method");    }
}
 var ch=new Child()
 ch.phone()