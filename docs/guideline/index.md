---
title: "풀 리퀘스트 및 마크다운 가이드라인"
---

# 풀 리퀘스트 및 마크다운 가이드라인

## 풀 리퀘스트 가이드라인
`0417taehyun`과 같이 본인의 깃헙 계정을 브랜치로 만든 뒤 `main` 브랜치에 풀 리퀘스트를 합니다. 이때 커밋은 `:memo: 글 제목`과 같이 작성합니다. 그리고 풀 리퀘스트 생성 이후 슬랙에 해당 사항을 공유하도록 합니다. 풀 리퀘스트를 할 때 확인해야 할 더 자세한 사항은 풀 리퀘스트를 했을 때 양식으로 만들어지는 체크 사항을 필히 확인하여 실수하지 않도록 합니다. 

## 마크다운 파일 가이드라인

마크다운 파일(`md`) 맨 위에 아래와 같은 코드를 작성합니다.  

```markdown
---
title: "글 제목"
author: "작성자"
date: "YYYY-MM-DD"
---

# "글 제목"
```

이때 `title` 및 `#`에는 글의 제목을 적습니다

!!! warning "주의"
    `#`이 글의 제목이기 때문에 `##`부터 목차로 들어가지게 됩니다.  

다음으로 `author`의 경우 글의 작성자, `date`의 경우 작성일자를 적습니다. `author`와 `date`는 각 글의 맨 아래 `작성자` 및 `작성일`로 들어가집니다.

### 파일명
`YYYY-MM-DD-글-제목.md`와 같이 `연도-월-일`을 파일명 제일 앞에 작성하며 그 뒤에 글 제목을 작성하게 됩니다. 해당 파일명이 곧 URL이 되기 때문에 `-`을 제외한 나머지 특수문자 및 띄워쓰기를 사용하지 않습니다.


### 특별한 마크다운 문법

블로그를 위해 `mkdocs` 및 `mkdocs-material`을 사용했습니다.

관련해서 특이한 문법을 몇 가지 소개합니다!  

## `docs_src`
직접 코드 소스파일을 마크다운에 가져와 사용할 수 있습니다. 이때 해당 소스 파일을 `docs_src`에 저장해야 합니다.  

예를 들어 `docs_src/guideline/test.py`라는 파일이 아래와 같이 존재합니다.

```python
def greeting(name):
    return f"Hello, {name}!
```    

이때 `python{!../docs_src/guideline/test.py!}`와 같이 사용할 수 있습니다. 그러면 아래와 같이 코드가 작성됩니다.

```python
{!../docs_src/guideline/test.py!}
```

#### 하이라이팅
이때 `python` 옆에 `python hl_lines=5-6`과 같이 작성하여 `1`에서 `2`번째 줄에 하이라이팅이 됩니다. 결과는 아래와 같습니다. 

```python hl_lines="1-2"
{!../docs_src/guideline/test.py!}
```

### `admonition`
`!!! note "참고"`와 같은 방법을 사용하여 일종의 참고할 사항을 따로 작성할 수 있습니다. 예를 들어 아래와 같습니다.

!!! note "참고"
    이곳은 참고사항입니다.

관련해서 `note` 외에도 사용할 수 있는 것들은 [이곳](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types)에서 확인할 수 있습니다. 이때 `"참고"`와 같은 `""`을 사용한 부분이 직접적인 보여지는 단어이며 실질적인 내용은 들여쓰기하여 작성해야 합니다.

### `termy`
CLI(Command Line Interface) 관련 명령어를 조금 더 멋지게 장식할 수 있습니다.

예를 들어 `$ pip install twil`이라는 명령어와 그에 대한 결괏값으로 `Successfully Installed twil`이라는 문장을 보여지게 한다고 생각해봅시다.

우선 `<div class="termy"> </div>`라는 `div` 태그를 만든뒤 그 내부에 `console $ pip install twil Successfully Installed twil`과 같이 작성합니다. 그 결과는 아래와 같습니다.  

<div class="termy">
    ``` sh
    $ echo "Hello TWIL"
    Hello TWIL
    ```
</div>
<br />

이때 `console` 부분은 들여쓰기 하며, `$`를 통해서 명령어가 실행되고 그 결괏값이 아래 나타나게 됩니다.

---

## 작성 로그

|작성자|수정 일자|수정 내용|
|:--:|:-----:|:-----:|
|이태현|2021. 10. 29. 금요일|첫 작성|


