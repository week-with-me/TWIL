---
title: "React | useCallback vs useMemo vs useEffect"
author: "정선미"
date: "2021-10-31"
---

# React | useCallback vs useMemo vs useEffect

## 🔶 글 쓰게된 배경

> 3가지 hook의 구체적인 차이

3가지 hooks의 공통점은 dependency 관계의 변수 값 변화에 따라 연동되어 실행됩니다.

언뜻 보기에 유사한 기능을 구현하는 것 같은 세 hooks들의 구체적인 차이가 무엇인지 비교하기 위해 작성하게 되었습니다.

## 🔶 사전 지식

### ◼ **memoization**

> 컴퓨터 프로그래밍이 동일한 계산을 반복해야 할 때 이전에 계산한 값을 메모리에 저장하는 것

즉, 동일한 계산의 반복 수행을 제거함으로써 프로그램의 실행 속도를 향상 시키는 기술입니다.

### ◼ **useCallback, useMemo, useEffect**

[공식문서](https://ko.reactjs.org/docs/hooks-reference.html) 또는 요약된 글(**[useEffect](https://velog.io/@katej927/React-Hooks#3-effect-hook), [useCallback, useMemo](https://velog.io/@katej927/React-Hooks-qnqrwnon)**)을 참고하시길 바랍니다.

### ◼ 의존성 배열

> - 두 번째 매개변수

- 의존성 배열의 내용이 변경되었을 경우 부수 효과 함수가 실행

- 예시 코드

```jsx
// 의존성 배열 안에 있는 state
useEffect(() => {}, [state]);
```

## 🔶 useEffect

### ◼ 예시 코드

```jsx
useEffect(() => {
  const subscription = props.source.subscribe();
  return () => {
    subscription.unsubscribe();
  };
}, [props.source]);
```

### ◼ 차이점

1. class 컴포넌트의 life cycle 함수(side effect) 를 function 컴포넌트에도 동일하게 사용 가능하게 합니다.
2. 최초 컴포넌트 마운트 되는 경우, 컴포넌트 내 레이아웃 배치와 랜더링 완료된 후 실행합니다.
3. 2 번째 인자(배열)의 요소 지정 시, 해당 요소 값이 업데이트 되는 경우에만 실행합니다.

- 단점
  > **state나 props를 dependency로 지정 시, 불필요한 렌더링이 발생 가능합니다.**

## 🔶 useCallback

### ◼ 예시 코드

```jsx
const memoizedCallback = useCallback(() => {
  doSomething(a, b);
}, [a, b]);
```

### ◼ 차이점

> **memoization 된 콜백(함수) 자체를 반환**

- `useCallback(fn, deps)` 와 `useMemo(() => fn, deps)` 은 같습니다.
- 의존성 변경 시, 이전에 기억하고 있던 '함수' 자체와 비교한 뒤 다른 경우에만 리렌더합니다.

## 🔶 useMemo

### ◼ 예시 코드

```jsx
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

> **memoization 된 값을 반환**

- 의존성 변경 시, 이전에 기억하고 있던 리턴 값과 비교하여 다른 경우에만 리렌더합니다.

### ◼ 타 hooks 와 비교

- useEffect 와 차이점

  useMemo에서 전달된 함수는 렌더링 중 실행을 하지만,

  useEffect 에서 전달된 함수는 렌더링 중 실행을 하지 않습니다.

- useRef 와 차이점
  useMemo는 특정 함수의 리턴 값을 기억하지만,
  useRef는 DOM element의 특정 속성 값을 기억합니다.

---

- 참고
  - [리액트 공식문서](https://ko.reactjs.org/docs/hooks-reference.html)
  - [메모이제이션\_위키백과](https://ko.wikipedia.org/wiki/%EB%A9%94%EB%AA%A8%EC%9D%B4%EC%A0%9C%EC%9D%B4%EC%85%98)
  - [React | Hooks 01 ( 개요 / state / effect )](https://velog.io/@katej927/React-Hooks#3-effect-hook)
  - [React | Hooks 02 ( useReducer / useMemo / useCallback / useRef / 커스텀 hooks)](https://velog.io/@katej927/React-Hooks-qnqrwnon)
  - [useEffect, useCallback, useMemo 비교](https://velog.io/@mementomori/useEffect-useCallback-useMemo-%EB%B9%84%EA%B5%90)
  - [TIL no.36 - React Hooks useEffect 의존성 배열 ?!](https://choihaneul9545.tistory.com/38)
