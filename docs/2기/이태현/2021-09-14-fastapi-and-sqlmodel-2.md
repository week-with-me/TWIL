---
title: "[ 공식 문서로 배우는 FastAPI & SQLModel ] 02. FastAPI 설치와 웹 애플리케이션 서버"
author: "이태현"
date: "2021-09-14"
---

# [ 공식 문서로 배우는 FastAPI & SQLModel ] 02. FastAPI 설치와 웹 애플리케이션 서버

![](../../images/2기/이태현/2주차/0.png)

## 도입
지난 시간 우리는 **FastAPI**의 특징에 대해 간단하게 살펴보았습니다.   

Django, Flask 등의 다른 파이썬 웹 프레임워크와의 비교를 통한 대략적인 FastAPI 특징에 대한 부분은 아래 글을 참고하시면 됩니다.

[[ 공식 문서로 배우는 FastAPI & SQLModel ] 01. FastAPI 소개](https://twil.weekwith.me/2%EA%B8%B0/%EC%9D%B4%ED%83%9C%ED%98%84/2021-09-05-fastapi-and-sqlmodel-1/)

오늘은 본격적으로 **FastAPI**를 설치하고 사용해보며, 이 과정에서 필요한 지식인 웹 애플리케이션 서버에 관해 알아보겠습니다.  


## FastAPI 설치 및 작동
### 설치
우선 `fastapi`와 `uvicorn`을 설치해야 합니다.  

터미널에서 `pip install fastapi`, `pip install uvicorn` 명령어를 사용하여 `fastapi`, `uvicorn` 를 설치할 수 있습니다.  

설치 이후 `pip freeze` 명령어를 통해 아래와 같은 의존성 패키지들을 확인할 수 있으면 정상적으로 설치된 것입니다.  

!!! note "참고"

    저는 현재 운영체제로 맥 OS(Mac OS)을 사용 중입니다.

    윈도우의 경우 리눅스 또는 맥과 명령어에 차이점이 존재할 수 있습니다.


<div class="termy">
    ```sh
    $ pip freeze
    asgiref==3.4.1
    certifi==2021.5.30
    click==8.0.1
    fastapi==0.68.1
    h11==0.12.0
    pydantic==1.8.2
    starlette==0.14.2
    typing-extensions==3.10.0.2
    uvicorn==0.15.0
    ```
</div>


### 작성
이제 `main.py`라는 폴더를 만든 이후 아래와 같이 코드를 작성합니다.  

```python
{!../docs_src/2기/이태현/2주차/main.py!}
```

`fastapi` 패키지에서 `FastAPI` 클래스를 임포트한 뒤 `app`이라는 변수에 할당합니다.  

`{"message": "pong"}`이라는 파이썬 딕셔너리를 반환하는 `test()`라는 함수를 만듭니다.  

`@app.get("/ping")`이라는 파이썬 데코레이터를 작성하여 `test()` 함수를 감쌉니다.

!!! note "참고"

    파이썬 데코레이터, `get` 과 같은 엔드포인트 및 HTTP 통신에 관한 부분은 다음에 설명드릴 예정입니다.

    또한 실제 공식 문서에서는 이전에 언급했던 FastAPI의 특징 중 하나인 비동기를 활용하여 `async` 사용한 `root()` 함수로 작성 되어있습니다.

    비동기와 관련해서도 추후 설명드릴 예정이라 우선은 비동기가 아닌 동기적으로 동작하게 함수를 작성하였습니다.


### 작동
이렇게 파일을 작성했다면 이제 서버를 돌려볼 차례입니다.  

다시 터미널 창으로 돌아와 `uvicorn main:app` 명령어를 입력합니다.  

아래와 같이 서버가 구동되면 성공입니다.  

<div class="termy">
    ```sh
    $ uvicorn main:app

    INFO:     Started server process [73844]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    ```
</div>


`unvicorn`은 웹 애플리케이션 서버(WEB Application Server)로, 쉽게 말해 `uvicorn`을 통해 서버를 구동하는 걸 의미합니다.  

그리고 `main:app`은 `main`이라는 파일에 존재하는 `app`을 실행시키라는 의미입니다.  

그러면 이제 위 터미널 창에 명시된 [http://127.0.0.1:8000](http://127.0.0.1:8000) 주소로 한 번 접속해봅시다.  

아래와 같이 `{"detail": "Not Found"}`라고 뜨는 걸 확인할 수 있습니다.

```json
{
    "detail": "Not Found"
}
```

!!! note "참고"

    웹 브라우저를 통해 접속을 할 때 크롬(Chrome) 브라우저를 사용하는 게 가장 좋습니다.


그러면 이제 [http://127.0.0.1:8000/ping](http://127.0.0.1:8000/ping) 주소로 한 번 접속해봅시다.  

아래 이미지와 같이 `{"message": "pong"}`이라고 뜨는 걸 확인할 수 있습니다.  

```json
{
    "detail": "Not Found"
}
```

그리고 이 과정을 통해 우리가 `test()`라는 함수에 반환값으로 입력한 딕셔너리가 그대로 반환된 것을 알 수 있습니다.  

두 번의 접속 이후 다시 터미널 창을 봤을 때 아래 이미지와 같이 로그가 찍혀있는 것을 확인할 수 있습니다.  

<div class="termy">
    ```sh
    INFO:     127.0.0.1:58175 - "GET / HTTP/1.1" 404 Not Found
    INFO:     127.0.0.1:58175 - "GET /ping HTTP/1.1" 200 OK
    ```
</div>

!!! note "참고"
    `GET`이라는 HTTP 메서드, `/`와 `/ping`이라는 엔드포인트, `404`와 `200`이라는 상태 코드(Status Code) 등에 관해서는 다음 시간에 더 자세히 살펴보려고 합니다.

    혹시 미리 궁금하신 분들은 MDN에 게시된 [HTTP 개요](https://developer.mozilla.org/ko/docs/Web/HTTP/Overview)를 읽어보시기 바랍니다.


많은 의문들이 남아 있을 수 있습니다.  

`127.0.0.1:8000`이라는 주소는 무엇이며, HTTP 통신은 무엇을 의미하고 웹 애플리케이션 서버는 무엇인지 감이 안 오실 수 있습니다.  

오늘은 이 중에서 서버에 관한 부분만 우선 살펴보고자 합니다.  

URL 및 HTTP 통신에 관한 부분은 다음 주에 더 자세히 알아보겠습니다.  


## 서버(Server)
### 도입
서버의 종류에는 크게 두 가지가 있습니다. 바로 웹 서버(WEB Server)와 웹 애플리케이션 서버(WAS__WEB Application Server)입니다.  

웹 서버와 웹 애플리케이션 서버의 차이점에 대해 알아보기 전에 우선 애플리케이션(Application)에 관해 알아봅시다.  

### 애플리케이션(Application)
흔히 줄여서 앱이라 불리는 애플리케이션은 쉽게 말해 특정 목적을 위해 제작된 프로그램을 의미합니다.  

우리가 현재 살펴보고 있는 **FastAPI**도 결국 웹이라고 하는 특정 목적을 위한 프로그램 제작을 위해 사용되는 것입니다.  

따라서 **FastAPI**를 통해 하나의 애플리케이션을 만들 수 있는 것이고, 웹을 위해 제작을 하고 있기 때문에 이를 웹 애플리케이션(WEB Application)이라 합니다.  

### 웹 애플리케이션(WEB Application)
웹 애플리케이션을 제작할 때는 조금 더 두드러진 특징이 있습니다.  

바로 웹 브라우저, 중간(엔진), 데이터베이스로 계층이 나눠져있다는 것입니다.  

이 과정을 풀어서 설명하면 사용자가 웹 브라우저에서 어떤 특정 동작, 이를 테면 로그인과 같은 액션(Action)을 수행하면 해당 액션에 대한 요청(Request)을 중간 계층이라 할 수 있는 서버로 보내게 되고 서버는 데이터베이스(DB__Database)에서 그에 맞는 데이터를 가져와 다시 웹 브라우저로 응답(Response)하게 됩니다.  

우리가 앞서 구현한 `test()` 함수의 경우 실제 데이터베이스를 거치지는 않았지만 결국 웹 브라우저의 [http://127.0.0.1:8000/ping](http://127.0.0.1:8000/ping) 에서의 `GET` 요청(Request)에 의해 그에 알맞은 반환값인 `{"message": "pong"}`으로 웹 브라우저에 응답(Response)했습니다.  

이를 통해 우리가 알 수 있는 사실은 아래와 같습니다.  

* **FastAPI**를 통해 웹 애플리케이션을 만든다.
* 웹 브라우저에서의 특정 요청에 알맞는 응답을 만들어야 한다.
* 어떤 요청들의 경우 데이터베이스를 통해 응답해야 한다.

### 웹 서버(WEB Server)
이러한 개념 속에서 서버라는 게 등장합니다.  

어떤 요청을 받았을 때 그에 알맞은 응답을 반환하기 위해 서버가 존재하는 것입니다.  

위 과정을 통해 도출한 웹 서버의 개념을 간단하게 도식화하면 아래 이미지와 같습니다.  


![](../../images/2기/이태현/2주차/1.png)

이때 웹 서버는 정적인 정보만 반환합니다. 이와 반대로 계속 언급되던 웹 애플리케이션 서버(WAS)는 동적인 정보를 반환합니다.  

그렇다면 우선 정적인 정보와 동적인 정보의 차이점 먼저 살펴봅시다.  



#### 정적인 정보(Static Contents)
정적인 정보에는 HTML, CSS, 이미지 등이 존재합니다.  

컴퓨터에 저장되어 있는 파일들로 요청에 알맞게 해당 파일을 반환하며 항상 동일한 페이지를 유지합니다.  

'정적이다'는 의미에서도 알 수 있듯이 말 그대로 바뀌지 않고 유지되는 것들을 의미합니다.  

그리고 이러한 정적인 정보들을 통해 만들어지는 페이지를 정적인 페이지(Static Page)라고 합니다.  

#### 동적인 정보(Dynamic Contents)
동적인 정보에는 서버 내의 로직이나 데이터베이스를 통해 받아오는 것들이 포함됩니다.  

서버 내의 로직이라 하면 쉽게 우리가 앞서 작성한 `test()` 함수를 예로 들 수 있습니다.  

만약 `test()` 함수의 반환값(`return`)을 `{"message": "pong"}`이 아닌 `{"message": "Hello"}`로 바꾼다면 웹 브라우저에는 `{"message": "Hello"}`가 출력됩니다.  

위 예시처럼, 또 '동적이다'는 의미에서도 알 수 있듯이 말 그대로 변화하는 것들을 의미합니다.  

그리고 이러한 동적인 정보들을 통해 만들어지는 페이지를 동적인 페이지(Dynamic Page)라고 합니다.  

### 웹 애플리케이션 서버(WAS__WEB Application Server)
웹 애플리케이션 서버(WAS)는 위에서 언급한 것처럼 동적인 정보(Dynamic Contents)를 주고 받습니다.  

우리는 `test()`라는 함수를 통해 `{"message": "pong"}`이라는 동적 데이터를 요청(Request, `GET /ping`)에 따라 응답(Response)했습니다.  

그리고 이 과정에서 만약 반환값(`return`)을 다르게 바꾸었다면, 다른 응답(Response)을 웹 브라우저에서 출력한다는 걸 알게 됐습니다.  

이러한 맥락에서 `uvicorn`은 파이썬 웹 애플리케이션 서버(WAS)입니다. 그리고 그 중에서도 **FastAPI**에서 사용하기 좋게 특화되어 있습니다.  

파이썬에는 `uvicorn` 외에도 [`gunicorn`](https://gunicorn.org/) 등 다양한 웹 애플리케이션 서버(WAS)가 존재합니다.  

**FastAPI**에서 `unvicorn`을 사용하고, 또 이것이 특화되어 있는 이유는 바로 비동기 서버를 쉽게 구축할 수 있기 때문입니다.  

이에 관해서는 추후에 더 자세히 알아볼 예정입니다.  

### 결론
동적인 정보를 다루기 위해 웹 애플리케이션 서버(WAS)가 필요합니다. 그리고 **FastAPI**와 **SQLModel**를 활용하여 우리는 앞으로 동적인 정보들을 다룰 것입니다.  

더욱이 최근 웹 애플리케이션 서버는 정적인 정보들까지도 다룰 수 있게 진화하였습니다. 그렇다면 왜 웹 서버를 여전히 사용하는지 의문이 들 수 있습니다.  

동적인 정보들은 말 그대로 변화를 하기 때문에 결국 서버 및 데이터베이스에서 그만큼 작업해야 할 것들이 많다는 걸 의미합니다.  

반대로 정적인 정보들은 정해진 데이터를 넘겨주면 되기 때문에 상대적으로 빠릅니다.  

따라서 웹 서버와 웹 애플리케이션 서버(WAS)를 분리하여 구성할 경우 서버 부하에 관한 부분을 어느 정도 해결할 수 있습니다.  

쉽게 생각하면 들어오는 주문에 따라 재료 손질, 조리까지 해야하는 요리사에게 단순 설거지까지 맡기지 않고, 단순한 설거지는 담당 아르바이트 생을 따로 두는 것과 같습니다.  

이 밖에도 SSL(Secoure Socket Layer)과 같은 보안과 로드 밸런싱(Load Balancing) 등 더 다양한 개념이 필요하지만 이는 추후에 더 설명하도록 하겠습니다.  

---

## 참고
`fastapi` 및 `uvicorn` 설치와 간단한 첫 함수 작동에 대한 공식 문서 번역은 아래 글들을 확인해주시기 바랍니다.  

* [튜토리얼 - 사용자 안내서 - 도입부]()
* [첫 단계]()


## 코드
본문에서 사용한 코드는 아래 GitHub 저장소에서 확인하실 수 있습니다.  

모든 커밋은 해당 게시글의 이름을 따릅니다.

[https://github.com/week-with-me/fastapi-practice](https://github.com/week-with-me/fastapi-practice)
