ts에서 쓰이는 기본 타입들

1. number
1. string
1. boolean
1. undefined -> 보통 `let age: number | undefined;`와 같이 쓰이고 단독으로 쓰이진 않는다.
1. null: 거의 안쓰인다.
1. unknown: any처럼 모든 타입을 받을 수 있지만 의미적으로 잘 모를때 씀
1. any: 무엇이든 상관 없다. 인데 거의 쓰이지 않고 외부 api나 다른 플랫폼에서 값을 받아와야 할 경우 쓰인다.

1. void: return이 undefined인 경우
1. never: `throw new Error()`나 `while(true)`처럼 함수가 리턴값이 없을 경우 사용


## 배열
```ts
  const fruits: string[] = ['토마토', '바나나'];
  const scores: Array<string> = ['토마토', '바나나'];
```
- 둘 다 동일한 형태
```ts
function printArray(fruits: readonly string[]){}
```
- `readonly`를 사용하고 싶으면 `string[]`으로만 해야함

## Type Aliases: 새로운 타입을 정의

```ts
  type Text = string;
  const name: Text = 'jongho';
  const address: Text = 'korea'
  type Num = number;

  type Student = {
    name: string;
    age: number;
  }
  const student: Student = {
    name: 'jongho',
    age: 27,
  }
```

## String Literal Types: 정확한 문자열을 타입으로 지정

```ts
  type Name = 'jongho';
  let jonghoName: Name;

  jonghoName = 'jongho';

  type Bool = true; // true값만 가질 수 있음
```

## Union Types: OR
```ts
  type Direction = 'left' | 'right' | 'up' | 'down';
  function move(direction: Direction) {
    console.log(direction)
  }
```
-  여러가지 문자열중 하나만을 가질 수 있음

```ts
  // function: login -> success, fail
  type SuccessState = {
    response: {
      body: string;
    }
  }
  type FailState = {
    reason: string;
  }
  type LoginState = SuccessState | FailState;
```
- 다른 타입에 대해서도 마찬이다

### discriminated union
- union 타입에서 **같은 속성값**을 가지게 하여, **구분짓기 편하게 만든 union 형식**
```ts
type SuccessState = {
  result: 'success'; // discriminated union
  response: {
    body: string;
  }
}
type FailState = {
  result: 'fail'; // discriminated union
  reason: string;
}
type LoginState = SuccessState | FailState;

function printLoginState(state: LoginState) {
  if(state.result === 'success') {
    console.log(state.response.body);
  } else {
    console.log(state.reason)
  }
}

```

## Intersection Types: &
- union과 반대되는 개념으로 두개의 타입 모두의 형식을 가져야 한다.
```ts
type Student = {
  name: string;
  score: number;
}

type Worker = {
  employeeId: number;
  work: () => void;
}

function internWork(person: Student & Worker) { // 이 부분
  console.log(person.name, person.employeeId, person.work);
}

internWork({
  name: 'jongho',
  score: 100,
  employeeId: 12345,
  work: () => {}
})

```

## enum
- 다른 언어에서 사용되는 형식인데 이것보다 union을 쓰는 것이 더 좋다고 한다.
- 왜냐하면 한번 값을 할당한 뒤에 **같은 타입의 다른 값을 할당하는 것이 가능**하기 때문
```ts
  enum Days {
    Monday = 1,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
    Sunday
  }

  console.log(Days.Monday); // 1
  let day = Days.Sunday; // 7
  day = 10; // 10
  console.log(day); // 10
```

## Type Inference: 타입 추론
```ts
  let text = 'hello'; // string으로 추론
  function print(message = 'hello'/* string */ ) { // return이 void로 추론
    console.log(message);
  }
  print('hello')
```
- 아주 기본타입이거나 함수 return이 undifined경우 추론을 사용할 수 있지만 회사규정에 따름

## Type Assertions: 타입 강제
```ts
  function jsStrFunc(): any {
    return 2
  }

  const result = jsStrFunc();

  console.log((result as string).length); // result가 string 타입이라고 강제해서 에러발생
  console.log((<string>result).length); // result가 string 타입이라고 강제해서 에러발생
```
- 개발자의 의도에 의해 타입을 강제하여 ts에게 알려줄 수 있다.
- `(result as string)`
- `(<string>result)` 동일
