---
title: "TS Refact Legacy2"
author: 이종호
date: "2021-08-08"
---

# TS Refact Legacy2

```ts
type Product = {
  id: number;
  name: string;
  detail: string;
  price: number;
  stock: number;
  count: number;
  shipping_fee: number;
  discount: number;
  minimum_free: number;
  imageList: string[];
  subItemList: Product[];

  currentImageUrl: string;
  subItemAddList: number[];
};

function ProductDetail() {
  const [product, setProduct] = useState<Product>({ // 일단 억지로 초기값설정
    id: 0,
    name: '',
    detail: '',
    price: 0,
    stock: 0,
    count: 0,
    shipping_fee: 0,
    discount: 0,
    minimum_free: 0,
    imageList: [],
    subItemList: [],

    currentImageUrl: '',
    subItemAddList: [],
  });
  ...
  
}
```

## is not assignable to parameter of type 'SetStateAction'...
![](https://images.velog.io/images/ljh95/post/cce71d6f-3b29-4431-ad1e-5d815673b012/image.png)

왜 스프레드 문법으로 객체 생성이 안되나 했는데, 컴포넌트에서 해당 state값에 **초기값이 설정되어 있지 않음**으로 내뱉는 에러인 듯 하다.

보고나니 맞는 말 같긴하다..
초기 값이 없으면 내부 속성값들이 전부 undefined형태인데 거기에 배열도 있으니 뭔가 안될만 하다.

단순 number나 string이라면 뒤에 undefined를 추가하는 것만으로 충분할지 모르지만, 
객체의 property중에 Reference타입이 있고, 초기값을 이용해야 할 경우 초기값을 설정해 줘야 겠다.



[https://dev.to/dwjohnston/react-usestate-argument-of-type-string-is-not-assignable-to-parameter-of-type-setstateaction-undefined-27po](https://dev.to/dwjohnston/react-usestate-argument-of-type-string-is-not-assignable-to-parameter-of-type-setstateaction-undefined-27po)