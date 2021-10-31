# awk로 표 형식의 데이터를 쉽게 가공해보자!

 `awk`는 패턴과 일치하는 문자열을 검색할 때 사용하는 명령어입니다.  
어 잠깐만요! 그건 `grep` 아닌가요?  
네 맞습니다. `grep`이라는 명령어 또한 패턴과 일치하는 문자열을 찾을 때 사용합니다.  
그럼 `awk`와 `grep`의 차이는 무엇일까요?  
 `grep`은 라인 단위로 패턴을 검색합니다. 결과 또한 라인을 반환하죠.  
옵션 또한 검색된 라인을 기준으로 무엇을 더 보여줄까! 하는 내용이 많습니다.  
보통 정형화되지 않은 텍스트를 검색할 때 사용합니다.  
반면, `awk`는 정형화된 데이터를 대상으로 검색할 때 유리합니다.  
여기서 말하는 정형화된 데이터는 `공백` 또는 `특정 기호`로 구분된 `정해진 형식의 데이터`를 말합니다.  

 좋은 예로 실행중인 프로세스 정보를 출력하는 `ps -ef`가 있네요!  
```shell
[centos@localhost ~]$ ps -ef
UID         PID   PPID  C STIME TTY          TIME CMD
root          1      0  0 10월19 ?      00:00:35 /usr/lib/systemd/systemd --switched-root --sys
root          2      0  0 10월19 ?      00:00:00 [kthreadd]
root          4      2  0 10월19 ?      00:00:00 [kworker/0:0H]
root          6      2  0 10월19 ?      00:00:09 [ksoftirqd/0]
root          7      2  0 10월19 ?      00:00:00 [migration/0]
root          8      2  0 10월19 ?      00:00:00 [rcu_bh]
root          9      2  0 10월19 ?      00:00:26 [rcu_sched]
root         10      2  0 10월19 ?      00:00:00 [lru-add-drain]
...생략...
```

위 정보에서 PID가 10인 프로세스의 정보를 찾으려면 어떻게 하는게 좋을까요? 
먼저 `grep`의 경우를 볼까요?  
`ps ef | grep 10`은 아쉽게도 `STIME`의 `10월19`도 같이 검색하기 때문에 원하는 데이터만 얻기는 어렵습니다.  
하지만 `awk`는 필드(열) 기준으로 검색하므로 쉽게 원하는 데이터를 얻습니다.  
`ps ef | awk '$2 == 10 { print }'`  
아직은 어떻게 사용하는건지 감이 안오신다구요?  
괜찮습니다! 기초적인 사용방법은 어렵지 않거든요.  
그럼 같이 `awk`를 알아보러 가볼까요?  


참고로 awk라는 이름은 `awk`를 개발한 Alfredo **A**ho, Peter **W**einberger, Brian **K**ernighan 의 이름을 따서 만들어졌습니다. 

아래는 이번 실습에 사용할 `sample.txt`입니다.  
```sh
# sample.txt
drwxrwxr-x. 4 centos centos    198  5월 22  2020 .
drwxrwxr-x. 3 centos centos     59 10월 31 13:55 ..
drwxrwxr-x. 2 centos centos     87  5월 20  2020 File
-rw-rw-r--. 1 centos centos     60  5월 21  2020 Separator.txt
-rw-rw----. 1 centos centos  65942  5월 15  2020 aa.txt
-rw-------. 1 centos centos     30  5월 19  2020 amin.txt
-rw-rw----. 1 centos centos  65942  5월 15  2020 bb.txt
-rw-rw-r--. 1 centos centos    750  5월 13  2020 expression.tar.gz
-rw-------. 1 centos centos    717  5월 21  2020 expression.txt
-rw-rw-r--. 1 centos centos      0  5월 22  2020 findtestfile
-rwxr-xr-x. 1 centos centos 159024  5월 13  2020 grep-test
drwxrwxr-x. 2 centos centos     86  5월 21  2020 pattern
-r--r--r--. 1 centos centos    721  5월 19  2020 test.txt
```

<br><br>

## 1. awk의 사용법

`awk`는 크게 3가지 방법으로 사용할 수 있습니다.  
`기본 사용법`, `파일에서 불러온 패턴과 액션을 사용하는 방법`, `명령의 실행 결과를 대상으로 사용하는 방법`입니다.  
지난 글에서 알아본 `grep`이나 `find`와 비슷한 포맷입니다.
그럼 `awk`의 사용법에 대해 알아보겠습니다.

<br>

