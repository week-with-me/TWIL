# Typescript의 기초

## 1. Typescript를 사용하는 이유

Javascript는 Weakly-typed 된 언어이기 때문에 특정 숫자 변수를 선언한 후에 다른 타입의 값을 변수에 넣을 수 있습니다.

```javascript
let a = 1;
a = { b: "B", c: "C" };
a = null;
a = [1, 2, 4];
a = "abc";
```

이로 인해서 사람이 코드를 작성하면서 실수를 할 확률이 높아집니다.
특히 Java, C#등의 클래스 기반 객체지향 언어에 익숙한 개발자가 Javascript 프로젝트를 수행할 때 진입 장벽을 낮추는 효과가 있습니다.

예를 들어 하기와 같은 함수를 생성 할 경우 두 인지의 타입이 나와 있지않으므로 어떤 타입의 반환값을 리턴해야 하는지 명확하지 않습니다. 따라서 오류를 예측하지 않은 값이 리턴이될 수 있습니다.

```javascript
const sum = (a, b) => {
  return a + b;
};
```

해당 함수를 작성한 개발자의 의도는 숫자 2개를 더하여 리턴하는 함수였을 수 있으나, 코드상에는 어떤 타입의 코드를 인수로 전달하는지 의도가 명확하지 않습니다.
하기 코드와 같이 함수를 작성하면 컴파일 단계에서 오류를 포착할 수 있으며 다른 개발자가 확인했을때 개발자의 의도를 명확하게 기술할 수 있습니다.

```javascript
const sum = (a: number, b: number) => {
  return a + b;
};

sum("a", "b"); //Error
```

## 2. Typescript

### 1. Type

타입 표기는 타입을 직정 지정해주는 것으로 함수나 변수의 타입을 기록하는 간단한 방법이며 컴파일 시점에 에러를 잡아낼 수 있습니다.

```javascript
let num1: number = 1200;
```

### 2. Interface

인터페이스는 클래스 또는 객체를 위한 타입을 지정 할 때 사용되는 문법입니다.
일반 객체를 interface를 설정할 경우는 하기와 같이 지정합니다.

```javascript
interface Animal {
  name: string;
  age?: number; //?가 들어간 경우, 설정을 해도되고 안해도 되는 값을 의미
}
interface Dog extends Animal {
  // extends를 사용하여 이미 선언한 interface를 상속 가능
  breed: string;
}

const myDog: Dog = {
  name: "자몽",
  breed: "Japanese Spitz",
};
```

### 3. Type alias

type은 특정 타입에 별칭을 붙이는 용도로 사용합니다. 이를 사용하여 객체를 위한 타입을 설정할 수도 있고, 배열, 또는 그 어떤 타입이던 별칭을 지어줄 수 있습니다.
type과 interface가 구버전의 Typescript에서는 큰 차이가 존재했으나 현재는 큰 차이가 없다고 합니다. 그렇지만 라이브러리를 작성하거나 다른 라이브러리를 위한 타입 지원 파일을 작성하게 될 때는 interface를 사용하는게 많이 권장되고 있다고 합니다.

```javascript
type Animal = {
  name: string,
  age?: number, //?가 들어간 경우, 설정을 해도되고 안해도 되는 값을 의미
};
type Dog = Animal & {
  // &를 이용하여 두개 이상의 타입을 합치는게 가능
  breed: string,
};

const myDog: Dog = {
  name: "자몽",
  breed: "Japanese Spitz",
};
```

### 4. Generics

함수, 클래스, interface, type을 사용하게 될 때 매개변수나 반환값의 타입을 선언하기 어려운 경우 사용 합니다.
<T>는 컨벤션이며 제네릭에 해당하는 타입에는 어떤 타입이든 들어 올 수 있습니다.

```javascript
interface Objects<T> {
  total_pages: number;
  total_count: number;
  objects: T[];
}

interface Address {
  zipcode: string;
  address1: string;
  address2?: string;
}

onst addressData : Objects<Address> = {
  total_pages: 1,
  total_count: 2,
  objects: [
    {
      zipcode: 12345,
      address1: "경기도 개발시"
    },
    {
      zipcode: 56789,
      address1: "경상도 개발시",
      address2: "개발건물 302호"
    }
  ]
}
```
