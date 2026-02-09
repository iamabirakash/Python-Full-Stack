/* Javascript--> logic/dynamic behaviour(data changing over the time) part of website 
--> actions handled by Javascript
--> high level lang(human readable form, to build language) same as python
--> dynamic(no need to give datatypes)
--> scripted lang(we can write scripts for automation and all)
--> same as python uses interpreter(execute line by line)
Applications 
--> dynamic behaviour
--> synchronous(exceution done(line by lline) by js only) and asynchronous(you can set priorities-->you can wait like first exceute this then this) at the same pt of time
--> single threaded(only one thread for execution cannot run multiple task at one time can only run a single task) --> 
Current version--> EM(ECMAScript)2025 --> Major update in ES6(2015)

*/

// console.log("external JS")

//var,let and const

// var--> function scope, re-declare, re assign
//let--> block scope, re-assign--> allowed, re-declare--> not allowed
//const--> block scope, re-assign--> not allowed, re-declare--> not allowed
// var a=20;
// let b="Hello";
// const c=30;
// console.log(b)

// function hello(){
//     var x=1;
//     if(x){
//         var a=20;
//     }
//     console.log(a)
// }
// hello();

// function hello(){
//     var x=1;
//     if(x){
//         let a=20;
//     console.log(a)
//     }
// }
// hello();

// function hello(){
//     var x=1;
//     if(x){
//         const a=20;
//     }
//     console.log(a)
// }
// hello();

// var a=20;
// var a=20;
// console.log(a)

// let a=20;
// a=40;
// console.log(a)

// let a=20;
// function hello(){
//     let a=30;
//     console.log(a)
// }
// hello();

// const a=20;
// a=50;
// console.log(a)

// features only provided by js
// DOM Manipulaton
// Event handling
 
        //              HTML
        //     body                 Head
        // h1      div        title      Meta

// function test(a,b){
    // return a+b;
    // console.log(a+b)
// }
// console.log(test(10,20))
// test(10,20);

// const a=function test(a,b){
//     console.log(a+b);
// }
// a(10,20);

// test(10,20);
// function test(a,b){
//     console.log(a+b)
// }

// Hoisting--> if you call a function before declaring--> var,function--> u can use function or variable with var before the declaration
console.log(a);
var a=20;