### 1.1 기본 사용법
**문법**
```shell
$ awk [옵션] '패턴 { 액션 }' 대상파일
```
**예제**
```shell
[centos@localhost ~]$ awk '$2 == 1 { print }' sample.txt
-rw-rw-r--. 1 centos centos     60  5월 21  2020 Separator.txt
-rw-rw----. 1 centos centos  65942  5월 15  2020 aa.txt
-rw-------. 1 centos centos     30  5월 19  2020 amin.txt
-rw-rw----. 1 centos centos  65942  5월 15  2020 bb.txt
-rw-rw-r--. 1 centos centos    750  5월 13  2020 expression.tar.gz
-rw-------. 1 centos centos    717  5월 21  2020 expression.txt
-rw-rw-r--. 1 centos centos      0  5월 22  2020 findtestfile
-rwxr-xr-x. 1 centos centos 159024  5월 13  2020 grep-test
-r--r--r--. 1 centos centos    721  5월 19  2020 test.txt
```
기본적인 사용법으로 패턴과 액션을 정의하고 대상 파일을 정의합니다.  
예시에서는 `$2 == 1`이라는 패턴과 `print`라는 액션을 사용했습니다.  
실행하면 위와 같이 2번째 필드의 값이 1인 레코드를 모두 출력합니다.

<br>

### 1.2 패턴과 액션을 정의한 파일을 사용하는 방법
**문법**
```shell
$ awk -f 패턴과_액션이_정의된_파일 대상파일
```

**예제**
```shell
[centos@localhost ~]$ cat patterns.txt 
$2 == 1 { print }
[centos@localhost ~]$ awk -f patterns.txt sample.txt 
-rw-rw-r--. 1 centos centos     60  5월 21  2020 Separator.txt
-rw-rw----. 1 centos centos  65942  5월 15  2020 aa.txt
-rw-------. 1 centos centos     30  5월 19  2020 amin.txt
-rw-rw----. 1 centos centos  65942  5월 15  2020 bb.txt
-rw-rw-r--. 1 centos centos    750  5월 13  2020 expression.tar.gz
-rw-------. 1 centos centos    717  5월 21  2020 expression.txt
-rw-rw-r--. 1 centos centos      0  5월 22  2020 findtestfile
-rwxr-xr-x. 1 centos centos 159024  5월 13  2020 grep-test
-r--r--r--. 1 centos centos    721  5월 19  2020 test.txt
```
자주 사용하거나 정의할 내용이 많은 경우 매번 입력하기 번거롭습니다.  
미리 파일에 패턴과 액션을 정의해서 사용한다면 편하겠죠?  
`-f 파일`은 파일에 정의된 패턴과 액션을 불러옵니다.  
예제에서는 `patterns.txt`파일에 정의해놓고 `-f`로 불러옵니다.  

### 1.3 파이프를 이용한 사용법
**문법**
```shell
$ 명령어 | awk [옵션] '패턴 { 액션 }'
```
**예제**
```shell
[centos@localhost ~]$ cat sample.txt | awk '$2 == 1 { print }'
-rw-rw-r--. 1 centos centos     60  5월 21  2020 Separator.txt
-rw-rw----. 1 centos centos  65942  5월 15  2020 aa.txt
-rw-------. 1 centos centos     30  5월 19  2020 amin.txt
-rw-rw----. 1 centos centos  65942  5월 15  2020 bb.txt
-rw-rw-r--. 1 centos centos    750  5월 13  2020 expression.tar.gz
-rw-------. 1 centos centos    717  5월 21  2020 expression.txt
-rw-rw-r--. 1 centos centos      0  5월 22  2020 findtestfile
-rwxr-xr-x. 1 centos centos 159024  5월 13  2020 grep-test
-r--r--r--. 1 centos centos    721  5월 19  2020 test.txt

```
마지막은 가장 많이 사용하는 방법으로 `다른 명령어의 실행 결과`를 awk로 처리하는 방법입니다.  
`cat`, `ls- al`같은 명령어 뒤에 파이프`|`와 `awk`를 입력하면 됩니다.
물론 `awk`도 실행 결과가 있으므로 다시 `awk`의 인자로 활용이 가능합니다.

<br><br>

## 2. 액션

액션은 패턴으로 추출한 레코드들을 출력하는 방법에 대해 정의하는 부분입니다.  
먼저 패턴을 정의한 다음에 중괄호에 기술합니다.  
액션은 조건문, 제어문, 입/출력문으로 구성되는데 모든 액션의 종류와 활용 방법을 모두 소개하기에는 분량이 많습니다.  
그래서 이번에는 기본적인 개념과 자주 사용하는 몇가지 실용적인 액션들에 대해 알아보겠습니다.  

<br>

