//class=blueprint,design pattern,plan,template
//object=realworld entity
//reference=
//this=current value point out
//this.varible=instantances variable (that is relesated with object)  constuctorin (new)
// constructor can also inizalize the instance variblas(init) pyton
//set =iniza;i
//print=output
//new keyword=
class student{
    constructor(name,course,grade){
        this.name=name;
        this.course=course;
        this.grade=grade
    }
    printStudent(){
        console.log(this.name);
        console.log(this.course);
        console.log(this.grade);
    }
}
var obj=new student("neethu","bca",234)
obj.printStudent()