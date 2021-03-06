---
title: "React | useCallback vs useMemo vs useEffect"
author: "์ ์ ๋ฏธ"
date: "2021-10-31"
---

# React | useCallback vs useMemo vs useEffect

## ๐ถ ๊ธ ์ฐ๊ฒ๋ ๋ฐฐ๊ฒฝ

> 3๊ฐ์ง hook์ ๊ตฌ์ฒด์ ์ธ ์ฐจ์ด

3๊ฐ์ง hooks์ ๊ณตํต์ ์ dependency ๊ด๊ณ์ ๋ณ์ ๊ฐ ๋ณํ์ ๋ฐ๋ผ ์ฐ๋๋์ด ์คํ๋ฉ๋๋ค.

์ธ๋ป ๋ณด๊ธฐ์ ์ ์ฌํ ๊ธฐ๋ฅ์ ๊ตฌํํ๋ ๊ฒ ๊ฐ์ ์ธ hooks๋ค์ ๊ตฌ์ฒด์ ์ธ ์ฐจ์ด๊ฐ ๋ฌด์์ธ์ง ๋น๊ตํ๊ธฐ ์ํด ์์ฑํ๊ฒ ๋์์ต๋๋ค.

## ๐ถ ์ฌ์  ์ง์

### โผ **memoization**

> ์ปดํจํฐ ํ๋ก๊ทธ๋๋ฐ์ด ๋์ผํ ๊ณ์ฐ์ ๋ฐ๋ณตํด์ผ ํ  ๋ ์ด์ ์ ๊ณ์ฐํ ๊ฐ์ ๋ฉ๋ชจ๋ฆฌ์ ์ ์ฅํ๋ ๊ฒ

์ฆ, ๋์ผํ ๊ณ์ฐ์ ๋ฐ๋ณต ์ํ์ ์ ๊ฑฐํจ์ผ๋ก์จ ํ๋ก๊ทธ๋จ์ ์คํ ์๋๋ฅผ ํฅ์ ์ํค๋ ๊ธฐ์ ์๋๋ค.

### โผ **useCallback, useMemo, useEffect**

