function makeCounter() {
  let num = 0; // 외부 함수의 변수. 은닉화.
  
  return function() { // 익명 함수 
    return num++
  }
}

const counter = makeCounter();

console.log(counter()) // 0
console.log(counter()) // 1
console.log(counter()) // 2