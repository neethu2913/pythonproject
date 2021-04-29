//inheritances =class parenti
//extents= class call chey
//multiple inheritance dose'nt support



// single inheritance
//class parent{
  //  phone(){
    //    console.log("have a nokiac1");
    //}
//}
//class child extends parent{

//}
//var ch=new child()
//ch.phone()


//multilevel

class Parent{
     m1(){
        console.log("nokiac1");
    }
}
class Child extends Parent{
        m2(){
            console.log("m2 method");
        }
}
class Subchild extends Child{
    m3(){
        console.log("m3 method");
    }
}
var ch=new Subchild()
ch.m3()
ch.m2()
ch.m1()