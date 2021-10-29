---
title: "javascript 변수, 데이터 타입"
author: 박지연
date: "2021-07-18"
---

# Javascript 변수, 데이터 타입

## JavaScript의 변수

JavaScript의 변수는 var, let, const로 선언할 수 있습니다.

### 1. var(function scope)

- 변수를 선언. 추가로 동시에 값을 초기화.
- var로 변수를 선언하는 경우 하기와 같이 '5'라는 로그를 남깁니다. 이는 x의 범위가 `if`문 블록이 아니라 x가 선언된 함수이기 때문입니다.

```javascript
if (true) {
  var x = 5;
}
console.log(x); // 5
```

### 2. let

- 블록 범위(scope) 지역 변수를 선언. 추가로 동시에 값을 초기화
- let의 경우 함수 내부에 변수를 선언하면, 오직 그 함수 내에서만 사용할 수 있기때문에 지역변수라고 부름

```javascript
if (true) {
  let y = 5;
}
console.log(y); // ReferenceError: y is not defined
```

### 3. const

- 블록 범위 읽기 전용 상수를 선언
- 변수 재선언, 재할당 불가능

```javascript
const name = "Hi!";
console.log(name); //Hi!

const name = "Hello!";
console.log(name); // Uncaught SyntaxError: Identifier 'name' has already been declared

name = "Bye!";
console.log(name); //Uncaught TypeError: Assignment to constant variable.
```

---

# 호이스팅(Hoisting)

- 변수의 선언문을 유효 범위의 최상단으로 끌어올리는 행위

```javascript
// var의 경우
console.log(name); //undefined
var name;
name = "Hello World!";

//let 의 경우
console.log(name); //SyntaxError: Identifier 'name' has already been declared
let name;
name = "Hello World!";
```

---

## Data Types

### 1. Number

- javascript 에서 숫자에 하나의 형식만 있습니다. 숫자는 소수점과 함께 또는 없이 쓸 수 있습니다.
- `number` 라고 따로 선언하지 않아도 됨.

```javascript
let x1 = 34.0;
let x2 = 34;
console.log(`value: ${x1}, type: ${typeof x1}`); //value: 34, type: number
console.log(`value: ${x2}, type: ${typeof x2}`); //value: 34, type: number
```

- 하기와 같은 경우도 javascript의 숫자 타입이다.

```javascript
const infinity = 1 / 0;
const negativeInfinity = -1 / 0;
const nAn = "not a number" / 2;
console.log(infinity); //Infinity
console.log(negativeInfinity); //-Infinity
console.log(nAn); //NaN
```

### 2. String

- javascript 에서 문자열은 하나의 형식을 가지고 있습니다.
- 단일 또는 이중 따옴표를 사용할 수 있습니다.

```javascript
const name = "ram";
const name1 = "hari";
const plusName = `name are ${name} and ${name1}`;
```

### 3. Boolean

- Boolean타입의 값은 논리적 참, 거짓을 나타내는 `true` 와 `false` 뿐입니다.

  | DATA Type |       true로 변환되는 값        | false로 변환되는 값 |
  | :-------: | :-----------------------------: | :-----------------: |
  |  boolean  |              true               |        false        |
  |  string   |   비어 있지 않은 모든 문자열    |    ""(빈 문자열)    |
  |  number   | 0이 아닌 모든 숫자(무한대 포함) |       0, NaN        |
  |  object   |            모든 객체            |        null         |
  | Undefined |            해당 없음            |      undefined      |

### 4. null

- `null`은 의도적으로 변수에 값이 없다는 것을 명시할때 사용

### 5. undefined

- 선언 이후 값을 할당하지 않은 변수는 `undefined` 값을 가집니다.

### 6. symbol

- `symbol`은 ES6에서 새롭게 추가된 타입으로 변경 불가능한 원시 타입의 값입니다.
- 주로 이름의 충돌 위험이 없는 유일한 객체의 프로퍼티 키(property key)를 만들기 위해 사용합니다.
