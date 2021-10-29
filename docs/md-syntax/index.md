---
title: "마크다운 문법 소개"
---

# 마크다운 문법 소개

블로그를 위해 `mkdocs` 및 `mkdocs-material`을 사용했습니다.

관련해서 특이한 문법을 몇 가지 소개합니다!  

## `docs_src`
직접 코드 소스파일을 마크다운에 가져와 사용할 수 있습니다. 이때 해당 소스 파일을 `docs_src`에 저장해야 합니다.  

예를 들어 `docs_src/md-syntax/test.py`라는 파일이 아래와 같이 존재합니다.

```python
def greeting(name):
    return f"Hello, {name}!"

def get_name(name):
    greeting(name)
```

이때 `python{!../docs_src/md-syntax/test.py!}`와 같이 사용할 수 있습니다. 그러면 아래와 같이 코드가 작성됩니다.

```python
{!../docs_src/md-syntax/test.py!}
```

### 하이라이팅
이때 `python` 옆에 `python hl_lines=5-6`과 같이 작성하여 `5`에서 `6`번째 줄에 하이라이팅이 됩니다. 결과는 아래와 같습니다. 

```python hl_lines=5-6
{!../docs_src/md-syntax/test.py!}
```

## `admonition`
`!!! note "참고"`와 같은 방법을 사용하여 일종의 참고할 사항을 따로 작성할 수 있습니다. 예를 들어 아래와 같습니다.

!!! note "참고"
    이곳은 참고사항입니다.

관련해서 `note` 외에도 사용할 수 있는 것들은 [이곳](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types)에서 확인할 수 있습니다. 이때 `"참고"`와 같은 `""`을 사용한 부분이 직접적인 보여지는 단어이며 실질적인 내용은 들여쓰기하여 작성해야 합니다.

## `termy`
CLI(Command Line Interface) 관련 명령어를 조금 더 멋지게 장식할 수 있습니다.

예를 들어 `$ pip install twil`이라는 명령어와 그에 대한 결괏값으로 `Successfully Installed twil`이라는 문장을 보여지게 한다고 생각해봅시다.

우선 `<div class="termy"> </div>`라는 `div` 태그를 만든뒤 그 내부에 `console $ pip install twil Successfully Installed twil`과 같이 작성합니다. 그 결과는 아래와 같습니다.  

<div class="termy">
    ``` console
    $ pip install

    Successfully Installed twil
    ```
</div>
<br />

이때 `console` 부분은 들여쓰기 하며, `$`를 통해서 명령어가 실행되고 그 결괏값이 아래 나타나게 됩니다.

---

## 마크다운 문법 소개 로그

|작성자|수정 일자|수정 내용|
|:--:|:-----:|:-----:|
|이태현|2021. 10. 29. 금요일|첫 소개 작성|


