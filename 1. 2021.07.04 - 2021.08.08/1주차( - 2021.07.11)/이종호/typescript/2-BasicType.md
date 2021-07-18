이번 글은 TypseScript가 제공하는 Basic타입들을 알아볼 것이다.

# Type annotation
먼저 TypeScript의 타입들을 알아보기 전에 Type annotation을 알아본다. 일반 변수 선언의 경우 Types anootation은 다음과 같다.
```js
const name: string = 'jongho';
```
간단하다. 변수의 식별자 뒤에 콜론(:)을 붙이고, 그 뒤에 타입을 정의하면 된다.
함수를 정의하는 경우 다음과 같이 쓴다.
```js
function echo(param: string): string{
  return param;
}
```
마찬가지로 매개변수 옆에 콜론을 찍고 타입을 입력하기만 하면 (공백무시) JavaScript와 다른 점이 없다. 함수의 경우 매개변수를 넘기는 괄호 후에 콜론 후 타입을 적으면 된다.

# JavaScript 지원 타입
TypeScript가 언어차원에서 기본적으로 지원하는 Type은 두 종류로 분류할 수 있다. 
`Basic Type`과 `Advanced Type`. 
이번 글에서는 이중 Basic Type만 다룬다. Basic Type은 다시 두 가지로 (순전히 나만의 분류) 나눌 수 있다. 
**JavaScript에 이미 존재하는 것**과 **그렇지 않은 것**. 
JavaScript에 존재하는 타입들의 목록은 다음과 같다.

- Boolean
- Number
- String
- Array
- Null / Undefined

위에 나열한 타입들은 기본적인 JavaScript 지식만 가지고 있더라도 모두 아는 타입일테니 누차 설명하지 않겠지만 몇가지 주의할 점에 대해서만 얘기하겠다.

## boolean? Boolean?
JavaScript에서는 위와 같은 JavaScript primitive type들에 대해 래핑한 객체를 제공한다. TypeScript도 이를 지원하므로 다음과 같이 코드를 쓸 수 있다.
```js 
const isLiar: boolean = true; // OK
const isTruth: Boolean = true; // OK
```
가급적이면 `boolean`을 사용하는 것이 권장된다. `new Boolean()`으로 생성한 값을 `boolean`타입에 할당할 수는 있으나 그 반대는 안되기 때문이다.
```js
cosnt isLiar: boolean = new Boolean(true); // OK
cosnt isTruth: Boolean = false; // Error: Type 'Boolean' is not assignable to type 'boolean'.
// 'boolean' is a primitive, but 'Boolean' is a wrapper object. Prefer using 'boolean' when possible.
```

몰론 리터럴 문법 대신 저렇게 래핑 객체를 이용하여 생성자를 호출하는 것이 JavaScript에서도 권장하지 않는 방법이다.

위의 사항은 `Number` & `number`, `String` & `string` 등에서도 해당되는 부분이므로 타입 병시할 떄 헷갈리지 말도록 하자.

## Array
`Array`는 두 가지 방법으로 선언이 가능하다. 먼저 Array 리터럴을 이용한 방식.
```js
const animals: string[] = ['Cow', 'Dog', 'Cat'];
```
그 다음은 제네릭이라는 것을 사용한 방식이다.
```js
const animals: Array<string> = ['Cow', 'Dog', 'Cat'];
```
`Array` 뒤에 뾰족한 괄호완 같이 사용되는 것인 제네릭(Generic)문법이다. 제네릭은  Java에서 흔히 알려진 개념이지만 동적 타이핑 언어인 JavaScript에서는 접할 일이 없는 개념이므로 약간 생소할 수 있다.
TypeScript의 제네릭에 대해서는 나중에 따로 다뤄보기로하고 일단은 저런 것이 있다라고만 생각하고 넘어가면 된다.
나의 경우 Java보다는 C++에 익숙하기 떄문에 C++템플릿 문법과 닮았다는 생각을 했다.

