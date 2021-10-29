---
title: "[Redux] Redux Basics"
author: 정선미
date: "2021-07-18"
---

# [Redux] Redux Basics

## 🔶 개요
### ◾ 리덕스란?
   - 리액트 상태 관리 라이브러리 (가장 많이 사용하는)
   - 컴포넌트 상태 업데이트 관련 **로직**을 다른 파일로 **분리** → 더 **효율**적인 관리 가능
   - 컴포넌트끼리 **똑같은 상태 공유** 필요 시 → 여러 컴포넌트 거치지 않고 손쉽게 상태 값 전달/업데이트 가능
   - 최적화(실제 업데이트 필요한 컴포넌트만 리렌더링)
   - 전역 상태 관리 시 → 효과적
       - Context API
            - 같은 작업 가능. (리액트 v16.3 릴리즈로 개선 전, 사용 방식 불편했음)
            - 단순 전역 상태 관리만 필요 시→ 충분

       - ↕ 리덕스와 비교
            - 상태 관리 더 체계적 → 플젝 규모 클 때 좋음
            - 코드 유지 보수 ⬆
            - 작업 효율 극대화 ⬆
            - 개발자 도구 지원 (매우 편리)
            - 미들웨어 (기능) 제공 → 비동기 작업 훨씬 효율적 관리 가능

### ◾ 리액트 종속 라이브러리 x
   - 리액트에서 사용하려고 만들어졌지만
   - 다른 UI 라이브러리/프레임워크와 함께 사용 가능
       - 바닐라 자바스크립트(라이브러리/프레임워크 없이 사용하는 순수 자바스크립트 그 자체)와 함께 사용 가능
       
       
       
## 🔷 개념
### ◾ 액션 (action)
- 발생 : 상태에 변화 필요 시
- 하나의 객체로 표현
- 형식
```jsx
            // 1
            {
            	type: 'TOGGLE_VALUE'
            }

            // 2
            {
            	type: 'ADD_TODO',
            	data: {
            		id: 1,
            		text: '리덕스 배우기'
            	}
            }

            // 3
            {
            	type: 'CHANGE_INPUT',
            	text: '안녕하세요'
            }
```

- type
  - 필수
  - 액션 이름 같은 것
    - 문자열 형태
    - 주로 대문자
    - 고유해야
- type 외 값
  - 추후, 상태 업데이트 시 참고할 값
  - 작성자 마음대로

### ◾ 액션 생성 함수 (action creator)
- 액션 객체 만들어주는 함수
- 형식
```jsx
            // 화살표 함수
            const changeInput = text => ({
            	type: 'CHANGE_INPUT',
            	text
            })

            // 일반 함수
            function addTodo(data) {
            	return {
            		type: 'ADD_TODO',
            		DATA
            	}
            }
```

- 사용 이유
  - 변화 만들 때마다 액션 객체 만들어야 함.

       → 매번 (액션 객체를) 직접 작성하기 번거로움

       → 실수로 정보 놓칠 수 있음

       ⇒ 이런 일 방지

### ◾ 리듀서 (reducer)
- 변화를 일으키는 함수
- 실행 과정
  - 액션 만들어서 발생 → 리듀서의 parameter: `현재 상태 & 전달받은 액션 객체` 받음 → 두 값 참고 → 새로운 상태 반환
- 형태
```jsx
            const initialState = {
            	counter: 1
            }

            // state가 undefined일 때는 initialState를 기본값으로 사용
            function reducer(state = initialState, action) {
            	switch (action.type) {
            		case INCREMENT:
            			return {
            				...state, // 불변성 유지 (spread 연산자 사용 예시)
            				counter: state.counter + 1
            			};
            		default: 
            			return state;
            	}
            }
```

- 세팅
  - 리듀서 첫 호출 시, state 값 = undefined

    → undefined일 때, **`initialState`을 기본 값으로 설정**하기 위해 **함수 파라미터**에 기본 값 **설정**

  - 상태의 불변성 유지하면서 데이터 변화 시켜야 함

    → spread 연산자(...) 사용 

      - 🤚 리덕스 상태는 `최대한 깊지 않은 구조`로 진행 추천
        - 이유: spread 연산자로 `불변성 관리&업데이트`가 번거롭지 않기 위해
      - 객체 **구조 복잡 or 배열**도 다룰 경우 → `immer`라이브러리 사용하면 쉽게 리듀서 작성 가능
