function makeAdder(x){
  return function(y){
    return x + y
  }
}

const add3 = makeAdder(3)
console.log(add3(2))