## Null & Undefined
JavaScript에서도 그랬들 `null` 이나 `undefined` 는 모든 타입의 변수로 할당할 수 있다. 
하지만 TypeScript의 `null` 타입과 `undefined` 타입은 다른 변수를 할당해버리면 에러가 난다.

```js
let only Null: null = null;
onlyNull = undefined; // OK
onlyNull = false; // error: Type 'boolean' is not assignalbe to type 'null'.
```
솔직히 왜 있는 타입인지는 잘 모르겠다. 실제로 JavaSCript를 쓰면서 항상 `null` 이거나 `undefined` 인 변수를 쓸 일이 없었기 때문.

# TypeScript 추가 타입
TypeScript에서는 JavaScript에서 지원하지 ㅇ낳는 타입들을 만들어 지원하고 있다. 
- Tuple
- Any
- Void
- Never
- Enum


## Tuple
python을 해봤다면 Python의 Tuple이 쉽게 연상될 것이다. 그러나 TypScript의 Tuple은 Python의 그것과는 많이 다르다.
먼저 Python의 Tuple은 요소의 숫자가 고정되어 있고 immutable(수정불가능한)리스트인데 Typescript에서는 자유롭게 추가, 삭제, 수정이 가능하다. TypScript의 Tuple은 다음과 같이 정의한다.
```js
let tuple: [ boolean, number ] = [true, 0];
tuple.concat([false, 1]);
tuple.push('string'); // Error: Argument of type 'string' is not assignable to parameter of type 'number | boolean'
```
Tuple의 기본적인 성격은 Array랑 동일하다. 차이점은 요소로 가질 수 있는 타입이 여러가지로 나뉠 수 있다는 것이다. 
위의 Tuple은 `boolean`, `number` 만 받을 수 있는 Tuple이다. 그러나 3번째 줄에서 `string`타입을 추가하려고 하면서 에러가 생겼다.

에러메시지를 보면 타입이  `number`나 `boolean`이 아니기에 할당할 수 없다고 한다. 때문에, 순서에 관계없이 선언된 두 종류의 타입 중 하나면 요소가 될 수 있는 건가? 라는 생각을 할 수 있다.

```js
let tuple: [ boolean, number ] = [ 0, true ]; // Error: Type '[number, boolean]'
```
하지만 위와 같이 순서도 중요하다. 단, 애초에 선언한 index일 때만 중요하다. 그러니까 위의 경우 0번째 요소는 반드시 `boolean` 타입이어야하고,  1번째 요소는 방드시 `number`타입이어야 하는 것이다. 그 뒤의 2, 3, 4, 번재 요소의 타입은 그냥 `boolean || number`이면 된다.

## Any
Any는 문자 그대로 어떤 타입이든 통과하는 타입이다. 예를 들면,
```js 
let anyVar = true;
anyVar = 1;
anyVar = null;
```
이런 식으로 어떤 타입의 값을 할당해도 오류가 나지 않는다. 정적 탕비 검사가 없음으로 JavaScrpt와 차이가 없고, TypeScript의 장점이 드러아지 않는 만큼 되도록이면 사용을 지야해야겠지만, JavaScript 기반의 프로그램을 반드는 경우 어쩔 수 없이 사용해야 하는 경우가 종종 있다.

## Vodi
Vodi는 함수에서만 득히 활용하는 타입이다.
```js
function log(arr): void {
  console.log(arr.join(', '));
}
```
위 함수처럼 리턴하는 값이 없는 함수의 경우 리턴 타입으로 `void`를 명시해줄 수 잇다. 그러나 `null`혹은 `undefined` 값을 할당할 수 있는 타입이므로, `return null;` 또한 가능하다 변수도 지정가능한 타입이지만 Null & Undefined타입과 마찬자지로 `null` 과 `undefined` 밖에 할당할 수 없으므로 별로 쓸모가 없다.

