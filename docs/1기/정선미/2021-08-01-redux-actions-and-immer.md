---
title: "Redux-actions & immer"
date: "2021-08-01"
author: ์ ์ ๋ฏธ
---

# Redux-actions & immer

### ๐น ํจ๊ณผ

๋ ์งง๊ฒ ์์ฑ โ ๊ฐ๋์ฑ โฌ, ๊ฐ์ฒด ์ง์  ์์ฑx

### ๐น ์ฌ์ฉ๋ฒ

#### ๐ธ ์ก์ ์์ฑ ํจ์

- `createAction` ์ฌ์ฉ
- (์ก์์ ํ์ํ) ์ถ๊ฐ ๋ฐ์ดํฐ : payload
  - ํํ
    - **๊ธฐ๋ณธํ ์์**

```jsx
import { createAction } from "redux-actions";

export const increase = createAction(INCREASE);
export const decrease = createAction(INCREASE);
```

- **์์ 1. ์ก์ ์์ฑ ํจ์ ํ๋ผ๋ฏธํฐ๋ฅผ payload์ ๋ณํ์ ์ฃผ์ด์ ๋ฃ๊ณ  ์ถ๋ค๋ฉด**
  - `creatAction` 2๋ฒ์งธ ํจ์์ ๋ฐ๋ก ์ ์ธ

```jsx
const MY_ACTION = "sample/MY_ACTION";
const myAction = creatAction(MY_ACTION, (text) => `${text}!`);
const action = myAction("hello world");

/*
                            	๊ฒฐ๊ณผ:
                            	{ type: MY_ACTION, payload: 'hello world!' }
                            */
```

- **์์ 2. ์๋ต ๊ฐ๋ฅํ ํ๋ผ๋ฏธํฐ**
  - ํ๋ผ๋ฏธํฐ๋ฅผ ๊ทธ๋๋ก ๋ฐํํ๋ ํจ์ (ex. `id โ id` )
    - ์๋ต ๊ฐ๋ฅ (ํ์x)
    - ํจ๊ณผ: ํ์ํ ํ๋ผ๋ฏธํฐ ๊ฐ ํ์ ์ฌ์์ง

```jsx
export const toggle = createAction(TOGGLE, (id) => id);
```

#### ๐ธ ๋ฆฌ๋์

> `handleActions` ์ฌ์ฉ

- ๊ธฐ๋ณธํ ์์

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

- 1๋ฒ์งธ ํ๋ผ๋ฏธํฐ: ๊ฐ ์ก์์ ๋ํ ์๋ฐ์ดํธ ํจ์
- 2๋ฒ์งธ ํ๋ผ๋ฏธํฐ: ์ด๊ธฐ ์ํ

---

- ์ถ๊ฐ ๋ฐ์ดํฐ ์กฐํ: `action.payload` ๊ฐ์ ์กฐํ
  - **๊ฐ์ฒด ๋น๊ตฌ์กฐํ ํ ๋น ํ์ฉ**
    - action ์ payload ์ด๋ฆ ์๋ก ์ค์  โ `action.payload`๊ฐ ์ด๋ค ๊ฐ ์๋ฏธํ๋์ง ๋ ์ฝ๊ฒ ํ์ ๊ฐ๋ฅ
  - **์์ 1. `action.payload` ์กฐํ & ๊ฐ์ฒด ๋น๊ตฌ์กฐํ ํ ๋น**

```jsx
const todos = handleActions(
  {
    [CHANGE_INPUT]: (state, action) => ({ ...state, input: action.payload }),
    // ๋น๊ตฌ์กฐํ ํ ๋น
    [CHANGE_INPUT]: (state, { payload: input }) => ({ ...state, input }),
  },
  initialState
);
```

## ๐ immer

- **๋ชจ๋ ์ํ๊ฐ ๋ณต์ก โฌ โ ๋ถ๋ณ์ฑ ์งํค๊ธฐ ์ด๋ ค์**

  โ ๋ชจ๋์ ์ํ ์ค๊ณ ์, **๊ฐ์ฒด ๊น์ด ๋๋ฌด ๊น์ด์ง์ง ์๊ฒ** ์ฃผ์

  - ๊ฐ์ฒด ๊น์ด ์์โฌ โ ๋ถ๋ณ์ฑ ์งํด & ๊ฐ ์๋ฐ์ดํธ: ์์

- **์ฌ์ฉ ์ด์ **

  ๊ฐ์ฒด ๊ตฌ์กฐ ๋ณต์ก & ๊ฐ์ฒด๋ก ์ด๋ฃจ์ด์ง ๋ฐฐ์ด ๋ค๋ฃฐ ๋ โ ํธ๋ฆฌํ ์ํ ๊ด๋ฆฌ ๊ฐ๋ฅ

- **์ฌ์ฉ ์์**

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

- ์ฐธ๊ณ  '๋ฆฌ์กํธ๋ฅผ ๋ค๋ฃจ๋ ๊ธฐ์ '\_์ ์ ๊น๋ฏผ์ค
