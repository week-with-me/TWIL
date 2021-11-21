---
title: "React | immer를 통한 불변성 유지"
author: "정선미"
date: "2021-11-07"
---

우리는 때때로 불변성을 지켜야 할 때가 있습니다.

- 참고 | `불변성을 지킨다`란?

  기존 값을 직접 수정하지 않고 새로운 값을 만드는 것입니다.

이때 (배열이나 객체의) 구조가 엄청 깊어지면 불변성을 유지하면서 이를 업데이트 하는 것이 힘들어 집니다. 이러한 상황에는 immer라는 라이브러리를 사용하면 해당 작업이 간단해집니다.

immer에 대해 알아볼까요?

## 1. 효과 & 사용하는 경우

서론에 적어둔 것 처럼 immer는 상태 업데이트가 까다로울 때 좋습니다.

구조가 복잡한 객체도 쉽고 짧은 코드를 사용하여 불변성을 유지하며 업데이트가 가능하기 때문입니다. 또한 리덕스를 사용할 때도 immer를 쓰면 코드를 매우 쉽게 작성할 수 있습니다.

immer는 편의를 위한 것이니 필수는 아니지만, 사용하게 되면 생산성을 크게 높일 수 있다는 장점이 있습니다.

## 2. 설치

`$ yarn add immer`

## 3. 사용법

### 3-1. 형식 & 원리

```jsx
import produce from "immer";
const nextState = produce(originalState, (draft) => {
  // 바꾸고 싶은 값 바꾸기
  draft.somewhere.deep.inside = 5;
});
```

#### ◻ [ 형식 ] produce 함수

- 1번째 파라미터
  > 수정하고 싶은 상태
  > 앞에 보여지는 예시 코드에서 produce함수 내부의 1번 째 파라미터인 `originalState` 이며, 수정하고 싶은 상태가 위치하게 됩니다.
- 2번째 파라미터
  > 상태를 어떻게 업데이트할지 정의하는 함수
  > produce함수 내부의 2번째 파라미터로 상태를 어떻게 업데이트 할지 정의하는 함수입니다.
  > 이 함수 내부에서 원하는 값으로 변경할 때 produce 함수가 대신 불변성을 유지하며 새로운 상태를 생성합니다.

#### ◻ 특징

- (앞서 계속적으로 했던 설명과 예시 코드에서 확인 할 수 있다 싶이,) 깊은 곳에 위치하는 값을 변경하는 것이 매우 쉽습니다.
  이외에도 배열을 처리할 때도 매우 쉽습니다.
- 객체나 배열을 직접적으로 변화시키는 함수 (ex. push, splice)를 사용해도 괜찮습니다.
- 그렇다고 무조건 간결해지지 않습니다.
  그렇기 때문에 코드가 복잡할 때만 사용해도 충분합니다.

예시코드와 함께 좀 더 자세히 이해해 보도록 하겠습니다.

### 3-2. 예시 코드

```jsx
import produce from "immer";

const originalState = [
  {
    id: 1,
    todo: "a",
    checked: true,
  },
  {
    id: 2,
    todo: "b",
    checked: false,
  },
];

const nextState = produce(originalState, (draft) => {
  // id가 2인 항목의 checked 값 -> true로 설정
  const todo = draft.find((t) => t.id === 2); // id로 항목 찾기
  todo.checked = true;
  // 혹은 draft[1].checked = true

  // 배열에 새로운 데이터 추가
  draft.push({
    id: 3,
    todo: "c",
    checked: false,
  });

  // id = 1인 항목 제거
  draft.splice(
    draft.findIndex((t) => t.id === 1),
    1
  );
});
```

## 4. useState의 함수형 업데이트와 함께 쓰기

우리는 리액트를 사용하며 성능 최적화하는 방법 중 한 가지로 `useState`의 함수형 업데이트 (**[React | 컴포넌트 성능 최적화](https://velog.io/@katej927/React-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94) 의** `함수 계속 만들어지는 상황 방지 방법` 참고) 를 활용하기도 합니다.

여기에 immer를 함께 사용하게 된다면 어떻게 될까요?

### 4-1. immer의 업데이트 함수 반환 방법

`produce` 함수의 1 번째 파라미터를 함수 형태로 호출하게 되면, 업데이트 함수를 반환하게 됩니다.

- 예시 코드

```jsx
const update = produce((draft) => {
  draft.value = 2;
});
const originalState = {
  value: 1,
  foo: "bar",
};

const nextState = update(originalState);
console.log(nextState); // { value:2, foo: "bar" }
```

### 4-2. 예시 코드

- 기존 코드

```jsx
const onChange = useCallback(
  (e) => {
    const { name, value } = e.target;
    setForm(
      produce(form, (draft) => {
        draft[name] = value;
      })
    );
  },
  [form]
);
```

- 적용 코드

```jsx
const onChange = useCallback((e) => {
  const { name, value } = e.target;
  setForm(
    produce((draft) => {
      draft[name] = value;
    })
  );
}, []);
```

이로써 보다 간단히 불변성을 지키며 업데이트 하도록 도와주는 immer에 대해 알아보았습니다.

도움이 되었기를 바랍니다. 감사합니다. 🙂

---

- 참고
  리액트를 다루는 기술\_김민준 저