- 루트 리듀서 (rootReducer)
  - **스토어 만들 때** (`createStore` 함수를 사용하여) **리듀서 1개만** 사용해야 함

   → 리듀서를 1개로 합쳐야 함 

   → `combineReducers` 유틸 함수 (리덕스 제공) 사용하면 쉬움

  - 형태 예시

```jsx
                import { combineReducers } from 'redux';
                import counter from './counter'; // 리듀서 1
                import todos from './todos'; // 리듀서 2

                const rootReducer = combineReducers({
                  counter,
                  todos,
                });

                export default rootReducer;
```

### ◾ 스토어 (store)
- 플젝 1개 당 store 1개
- 스토어 내부
  - 현재 어플리케이션 상태
  - 리듀서
  - 몇 가지 중요한 내장 함수
- 만드는 법 & 형식
  - 만드는 법
    - createStore 함수 사용

      → 함수의 parameter에 리듀서 함수 넣기

  - 형식

```jsx
                import {createStore} from 'redux';

                (...)

                const store = createStore(reducer);
```

### ◾ 디스패치 (dispatch)
- (스토어 내장 함수 中 하나)
- 역할
  - 액션 발생시킴.
  - 액션을 스토어에 전달
- 사용 방식
  - 형태: `dispatch(action)`

  → 액션 객체를 파라미터로 넣어 호출

  → 호출 후:  스토어- 리듀서 함수 실행 → 새로운 상태 만듦

### ◾ 구독 (subscribe)
- 대체제: react-redux
- (스토어 내장 함수 中 하나)
- **subscribe 함수 내부에 함수**(listener)**를 파라미터로 넣어** 호출 시

  → 함수( listener )가 액션이 디스패치되어 **상태가 업데이트 될 때마다** **호출**됨

- 형태

```jsx
            const listener = () => {
            	console.log('상태가 업데이트됨');
            }
            const unsubscribe = store.subscribe(listener);

            unsubscribe(); // 추후 구독을 비활성화할 때 함수를 호출
```


## 🔶 리덕스의 세 가지 규칙
### 1. 단일 스토어
- 추천: 1 어플리케이션 : 1 스토어
- 이유
  - 여러 스토어 사용 가능→ 상태 관리 복잡해질 가능성 多
### 2. 읽기 전용 상태
- 리덕스 상태는 읽기 전용

 → 상태 업데이트 할 때

    - 기존 객체는 건드리지 x
    - 새 객체 생성
- 불변성 유지 이유
  - 얕은 비교 검사 하기 때문

    *얕은 비교 검사: 내부적으로 데이터 변경 감지하기 위함

### 3. 리듀서는 순수한 함수
- 조건
  1. 리듀서 함수의 parameter: 이전 상태 & 액션 객체
  2. parameter 외의 값→ 의존 x
  3. 이전 상태 건드리지 x & 변화 준 새 상태 객체를 만들어 반환
  4. 같은 parameter 호출된 리듀서 함수 → 같은 값 반환


## 🔷 리덕스 사용 패턴
### ◾ `프레젠테이셔널 / 컨테이너` 컴포넌트 분리 (필수 X)

![](https://images.velog.io/images/katej927/post/bb9d28ca-fd4a-46e5-aafc-9f48b0ad89ec/image.png)

- 프레젠테이셔널 컴포넌트
  - UI 컴포넌트 (상태 관리 X)
- 컨테이너 컴포넌트
  - 리덕스 연동 컴포넌트
    - 리덕스로부터 상태 받아옴
    - 리덕스 스토어에 액션을 디스패치
- 장점
  - 코드 재사용성 ⬆
  - 관심사 분리 → UI 작성시 좀 더 집중 가능

### ◾ 파일 구분 방식
- 리덕스 사용 시
  - `액션 타입`, `액션 생성 함수`, `리듀서` 코드 작성
  - 일반적인 구조
    - 디렉토리: actions, constants, reducers
      - 내부: 기능 별로 파일 1개씩

           ![](https://images.velog.io/images/katej927/post/9390adeb-ba54-4915-b985-c91a283dbd40/image.png)

   - Ducks 패턴
     - `액션 타입`, `액션 생성 함수`, `리듀서` → 기능 별로 파일 1개에 몰아서 다 작성

          ![](https://images.velog.io/images/katej927/post/8a8bd61c-797f-4465-9d8a-328583c2db9e/image.png)
          
          
- 참고
	'리액트를 다루는 기술'_저자 김민준