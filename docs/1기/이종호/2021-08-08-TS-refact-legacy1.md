---
title: "TS Refact Legacy1"
author: 이종호
date: "2021-08-08"
---

# TS Refact Legacy1

## fetch headers 설정
```ts
const requestHeaders: HeadersInit = new Headers();
  requestHeaders.set('Content-Type', 'application/json');
  requestHeaders.set(
    'Authorization',
    localStorage
      ?.getItem('token')
      ?.slice(1, localStorage.getItem('token')!.length - 1) || 'no token'
  );


fetch('http://18.116.64.187:8000/carts', {
        method: 'POST',
        headers: requestHeaders,
        body: JSON.stringify({
          products: [...productEntitiy, { product_id: id, count: count }],
        }),
})
  .then(res => res.json())
  .then(data => {
  console.log('detail');
  console.log(data);
});

```
requestHeader에 타입을 지정하기 위해선, 이렇게 해야하는 듯 하다.

----
----

![](https://images.velog.io/images/16616516/post/63988d19-c838-43aa-b476-8df5ae14851e/image.png)
`headers`는 `HeadersInit`타입을 가지고있고

----

![](https://images.velog.io/images/16616516/post/30d0687d-801b-4c67-94d0-d8544ce95200/image.png)
`HeadersInit`은 `Headers`, `string[][]`, `Recode<string, string>`형태를 가질 수 있다.

----
----

```ts
/** This Fetch API interface allows you to perform various actions on HTTP request and response headers. These actions include retrieving, setting, adding to, and removing. A Headers object has an associated header list, which is initially empty and consists of zero or more name and value pairs.  You can add to this using methods like append() (see Examples.) In all methods of this interface, header names are matched by case-insensitive byte sequence. */
interface Headers {
    append(name: string, value: string): void;
    delete(name: string): void;
    get(name: string): string | null;
    has(name: string): boolean;
    set(name: string, value: string): void; // 우리가 사용한 메서드!!!!!!
    forEach(callbackfn: (value: string, key: string, parent: Headers) => void, thisArg?: any): void;
}

declare var Headers: {
    prototype: Headers;
    new(init?: HeadersInit): Headers;
};
```
> **주석을 해석한 글**
> 
> 이 Fetch API 인터페이스를 사용하면 HTTP 요청 및 응답 헤더에 대해 다양한 작업을 수행할 수 있습니다. 이러한 작업에는 검색, 설정, 추가 및 제거가 포함됩니다. 헤더 개체에는 처음에는 비어 있고 0개 이상의 이름과 값 쌍으로 구성된 연결된 헤더 목록이 있습니다.  adpend()와 같은 메서드를 사용하여 이 메서드에 추가할 수 있습니다(예제 참조). 이 인터페이스의 모든 메서드에서 헤더 이름은 대소문자를 구분하지 않는 바이트 시퀀스로 일치합니다.

`Headers`는 이런 식으로 구성되어 있는데,
![](https://images.velog.io/images/16616516/post/03a3a0a2-3544-4395-81f5-885541528aad/image.png)
그래서 이런 식으로 `set`메소드를 통해 값을 `키 값` 형태로 지정할 수 있나 싶다.

### 결론.
- fetch에서 requestHeaders를 설정하려면, 특정 인터페이스에 속한 타입을 만들어야하고 => `new Headers()`
- 속성 값은 set함수를 통해 설정할 수 있다.