[๊ณต์๋ฌธ์](https://ko.reactjs.org/docs/hooks-reference.html) ๋๋ ์์ฝ๋ ๊ธ(**[useEffect](https://velog.io/@katej927/React-Hooks#3-effect-hook), [useCallback, useMemo](https://velog.io/@katej927/React-Hooks-qnqrwnon)**)์ ์ฐธ๊ณ ํ์๊ธธ ๋ฐ๋๋๋ค.

### โผ ์์กด์ฑ ๋ฐฐ์ด

> - ๋ ๋ฒ์งธ ๋งค๊ฐ๋ณ์

- ์์กด์ฑ ๋ฐฐ์ด์ ๋ด์ฉ์ด ๋ณ๊ฒฝ๋์์ ๊ฒฝ์ฐ ๋ถ์ ํจ๊ณผ ํจ์๊ฐ ์คํ

- ์์ ์ฝ๋

```jsx
// ์์กด์ฑ ๋ฐฐ์ด ์์ ์๋ state
useEffect(() => {}, [state]);
```

## ๐ถ useEffect

### โผ ์์ ์ฝ๋

```jsx
useEffect(() => {
  const subscription = props.source.subscribe();
  return () => {
    subscription.unsubscribe();
  };
}, [props.source]);
```

### โผ ์ฐจ์ด์ 

1. class ์ปดํฌ๋ํธ์ life cycle ํจ์(side effect) ๋ฅผ function ์ปดํฌ๋ํธ์๋ ๋์ผํ๊ฒ ์ฌ์ฉ ๊ฐ๋ฅํ๊ฒ ํฉ๋๋ค.
2. ์ต์ด ์ปดํฌ๋ํธ ๋ง์ดํธ ๋๋ ๊ฒฝ์ฐ, ์ปดํฌ๋ํธ ๋ด ๋ ์ด์์ ๋ฐฐ์น์ ๋๋๋ง ์๋ฃ๋ ํ ์คํํฉ๋๋ค.
3. 2 ๋ฒ์งธ ์ธ์(๋ฐฐ์ด)์ ์์ ์ง์  ์, ํด๋น ์์ ๊ฐ์ด ์๋ฐ์ดํธ ๋๋ ๊ฒฝ์ฐ์๋ง ์คํํฉ๋๋ค.

- ๋จ์ 
  > **state๋ props๋ฅผ dependency๋ก ์ง์  ์, ๋ถํ์ํ ๋ ๋๋ง์ด ๋ฐ์ ๊ฐ๋ฅํฉ๋๋ค.**

## ๐ถ useCallback

### โผ ์์ ์ฝ๋

```jsx
const memoizedCallback = useCallback(() => {
  doSomething(a, b);
}, [a, b]);
```

### โผ ์ฐจ์ด์ 

> **memoization ๋ ์ฝ๋ฐฑ(ํจ์) ์์ฒด๋ฅผ ๋ฐํ**

- `useCallback(fn, deps)` ์ `useMemo(() => fn, deps)` ์ ๊ฐ์ต๋๋ค.
- ์์กด์ฑ ๋ณ๊ฒฝ ์, ์ด์ ์ ๊ธฐ์ตํ๊ณ  ์๋ 'ํจ์' ์์ฒด์ ๋น๊ตํ ๋ค ๋ค๋ฅธ ๊ฒฝ์ฐ์๋ง ๋ฆฌ๋ ๋ํฉ๋๋ค.

## ๐ถ useMemo

### โผ ์์ ์ฝ๋

```jsx
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

> **memoization ๋ ๊ฐ์ ๋ฐํ**

- ์์กด์ฑ ๋ณ๊ฒฝ ์, ์ด์ ์ ๊ธฐ์ตํ๊ณ  ์๋ ๋ฆฌํด ๊ฐ๊ณผ ๋น๊ตํ์ฌ ๋ค๋ฅธ ๊ฒฝ์ฐ์๋ง ๋ฆฌ๋ ๋ํฉ๋๋ค.

### โผ ํ hooks ์ ๋น๊ต

- useEffect ์ ์ฐจ์ด์ 

  useMemo์์ ์ ๋ฌ๋ ํจ์๋ ๋ ๋๋ง ์ค ์คํ์ ํ์ง๋ง,

  useEffect ์์ ์ ๋ฌ๋ ํจ์๋ ๋ ๋๋ง ์ค ์คํ์ ํ์ง ์์ต๋๋ค.

- useRef ์ ์ฐจ์ด์ 
  useMemo๋ ํน์  ํจ์์ ๋ฆฌํด ๊ฐ์ ๊ธฐ์ตํ์ง๋ง,
  useRef๋ DOM element์ ํน์  ์์ฑ ๊ฐ์ ๊ธฐ์ตํฉ๋๋ค.

---

- ์ฐธ๊ณ 
  - [๋ฆฌ์กํธ ๊ณต์๋ฌธ์](https://ko.reactjs.org/docs/hooks-reference.html)
  - [๋ฉ๋ชจ์ด์ ์ด์\_์ํค๋ฐฑ๊ณผ](https://ko.wikipedia.org/wiki/%EB%A9%94%EB%AA%A8%EC%9D%B4%EC%A0%9C%EC%9D%B4%EC%85%98)
  - [React | Hooks 01 ( ๊ฐ์ / state / effect )](https://velog.io/@katej927/React-Hooks#3-effect-hook)
  - [React | Hooks 02 ( useReducer / useMemo / useCallback / useRef / ์ปค์คํ hooks)](https://velog.io/@katej927/React-Hooks-qnqrwnon)
  - [useEffect, useCallback, useMemo ๋น๊ต](https://velog.io/@mementomori/useEffect-useCallback-useMemo-%EB%B9%84%EA%B5%90)
  - [TIL no.36 - React Hooks useEffect ์์กด์ฑ ๋ฐฐ์ด ?!](https://choihaneul9545.tistory.com/38)
