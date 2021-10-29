---
title: "리액트 app에 리덕스 적용"
date: "2021-07-25"
author: 정선미
---

# 리액트 app에 리덕스 적용

### 1. store 만들기

- `src/index.js` → **스토어 제작** & 리액트 app에 **리덕스 적용** 작업
- 형태 예시

```jsx
    import React from 'react';
    import ReactDOM from 'react-dom';
    **import { createStore } from 'redux';** // 추가
    ****import './index.css';
    import App from './App';
    import * as serviceWorker from './serviceWorker';
    **import rootReducer from './modules';** // 추가
    ****
    **const store = createStore(rootReducer);** // 추가
    ****
    ReactDOM.render(<App />, document.getElementById('root'));

    serviceWorker.unregister();
```

### 2. 리덕스 적용 (`<Provider>`사용)

- 스토어 사용 위해→ `<App/>`를 `<Provider>`로 감쌈
  - `<Provider>`
    - 'react-redux' 제공
    - store: props로 전달

### 3. `Redux DevTools` 적용

- 리덕스 개발자 도구
- 크롬 확장 프로그램 (설치하여 사용 가능)
- 사용 방법
  - 옵션 1. store 코드 수정

```jsx
        const store = createStore(
          rootReducer,
          **window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),**
        );
```

- 옵션 2. 패키지 설치 (코드 깔끔)
  1. 크롬 확장 프로그램 설치
  2. yarn add redux-devtools-extension 으로 설치
  3. 코드 추가&수정

```jsx
import { composeWithDevTools } from "redux-devtools-extension";

const store = createStore(rootReducer, composeWithDevTools());
```

## 🔷 컨테이너 컴포넌트 만들기

---

- **컨테이너** 컴포넌트: 리덕스 **스토어와 연동**된 컴포넌트
- `src/containers` & `connect`함수
  1. `src/containers` 에 container 컴포넌트 생성
  2. 리덕스 연동 -> `connect`함수(react-redux 제공) 사용

### ◾ `connect`함수

#### ◽ 사용법

`connect(mapStateToProps, mapDispatchToProps)(연동할 컴포넌트)`

- `mapStateToProps, mapDispatchToProps` 에서 반환하는 객체 내부 값들

  컴포넌트의 props로 전달

##### - `mapStateToProps` 란?

스토어의 **상태**를 컴포넌트의 **props로 넘겨**주기 위한 함수

- 파라미터: state (현재 스토어의 상태)

##### - `mapDispatchToProps` 란?

**액션 생성 함수**를 컴포넌트의 **props로 넘겨**주기 위한 함수

- 파라미터 : dispatch (store의 내장 함수)

#### ◽ 원리

connect 함수 호출 → 다른 함수 반환 → 반환된 함수의 parameter: 컴포넌트
⇒ 리덕스와 연동된 컴포넌트 만들어짐

#### ◽ 형태 예시 (일반적)

```jsx
import React from "react";
import { connect } from "react-redux";
import Counter from "../components/Counter";
import { increase, decrease } from "../modules/counter";

const CounterContainer = ({ number, increase, decrease }) => {
  return (
    <Counter number={number} onIncrease={increase} onDecrease={decrease} />
  );
};

// mapStateToProps, mapDispatchToProps 선언
const mapStateToProps = (state) => ({
  number: state.counter.number,
});
const mapDispatchToProps = (dispatch) => ({
  increase: () => {
    dispatch(increase());
  },
  decrease: () => {
    dispatch(decrease());
  },
});
export default connect(mapStateToProps, mapDispatchToProps)(CounterContainer);
```

---

#### ◽ `bindActionCreators` 사용

- 추가 & 수정 코드

```jsx
import { bindActionCreators } from "redux";

export default connect((dispatch) =>
  bindActionCreators(
    {
      increase,
      decrease,
    },
    dispatch
  )
)(CounterContainer);
```

#### ◽ `mapDispatchToProps` 에 해당하는 파라미터: 액션 생성 함수로 이루어진 객체 형태

- `connect`함수가 `bindAtionCreators` 처리
- 형태

```jsx
export default connect(
  (state) => ({
    number: state.counter.number,
  }),
  {
    increase,
    decrease,
  }
)(CounterContainer);
```

---

- 참고
  '리액트를 다루는 기술'\_저자 김민준