### 2.1 awk내장 변수와 필드 리스트
본격적으로 액션을 알아보기 전에 알아야할 개념으로 `awk 내장 변수`와 `필드 리스트`가 있습니다.  
`awk 내장 변수`와 `필드 리스트`는 액션과 패턴에서 값을 비교하거나 출력할 때 사용합니다.  
`내장 변수`는 미리 정의된 상수라고 생각하면 됩니다.  
`FNR(대상 파일 레코드 번호)`, `NF(대상 파일 필드 개수)`, `NR(레코드 개수)` 등이 있으며 이 밖에도 다양한 내장 변수가 있습니다.  
`필드 리스트`는 특정한 필드의 값을 출력할 때 사용합니다.  
`달러 표시($)`와 `인덱스 번호`를 입력하면 해당하는 필드의 값을 출력합니다.  
예를 들어 `$6`이면 현재 처리하고있는 레코드에서 6번째 필드의 값을 출력하는 식이죠.
필드의 인덱스는 1번부터 시작합니다. 0번 인덱스는 현재 레코드 전체값을 출력하므로 헷갈리지 않게 주의할 필요가 있습니다.    

<br>

### 2.2 출력문

기본적인 출력 액션으로는 `print`와 `printf`가 있습니다.  
`print`는 일반적으로 출력하는 경우 사용합니다.  
눈치가 빠른 분은 아시겠지만 `printf`는 정의한 포맷에 맞게 출력하고 싶을 때 사용합니다.  
그럼 먼저 `print`부터 알아볼까요?

<br>

### 2.2.1 print
**문법**
```shell
'{ print 필드리스트 또는 문자열}'
# example
'{ print $1, $2, "hello" }'
```
**예제**
```shell
# print는 기본적으로 레코드 전체를 출력한다. print $0과 같다.
[centos@localhost ~]$ awk '$2 != 1 { print }' sample.txt 
drwxrwxr-x. 4 centos centos    198  5월 22  2020 .
drwxrwxr-x. 3 centos centos     59 10월 31 13:55 ..
drwxrwxr-x. 2 centos centos     87  5월 20  2020 File
drwxrwxr-x. 2 centos centos     86  5월 21  2020 pattern

# print $1, $2 ... 처럼 원하는 필드만 출력할 수 있다!
[centos@localhost ~]$ awk '$2 != 1 { print $1, $NF }' sample.txt 
drwxrwxr-x. .
drwxrwxr-x. ..
drwxrwxr-x. File
drwxrwxr-x. pattern
```
`print`는 위와 같이 레코드 전체 또는 특정 필드만을 출력하는게 가능합니다.  
콤마(,)로 구분해 여러개의 필드를 나열할 수 있으며 임의의 문자열도 추가할 수 있습니다.  

<br>

### 2.2.2 printf
**문법**
```shell
'{ printf "포맷 문자열", 인자1, 인자2...}'
```
**예제**
```shell
[centos@localhost ~]$ awk '$2 == 1 { printf "%+20s %s\n", $NF, $6 }' sample.txt 
       Separator.txt 5월
              aa.txt 5월
            amin.txt 5월
              bb.txt 5월
   expression.tar.gz 5월
      expression.txt 5월
        findtestfile 5월
           grep-test 5월
            test.txt 5월
[centos@localhost ~]$ awk '$2 == 1 { printf "%-20s %s\n", $NF, $6 }' sample.txt 
Separator.txt        5월
aa.txt               5월
amin.txt             5월
bb.txt               5월
expression.tar.gz    5월
expression.txt       5월
findtestfile         5월
grep-test            5월
test.txt             5월
```
`printf`는 특정한 포맷으로 출력하고자할 때 사용합니다.  
위 예제처럼 필드의 글자수(자리수)를 조정해서 크기를 늘리거나 정렬 방식을 변경할 수 있습니다.  
`"%-20s"`에서 `-`는 왼쪽 정렬을 의미합니다. 반대로 `+`는 오른쪽 정렬을 의미합니다.  
다음으로 오는 `20`은 필드가 차지하는 자리수를 의미하고 `s`는 문자로 인자를 받는것을 뜻합니다.  
C나 다른 언어의 `printf`와 비슷한 문법을 가지고 있습니다.  
`printf`의 문법 체계를 모두 소개하기엔 분량이 많으므로 생략하겠습니다.  

<br>

### 2.3 제어문
액션에서 사용하는 제어문의 종류는 `비교문`과 `반복문`이 있습니다.  
`if`, `switch`, `for`, `while` 등 여러 제어문이 있는데 이번에는 가장 많이 사용하는 `if`에 대해서 살펴보겠습니다.  

<br>

