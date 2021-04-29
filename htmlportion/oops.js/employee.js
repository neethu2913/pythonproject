class Employee{
    constructor(eid ,name,desgin,salary){
    this.eid=eid;
    this.name=name;
    this.desgin=desgin;
    this.salary=salary;
    }
    printemployee(){
        console.log(this.eid);
        console.log(this.name);
        console.log(this.desgin);
        console.log(this.salary);
    }
}
var emp1=new Employee(11,"neethu","developer",23400)
var emp2=new Employee(21,"nandhu","qa",26000)
var emp3=new Employee(24,"andhu","mrkt",24500)
var emp4=new Employee(22,"vijay","developer",22000)

var employees=[]
employees.push(emp1)// push to the above arry
employees.push(emp2)
employees.push(emp3)
employees.push(emp4)

var enames=employees.map(emp=>emp.name)
console.log(enames);

var edesgin=employees.map(emp=>emp.desgin)
console.log(edesgin);

var edevloper=employees.filter(emp=>emp.desgin=="developer")
console.log(edevloper);

var maxsalary=employees.reduce((emp1,emp2)=>emp1.salary<emp2.salary?emp1:emp2)
console.log(maxsalary);

var sal=employees.sort((emp1,emp2)=>emp1.salary-emp2.salary).forEach(emp=>console.log(emp))
//console.log(sal);
   

//foreach
 var arr=[1,2,3,4,5]
//to select all the elements
 arr.forEach(arr=>console.log(arr))
 
