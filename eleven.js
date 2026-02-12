//mouse--> onclick,ondblclick, onmouseover
//input--> onkeyup, onkeydown, onchange, oninput

// const handleDown = () => {
//     document.getElementById("output").innerHTML="Key is Pressed...";
// }

// const handleUp = () => {
//     document.getElementById("output").innerHTML="Key is Released...";
// }

// const handleChange = () => {
//     let inp=document.getElementById("inp")
//     document.getElementById("output").innerHTML=inp.value;
//     inp.value="";
// }
// const handleInput = () => {
//     let inp=document.getElementById("inp")
//     document.getElementById("output").innerHTML=inp.value;
//     // inp.value="";
// }

//create input fied and paragraph p tag) which will show the character count and update the keyword using onkeyup

// const handleClick = () => {
//     let inp=document.getElementById("inp");
//     document.getElementById("output").innerHTML=inp.value;
//     inp.value="";
// }

// const handleClick = () => {
//     let p=document.createElement("p");
//     p.innerHTML="Reading books is a wonderful hobby that opens up new worlds. It allows readers to explore different cultures, eras, and perspectives without leaving their homes. Additionally, it improves vocabulary and enhances imagination, making it a productive way to spend free time. Therefore, developing a habit of reading brings knowledge and joy to life."
//     document.body.appendChild(p);
//     p.classList.add("para");
// }

// const handleSubmit = (e) => {
//     e.preventDefault();

//     let name=document.getElementById("name");
//     let message=document.getElementById("message")

//     let output1=document.createElement("h1");
//     let output2=document.createElement("h1");

//     output1.innerHTML="Name: " + name.value;
//     output2.innerHTML="       Message: "+message.value;

//     document.body.appendChild(output1);
//     document.body.appendChild(output2);

//     name.value="";
//     message.value="";
// }

const handleSubmit=(e)=>{
    e.preventDefault();
    let task=document.getElementById("task");
    let output=document.getElementById("output");

    let p=document.createElement("p");
    p.innerHTML=task.value;
    output.append(p);
    task.value="";
    p.classList.add("para")
    p.style.cursor="pointer";
    p.onclick=function(){
        p.remove();
    }
}