### 2.3.1 if
**문법**
```shell
'{ if (비교문) 실행문; else 실행문; 액션 }'
```
**예제**
```shell
[centos@localhost ~]$ awk '{ if ($2 == 1) $3="A"; else $3="B"; print }' sample.txt
drwxrwxr-x. 4 B centos 198 5월 22 2020 .
drwxrwxr-x. 3 B centos 59 10월 31 13:55 ..
drwxrwxr-x. 2 B centos 87 5월 20 2020 File
-rw-rw-r--. 1 A centos 60 5월 21 2020 Separator.txt
-rw-rw----. 1 A centos 65942 5월 15 2020 aa.txt
-rw-------. 1 A centos 30 5월 19 2020 amin.txt
-rw-rw----. 1 A centos 65942 5월 15 2020 bb.txt
-rw-rw-r--. 1 A centos 750 5월 13 2020 expression.tar.gz
-rw-------. 1 A centos 717 5월 21 2020 expression.txt
-rw-rw-r--. 1 A centos 0 5월 22 2020 findtestfile
-rwxr-xr-x. 1 A centos 159024 5월 13 2020 grep-test
drwxrwxr-x. 2 B centos 86 5월 21 2020 pattern
-r--r--r--. 1 A centos 721 5월 19 2020 test.txt
```
`if`는 값을 비교해서 처리를 다르게 하고 싶을 때 사용합니다.  
예제는 2번째 필드의 값이 1인경우 3번필드의 값을 A로 바꾸고 아닌 경우 B로 변경하는 내용입니다.  
논리연산자 `&&`와 `||`를 사용해 여러 조건을 동시에 비교하는것도 가능합니다.  

<br><br>

## 3. 패턴

패턴은 대상 파일에서 어떤 레코드를 출력할지 정의하는 부분입니다.  
보통은 필드의 내용과 특정한 값을 비교하거나 정규표현식 패턴과 일치하는지 판단하기 위해 사용합니다.  
그리고 awk 명령을 실행하기 전과 후에 특정한 동작을 하도록 할 때도 사용합니다.  
그럼 패턴을 어떻게 사용하는지 알아볼까요?  

<br>

### 3.1 BEGIN, END

**문법**
```shell
$ awk 'BEGIN {액션} {액션}'
$ awk 'END {액션} {액션}'
```
**예제**
```shell
[centos@localhost ~]$ ps -ef | awk 'BEGIN { print "# begin #" } END { print "# end #"} ($2 == 10) { print }'
# begin #
root         10      2  0 10월19 ?      00:00:00 [lru-add-drain]
# end #
```
BEGIN과 END는 각각 awk를 실행하기 전과 후에 특정한 동작을 수행하려는 경우 사용합니다.  
위 예제처럼 비교문 패턴과 함께 사용하는것도 가능합니다.

<br>

### 3.2 정규표현식, 관계식, 삼항연산자 패턴
**문법**
```shell
'비교 패턴 { 액션 }'
```
**예제**
```shell
# 정규표현식 예
[centos@localhost ~]$ cat sample.txt | awk '/[[:lower:]]*.txt/ { print }'
-rw-rw-r--. 1 centos centos     60  5월 21  2020 Separator.txt
-rw-rw----. 1 centos centos  65942  5월 15  2020 aa.txt
-rw-------. 1 centos centos     30  5월 19  2020 amin.txt
-rw-rw----. 1 centos centos  65942  5월 15  2020 bb.txt
-rw-------. 1 centos centos    717  5월 21  2020 expression.txt
-r--r--r--. 1 centos centos    721  5월 19  2020 test.txt
# 관계식 예
[centos@localhost ~]$ ps -ef | awk '($1 == "root") && ($2 == 6) { print $0}' 
root          6      2  0 10월19 ?      00:00:09 [ksoftirqd/0]
# 삼항연산자 예 
[centos@localhost ~]$ cat sample.txt | awk '$2 == 2 ? res="Directory" : res="File" { print $1, res }'
drwxrwxr-x. File
drwxrwxr-x. File
drwxrwxr-x. Directory
-rw-rw-r--. File
-rw-rw----. File
-rw-------. File
-rw-rw----. File
-rw-rw-r--. File
-rw-------. File
-rw-rw-r--. File
-rwxr-xr-x. File
drwxrwxr-x. Directory
-r--r--r--. File
```
많이 사용하는 비교 패턴으로는 위 예제에서 사용한 `정규표현식`, `관계식`, `삼항연산자`가 있습니다.  
`정규표현식`과 `관계식`의 논리연산은 익숙한 방식이니 넘어가겠습니다.  
`삼항연산자`에서 변수를 정의하고 값을 할당하는 구문이 보이시나요?  
여기서 정의한 변수는 뒤에 나오는 액션에서 활용할 수 있습니다!  
물론 앞서 배운 `if`를 사용해도서 처리하는것도 가능하니 상황에 맞게 사용하면 되겠습니다.

<br><br>

## 마무리
이번 시간에는 `awk`의 기초적인 사용법에 대해 알아봤습니다.  
그리고 텍스트의 성격에 따라서 `grep`과 `awk` 둘중 어떤것을 활용해야 하는지도 살펴봤습니다.  
`awk`는 본문에서 소개드리지 못한 다양한 활용방법이 있습니다.  
자세한 정보는 아래 링크를 참고해 주시기 바랍니다.  

https://man7.org/linux/man-pages/man1/awk.1p.html