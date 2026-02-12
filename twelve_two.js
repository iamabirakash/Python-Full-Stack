// let arr=["Python","JS",1];
// console.log(arr[0])
// console.log(arr[0,1])
// arr[0]="CSS"
// console.log(arr)

//foreach,map,filter,reduce
// for each: do updation in the same array, donot return the new array: performs operation on each element of an array but doesw not return a new array
// let arr=[10,20,30,40,50];
// arr.forEach((num) => {
//     console.log(num+5);
// })

//Map: perform operation on each elemnt and return a new array
// let arr=[10,20,30,40,50];
// let newArr=arr.map((num) => {
//     return num+5;
// })
// console.log(newArr)

//Filter--> return elemnts based on some conditions
// let arr=[10,20,30,40,50];
// let newArr=arr.filter((num) => {
//     return num>20;
// })
// console.log(newArr)

//Reduce= it will combine the array and return single value
// let arr=[10,20,30,40,50];
// let newArr=arr.reduce((acc, currval) => {
//     console.log("Acc: ",acc);
//     console.log("Curr Val: ",currval);i9
//     return currval+acc;
// })
// console.log(newArr)

//Array destructuring: to store each array element in some other element, break array into variables
//--rest operator--> collect remaining elements of an array [a,b,...z]
//spread operator--> expand elements of an array
// const[a,b,...z]=arr;
// let newArr=[arr,60,70];
// let newArr=[...arr,60,70];
// console.log(newArr);

// add 5 to each element, filter out element whiich is greater than 25, find sum of the remaining elements
// let newArr=arr.map((num) => {
//     return num+5;
// })
// console.log(newArr)
// let newArr2=newArr.filter((num) => {
//     return num >25;
// })
// console.log(newArr2)
// let newArr3=newArr2.reduce((acc,currval) => {
//     return acc+currval;
// })
// console.log(newArr3)

// let newArr=arr.map(num => (num+5)).filter(num => num>25).reduce((num1,num2) => num1+num2)
// console.log(newArr)

// obj={
//     name:"Amisha",
//     id:1,
    // greet: function(){
    //     return "hello"
    // }
    // add:["Noida","Assam"],
// }
// obj.address="assam";
// obj.name="Abir"
// console.log(obj["name"])
// console.log(obj.greet())
//this--> refers to current object

// const {name,id}=obj;
// console.log(name)
// let newObj={...obj,add:"Delhi"}
// console.log(newObj)

//keys
// Object.keys(obj).forEach((key) => {
//     console.log(key)
// })

// Object.values(obj).forEach((val) => {
//     console.log(val)
// })

// Object.keys(obj).forEach((key) => {
//     console.log(key,obj[key])
// }).

//Asynchronous js:
// --> callbacks
// --> promises
// --> async await

// synchronous -------------> call stack-----------> gec,fec
// gec: global execuction context
// fec: function execution context
// let a=20;//global variable
// function test(){
//     let a=30;//local variable
//     console.log(a);
// }
// test();
// console.log(a);

// asynchronous -->
// microtask queue(promises)
// callback queue(call backs)

// first goto callstack then microtask then to callback queue
//callbacks==> functions which can be return into another function as a parameter

// function test(){
//     console.log("Fetching data...")
// }
// function data(callback){
//     callback();
//     console.log("Data fetched...")
// }
// data(test);

// function test(){
//     console.log("HTML")
//     setTimeout(() =>{
//         console.log("JavaScript...")
//     })
//     // },2000)  //this 2000 is for delay
//     console.log("CSS")
// }
// test()

//event loop->all exceution in js decided by event loop --> first of alll synchronous code run (call stack), then microstack promises run, then call back
// function test(){
//     console.log("HTML")
//     setTimeout(() =>{
//         console.log("JavaScript...")
//         setTimeout(() => {
//             console.log("Python")
//         },2000)
//         setTimeout(() => {
//             console.log("CSS")
//         },1000)
//     },500)
// }
// console.log(1)
// test()

// function test(){
//     console.log("HTML")
//     setTimeout(() =>{
//         console.log("JavaScript...")
//         setTimeout(() => {
//             console.log("Python")
//         })
//         console.log("Java")
//         setTimeout(() => {
//             console.log("CSS")
//         })
//     })
// }
// console.log(1)
// test()

function test(){
    let i=0;
    let interval = setInterval(() => {
        console.log(i);
        i++;
        if(i==5){
            clearInterval(interval )
        }
    },2000)
}
test();