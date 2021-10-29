---
title: "TS Introduction"
author: 이종호
date: "2021-07-11"
---

# TS Introduction

## Introduction
> JavaScript that scales
> - TypeScript 캐치 프레이즈

[TypeScript](https://www.typescriptlang.org/)는 MS에서 개발하여 2012년에 발표한 JavaScript로 컴파일 되는 언어이다. Javascript에 정적 타이핑과 ES2015를 기반으로 하는 객체지향적 문법이 추가된 것을 주요 특징으로 한다.
나올 당시에는 Windows 이외의 다른 개발 환경이 미비해서 부정적인 의견도 적기 않았던 것으로 알고 있지만, 생태계 지원이 점점 확장되고, 최근에 Angular 팀에서 이 언어를 메인 언어로 태책하면서 현재로서는 정적 타이핑을 지원하는 다른 JavaScript 전처리기 (Flow 등)에 비해서 컴뮤니티나 안정성 측면에서 앞서나가는 모양새다.

JavaScript로 컴파일 되는 언어라고 하니 CoffeeScript가 떠오른다. 그러나 TypeSCript는 CoffeScript와는 달리 JavaScript의 Superset이라는 차이점이 있다. 즉, 지금까지 사용했던 익숙한 JavaScript의 문법을 사용하면서도 코딩이 가능하다. 특히, TypeScript는 ES2015문법도 지원하므로 TypScript 이외의 별도 Transpiler를 사용하지 않아도 ES2015 기능들을 브라우저에서 사용할 수 잇다는 장점도 있다. 게다가 미래의 ECMAScript Feature들도 계속해서 지원할 예정이므로 표준에서 벗어날 걱정도 덜 수 있겠다.

TypeScript는 오픈 소스이며, 마이크로소프트는 TypeScript를 계속해서 개선하고 있다. 최근에는 V2.0 버전이 배포되었고 여러가지 기능이나 이슈는 지금도 계속 보완되는 중이다.

### Why use?
TypeScript를 사용하면 정적 타이핑이 가지는 장점을 JavaScript에 적용할 수 있다. 정적 타이핑은 컴파일 타임에 타입체크를 한다. 당연히 에러는 발생하지 않는게 가장 좋지만, 만약 발생했다면 컴파일타이 에러가 런타임 에러보다 낫다.

문서화 측면에서도 뛰어나다. JavaScript 문서화 도구인 JSDoc이 Type annotation을 지원하느 것과 일맥상통한다. 제대로 된 Type annotation은 그 자체로 문서화다.

물론 정적 타이핑과 동적 타이핑은 무엇이 우위라고 볼 수 없는 것이 사실이다. 이 관계에는 Trade-off가 있다고 볼 수 있으며, 일반적으로 꼽는 정적 타이핑의 단점은 바로 생산성이다. 때문에 TypScript에서는 생산성보다는 안정성이 중요시된는 대규모 JavaScript 어플리케이션 개발에 적합하다고 한 것이다.

### Features
TypeScript의 기능들은 크게 보면 정적 파이핑과 ECMASCript구현으로 나뉠 수 있다.
- Type annotation & 정적 타입 체크
- 타입 추론
- Interfaces
- ES2015 FEatures
  - `let` & `const`
  - Block scope
  - Arrow function
  - Classes
  - Promise
  - Etc...
- Namespaces & Modules(CommonJS, ES2015, AMD)
- Generic
- Mixin
