// DOM manipulation--> in which u can change the html Data, change in the html tree
//getElementByID
// let head=document.getElementById("head");
// head.style.color="red"  //we write .style to apply css over there

//getElementsByClassName
// let head=document.getElementsByClassName("headClass");
// head[2].style.color="red";
// for (let i=0;i<head.length;i++){
//     head[i].style.color="red"
// }

//passing class name or tag name we need to pass the index for the color
// getElementsbyTagName
// let head=document.getElementsByTagName("h1");
// head[0].style.color="red";

//querySelector--> provide only first element
// --> instead of writing IdleDeadline, class,tag differently we can pass all in once

//for id use # 
// let head=document.querySelector("#head");
// head.style.color="red";

//querySelectorAll--> provide all the element
//for class use .
// let head=document.querySelectorAll(".headClass");
// head[1].style.color="red";

// for tag nothing will be  used 
// let head=document.querySelector("h1")
// head.style.color="red"

let head=document.querySelectorAll("h1")
head[1].style.color="red"