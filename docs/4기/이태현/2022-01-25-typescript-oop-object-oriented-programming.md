---
title: "TypeScript OOP(Object Oriented Programming)"
description: "JavaScript의 객체 지향 프로그래밍(OOP_Object Oriented Programming)을을 이해하기 위한 프로토타입(Prototype)과 this 키워드 그리고 ES6 때 등장한 Class에 대한 설명과 TypeScript에서의 구현 방법"
author: "이태현"
date: "2022-01-25"
---

# TypeScript OOP(Object Oriented Programming)

## 도입

최근 TypeScript를 공부하면서 JavaScript의 객체 지향 프로그래밍 개념이 다른 언어와 조금 다르다는 것을 알게 되었습니다. 그래서 관련해서 한 번 정리를 할 필요가 있을 것 같아 이렇게 글을 작성하게 되었습니다.

!!! info "정보"

    기존의 JavaScript에 관해 어느 정도 알고 있는 분이라면 [자바스크립트는 왜 프로토타입을 선택했을까](https://medium.com/@limsungmook/자바스크립트는-왜-프로토타입을-선택했을까-997f985adb42)라는 글을 추천드립니다.

    아래 제 글의 경우 언어의 철학이나 객체 지향 프로그래밍의 가치관에 대한 서술보다는 단순히 문법적인 측면으로 접근한 글로 더 근원적인 부분을 이해하기에 부족할 수 있습니다.

## JavaScript

JavaScript는 2015년 ES6가 등장한 이후 현재까지 매년 업데이트를 하며 여러 기능들을 추가하고 있습니다. 2015년 이전까지는 2009년에 등장한 ES5 기능을 사용해야 했는데 이때 당시 다른 객체 지향 언어처럼 클래스가 별도로 존재하지 않았기 때문에 **프로토타입(Prototype)** 및 **`this` 키워드** 를 활용하여 객체 지향 프로그래밍을 구현해야 했습니다.

!!! info "정보"

    JavaScript는 명령형 프로그래밍(Imperative Programming), 선언형 프로그래밍(Declarative Programming), 함수형 프로그래밍(Functional Programming)과 객체 지향 프로그래밍(Object Oriented Programming)까지 모두 가능한 **다중 패러다임 언어(Multi-Paradigm Language)**입니다.

### ES5

먼저 ES5 문법을 통해 객체를 만드는 방법을 한 번 살펴봅시다. `Student`라는 객체를 생성하는 방법은 아래와 같습니다.

```Javascript
{!../docs_src/4기/이태현/4주차/1-example.js[ln:1-20]!}
```

위 코드를 실행하면 아래와 같이 정상적으로 객체의 메서드인 `getInfo`가 실행되는 걸 확인할 수 있습니다.

<div class="termy">
    ```sh
    $ node 1-example.js

    Name: James Student ID: undefined Age: undefined
    ```

</div>

`this` 키워드를 활용하여 객체의 필요한 멤버 변수(Member Variable)를 정의하고 객체를 생성합니다. 그리고 메서드는 `prototype`이라는 프로퍼티에 저장합니다. 여기서 특이한 점은 객체를 통해 생성된 인스턴스의 자료형이 함수라는 점입니다.

아래와 같이 `Student` 객체를 출력해보면 함수로 반환되는 걸 확인할 수 있습니다.

```Javascript
{!../docs_src/4기/이태현/4주차/1-example.js[ln:21-22]!}
```

<div class="termy">
    ```sh
    $ node 1-example.js

    [Function: Student]
    ```

</div>

!!! info "정보"

    JavaScript에서의 `this` 키워드는 Java와 같은 기존의 객체 지향 프로그래밍에서의 `this`와는 조금 다릅니다. 보통 `this`가 사용된 위치에 따라서 해당 키워드가 가리키는 것이 다르다고 이야기하곤 합니다.

### ES6

ES6에는 `class` 키워드가 등장했습니다. 위 ES5에서 생성했던 `Student` 객체를 `class` 키워드를 활용하여 만들면 아래 코드와 같습니다.

```Javascript
{!../docs_src/4기/이태현/4주차/2-example.js[ln:1-23]!}
```

코드를 실행해보면 결과는 아래와 같습니다.

<div class="termy">
    ```sh
    $ node 2-example.js

    This is static method. Name: Student
    Name: James Student ID: undefined Age: undefined
    [class Student]
    ```

</div>

`static`이라는 키워드가 등장했습니다. 객체 내에 정의하여 사용할 수 있는 메서드의 종류에는 크게 인스턴스 메서드(Instance Method)와 정적 메서드(Static Method)가 존재합니다.

#### 인스턴스 메서드

인스턴스 메서드(Instance Method)는 위 코드에서 `getInfo()` 함수에 해당합니다. 그 특징으로는 인스턴스를 통해서만 호출할 수 있고 객체 내의 멤버 변수를 사용할 수 있다는 점입니다.

#### 정적 메서드

정적 메서드(Static Method)는 위 코드에서 `staticMethod()` 함수에 해당합니다. 그 특징으로는 인스턴스 메서드와 반대로 인스턴스를 생성하지 않고도 `Student.staticMethod()`와 같은 방식으로 통해 메서드를 사용할 수 있다는 점입니다.

#### 특징

정적 메서드의 경우 인스턴스가 존재하지 않아도 객체로만 메서드가 사용 가능한 이유는 객체가 메모리에 올라갈 때 자동으로 생성되는 메서드이기 때문입니다. 다시 말해 프로그램의 시작할 때부터 종료할 때까지 메모리 상에 올라가게 되어 언제든 사용할 수 있습니다. 그리고 이러한 특징 때문에 인스턴스를 정의하지 않아도 사용할 수 있어 `this` 키워드를 통해 정의하게 된 멤버 변수를 사용할 수 없게 됩니다. 그 결과로 위 코드의 출력이 `This is static method. Name: James`가 아닌 `This is static method. Name: Student`가 되었습니다. `this`가 가리키는 건 객체은 `Student`이고 결국 객체 `Student`의 `name`은, 다시 말해 `this.name`이 반환하는 값은 `Student`이기 때문에 `James`가 아닌 `Student`가 값으로 반환되었습니다.

하지만 만약 해당 코드에서 아래 변수 `student`와 같이 인스턴스를 생성하고 `student.staticMethod()`와 같이 사용하게 되면 해당 인스턴스를 통해 정적 메서드는 사용할 수 없기 때문에 오류를 반환합니다.

!!! info "정보"

    JavaScript에는 `new` 키워드를 활용한 객체 생성 외에도 객체 리터럴(`{}`)을 활용한 방법과 `Object()` 생성자 함수를 활용하는 방법 또한 존재합니다.

## TypeScript

!!! warning "주의"

    기본적인 TypeScript의 특징 및 장점이나 `package.json`, `tsconfig.json` 등의 파일을 통해 TypeScript를 JavaScript로 컴파일하는 과정 등에 대해서는 해당 글에서 다루지 않겠습니다.

TypeScript에서는 아래와 같이 ES6의 문법을 활용하여 객체를 생성할 수 있습니다.

```Typescript
{!../docs_src/4기/이태현/4주차/3-example.ts[ln:1-25]!}
```

해당 코드를 실행해보면 아래와 같습니다.

<div class="termy">
    ```sh
    $ yarn start

    This is static method. Name: Student
    Name: James Student ID: ABCD1234, Age: undefined
    ```

</div>

JavaScript로 컴파일 된 코드를 확인해보면 아래와 같습니다.

```Javascript
"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class Student {
    constructor(name, studentId, age) {
        this.name = name;
        this.studnetId = studentId;
        this.age = age;
    }
    static staticMethod() {
        return `This is static method. Name: ${this.name}`;
    }
    getInfo() {
        return `Name: ${this.name} Student ID: ${this.studnetId}, Age: ${this.age}`;
    }
}
console.log(Student.staticMethod());
const student = new Student("James", "ABCD1234");
console.log(student.getInfo());
```

출력 결과도 동일한데 TypeScript를 사용하여 굳이 객체를 생성하는 이유는 안전성을 위해서입니다.

#### 멤버 변수 선언

JavaScrtip와 달리 아래 코드처럼 멤버 변수를 선언해야 합니다. 그 과정에서 각 멤버 변수의 자료형은 물론 외부로부터의 접근 여부를 `public`, `private`, `protected` 키워드 등을 활용하여 결정해줄 수 있습니다. 그리고 이 과정을 통해 객체에 대한 접근을 제어할 수 있어 개발 과정이 안정적이게 됩니다.

```Typescript
{!../docs_src/4기/이태현/4주차/3-example.ts[ln:5-9]!}
```

이는 `constructor`를 활용한 생성자를 정의할 때도 마찬가지입니다. 아래 코드처럼 `age` 멤버 변수의 경우 선택 사항으로, `name` 및 `studentId` 멤버 변수의 경우 필수 사항으로 만들어 객체를 생성할 때의 오류를 줄일 수 있습니다.

```Typescript
{!../docs_src/4기/이태현/4주차/3-example.ts[ln:9-15]!}
```

## 결론

사실 ES6에서 `class` 키워드를 활용하여 객체를 만드는 방식은 ES5에서의 객체를 생성하는 방식과 내부적으로는 크게 다르지 않다고 합니다. 그럼에도 불구하고 명시적인 선언을 통해 조금 더 생산적인 개발이 가능하며 추가적으로 생긴 `static`과 같은 키워드를 통해 객체 지향에 더 직관적으로 다가갈 수 있게 되었습니다.

TypeScript 등장 이전 JavaScript를 활용하여 은닉화를 구현하기 위해서는 `this` 키워드 대신에 `var` 등의 변수 선언 키워드를 활용해서 마치 `private` 키워드를 사용한 것처럼 구현할 수 있었습니다. 하지만 이 과정이 상당히 복잡했기에 생산성이 떨어질 수밖에 없었습니다. TypeScript에서는 명시적으로 `public`, `private`, `protected` 키워드가 등장하여 객체 지향의 여러 특성을 조금 더 직관적이고 생산적으로 구현할 수 있게 되었습니다.

안정적이고 생산적인 개발을 위해서 ES6 이후의 문법과 함께 TypeScript를 사용하는 건 좋은 선택지라 할 수 있습니다. 클래스가 아닌 프로타타입을 활용한 객체 지향 프로그래밍이라는 특징 때문에 헷갈리던 부분들이 조금은 쉽게 해결될 수도 있습니다.

!!! info "정보"

    은닉화는 정보 은닉(Information Hiding)이라고도 하며 외부 객체로부터 멤버 변수와 같은 속성 값을 감추는 특성을 의미하며 객체 지향의 특징 중 하나입니다.
