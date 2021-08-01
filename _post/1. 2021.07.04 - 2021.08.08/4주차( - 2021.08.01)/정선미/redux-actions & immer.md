# 📌 redux-actions

## 🔹 효과

더 짧게 작성 → 가독성 ⬆, 객체 직접 작성x

## 🔹 사용법

### 🔸 액션 생성 함수

- `createAction` 사용
- (액션에 필요한) 추가 데이터 : payload
  - 형태
    - **기본형 예시**

```jsx
import { createAction } from "redux-actions";

export const increase = createAction(INCREASE);
export const decrease = createAction(INCREASE);
```

- **예시 1. 액션 생성 함수 파라미터를 payload에 변형을 주어서 넣고 싶다면**
  - `creatAction` 2번째 함수에 따로 선언

```jsx
const MY_ACTION = "sample/MY_ACTION";
const myAction = creatAction(MY_ACTION, (text) => `${text}!`);
const action = myAction("hello world");

/*
                            	결과:
                            	{ type: MY_ACTION, payload: 'hello world!' }
                            */
```

- **예시 2. 생략 가능한 파라미터**
  - 파라미터를 그대로 반환하는 함수 (ex. `id ⇒ id` )
    - 생략 가능 (필수x)
    - 효과: 필요한 파라미터 값 파악 쉬워짐

```jsx
export const toggle = createAction(TOGGLE, (id) => id);
```

### 🔸 리듀서

> `handleActions` 사용

- 기본형 예시

```jsx
import { handleActions } from "redux-actions";

const counter = handleActions(
  {
    [INCREASE]: (state, action) => ({ number: state.number + 1 }),
    [DECREASE]: (state, action) => ({ number: state.number - 1 }),
  },
  initialState
);
```

- 1번째 파라미터: 각 액션에 대한 업데이트 함수
- 2번째 파라미터: 초기 상태

---

- 추가 데이터 조회: `action.payload` 값을 조회
  - **객체 비구조화 할당 활용**
    - action 의 payload 이름 새로 설정 → `action.payload`가 어떤 값 의미하는지 더 쉽게 파악 가능
  - **예시 1. `action.payload` 조회 & 객체 비구조화 할당**

```jsx
const todos = handleActions(
  {
    [CHANGE_INPUT]: (state, action) => ({ ...state, input: action.payload }),
    // 비구조화 할당
    [CHANGE_INPUT]: (state, { payload: input }) => ({ ...state, input }),
  },
  initialState
);
```

# 📌 immer

- **모듈 상태가 복잡 ⬆ → 불변성 지키기 어려움**

  → 모듈의 상태 설계 시, **객체 깊이 너무 깊어지지 않게** 주의

  - 객체 깊이 얕음⬆ → 불변성 지킴 & 값 업데이트: 수월

- **사용 이유**

  객체 구조 복잡 & 객체로 이루어진 배열 다룰 때 → 편리한 상태 관리 가능

- **사용 예시**

```jsx
const todos = handleActions(
  {
    [TOGGLE]: (state, { payload: id }) =>
      produce(state, (draft) => {
        const todo = draft.todos.find((todo) => todo.id === id);
        todo.done = !todo.done;
      }),
  },
  initialState
);
```

- 참고 '리액트를 다루는 기술'\_저자 김민준
