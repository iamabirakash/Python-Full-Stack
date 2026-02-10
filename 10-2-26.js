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

// document.getElementById("head").innerHTML="This is Heading";
// document.getElementById("head").innerText="Wanna Have Coffee?"

// let div=document.getElementById("div");
// let p=document.createElement("p"); //this creates a p tag
// div.append(p)
// p.innerHTML="Paragraph"
// p.classList.add("para")

//when we perform any action it is called event trigger
// Action performed on event trigger is called event handling

//Events
// mouse --> onclick,ondblclick
//keyboard --> onkeydown,onkeyup
//form --> onsubmit
//input --> oninput,onchange

// function handleClick(){
//     // alert("Button Clicked");
//     // document.getElementById("head").style.color="red"
//     document.getElementsByTagName("h1")[0].style.color="blue"
//     document.getElementsByTagName("h1")[1].style.color="red";
// }

// let head=document.getElementsByTagName("h1")
// function handleClick(){
//     head[0].style.color="red";
//     head[1].style.color="blue";
// }

// const handleClick2=()=>{
//     hea d[0].innerHTML="JavaScript"
// }

let main=document.getElementById("main");
const handleClick = () =>{
    if(main.style.display == "block"){       //div is a block level element
        main.style.display = "none";
    }
    else{
        main.style.display = "block";
    }
}

// colors=["red","pink","blue","yellow","purple","green"]
// i=0;
// const handleClick=()=>{
//     i=i+1;
//     document.getElementById("main").style.backgroundColor=colors[i%6];
// }

// using random
// const colors = ["red", "pink", "blue", "yellow", "purple", "green"];
// const handleClick = () => {
//     const randomIndex = Math.floor(Math.random() * colors.length);
//     document.getElementById("main").style.backgroundColor = colors[randomIndex];
// };

// const handleDblClick=()=>{
//     document.getElementById("main").style.display="none"
// }

const handleOver=()=>{
    document.getElementById("btn").style.display="none"
}
