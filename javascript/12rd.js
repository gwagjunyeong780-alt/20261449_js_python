const btn = document.getElementById("btn");

// Let btn listen for click
btn.addEventListener("click", myFunction);
btn.addEventListener("dblclick", myFunction1);
btn.addEventListener("mouseover", myFunction2);
btn.addEventListener("mouseout", myFunction3);
function myFunction() {
  document.getElementById("demo").innerHTML = "클릭되었습니다!";
}
function myFunction1() {
  document.getElementById("demo").innerHTML = "더블";
}
function myFunction2() {
  document.getElementById("demo").innerHTML = "들어감";
}
function myFunction3() {
  document.getElementById("demo").innerHTML = "나감";
}




ㄴ
