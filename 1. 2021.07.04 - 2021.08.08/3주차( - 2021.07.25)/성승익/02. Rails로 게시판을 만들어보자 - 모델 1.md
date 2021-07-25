# Rails로 간단한 게시판을 만들어보자 - 모델 1편

## 1. Rails의 모델은 어떤 역할을 하는가?
모델은 비즈니스로직과 이를 수행하는데 필요한 여러가지 로직들이 정의되는 공간이다.  
대표적으로 DB에서 데이터를 읽고 쓰는것이 있다.  
이밖에도 데이터의 유효성검사, 모델간의 관계 설정 등을 담당한다.  

<br></br>


## 2. ORM 그리고 ActiveRecord
`ORM`은 객체와 관계형 데이터베이스의 데이터를 매핑해주는 기술을 말한다.  
`ActiveRecord`는 Rails에서 ORM을 구현하기 위해 사용되는 구현체이다.  Java의 `JPA`와 `Hibernate`의 관계와 같다.  
ORM과 관련된 자세한 내용은 검색해보면 많이 나오는 관계로 생략하겠다.  

<br></br>


## 3. 모델을 생성하는 방법
```sh
# rails g model modelName [field:type ...]
$ rails g model Post title:string body:text
```
위 명령은 Post 모델에 필요한 파일들을 생성한다.
한번에 필드를 나열해서 정의할 수도 있고, 생략한 다음 나중에 정의해도 된다.
명령을 실행하기 전에 눈여겨 볼 점은 지난번과 마찬가지로 이름의 형태이다.  
앞서 살펴본 컨트롤러의 경우는 `복수형(plural)`을 사용하는 것이 컨벤션이었다면, 모델의 경우는 `단수형(singular)`을 사용해야한다.  
그 이유는 바로 Rails가 모델에 매핑되는 `테이블 이름`을 `모델 이름의 복수형`으로 자동 생성하기 때문이다.  
명령어를 실행하면 다음과 같은 결과를 볼 수 있다.

```sh
iksflow@iksflow example % rails g model Post title:string body:text
Running via Spring preloader in process 44409
      invoke  active_record
      create    db/migrate/20210723132121_create_posts.rb
      create    app/models/post.rb
      invoke    test_unit
      create      test/models/post_test.rb
      create      test/fixtures/posts.yml
```
총 4개의 파일이 생성되었다는 메시지를 확인할 수 있는데, 기능 구현에 필요한 파일은 `모델 파일(post.rb)`과 `마이그레이션 파일(20210723132121_create_posts.rb)`이다.  

<br></br>


### 3.1 모델 파일
```rb
class Post < ActiveRecord::Base
end
```
명령어를 실행해서 생성한 post.rb의 코드이다.  
코드에는 필드에 관한 내용이 아무것도 없지만, 실행되는 시점에는 `ActiveRecord`가 매핑을 해준다.  
그래서 `Post.title`처럼 값을 불러오는 것이 가능하다.
나중에는 모델간의 관계, 유효성 검사로직, 비즈니스 로직 등의 내용을 작성할 떄 사용된다.
구체적인 사용법은 나중에 CRUD 관련된 내용을 설명할 때 다룰 생각이다.  

<br></br>


### 3.2 마이그레이션 파일
```rb
class CreatePosts < ActiveRecord::Migration
  def change
    create_table :posts do |t|
      t.string :title
      t.text :body
      t.timestamps
    end
  end
end
```
`20210723132121_create_posts.rb`이라는 이름의 `마이그레이션 파일`의 코드이다.  
`마이그레이션 파일`에는 테이블을 생성하기 위해 필요한 내용들이 정의되어 있다.  
테이블
다소 난잡한 이름을 가진 파일인데, 눈썰미가 있는 사람이라면 파일명에 타임스탬프가 포함되었다는 것을 눈치챘을 것이다.  
그 이유는 마이그레이션 파일이 순서대로 처리되도록 하기위함이다.  
예를 들어, A테이블과 A의 서브테이블인 B가 있다고 가정해보자.  
만약 `20210723_A.rb` 라는 마이그레이션 파일과 `20210724_B.rb`라는 파일이 있다면 마이그레이션을 수행할 때 오류가 발생하지 않는다.  
A테이블을 먼저 생성하고 B를 생성하는건 자연스럽기 때문이다.  
그러나 `20210723_B.rb`와 `20210724_A.rb`와 같은 순서로 파일을 생성했다면 오류가 발생하게 된다.  
`20210723_B.rb`파일을 실행하는 시점에는 의존할 테이블인 A를 찾을 수 없기 때문이다.  
간단히  위해서 `change` 라는 메서드의 내용

<br></br>


## 4. DB에 반영하기
```sh
iksflow@iksflow example % rake db:migrate
== 20210723132121 CreatePosts: migrating ======================================
-- create_table(:posts)
   -> 0.0014s
== 20210723132121 CreatePosts: migrated (0.0015s) =============================
```
모델과 마이그레이션 파일을 생성했다고 해서 DB에 테이블이 생기는것은 아니다.  
DB에 앞서 진행한 내용들을 적용하기 위해서는 `rake db:migrate` 명령어를 실행해야한다.  
위의 내용은 `rake db:migrate`를 실행했을 때의 결과내용이다.  
`posts` 라는 복수형 이름의 테이블이 생성되었다는 사실을 알 수 있다.  

```rb
# schema.rb
ActiveRecord::Schema.define(version: 20210723132121) do
  create_table “posts”, force: true do |t|
    t.string   “title”
    t.text     “body”
    t.datetime “created_at”
    t.datetime “updated_at”
  end
end
```

`rake db:migrate` 명령을 실행하면 위와 같은 내용의 `schema.rb`파일이 생성된다.  
실제로 DB에 관한 내용을 처리할 때는 schema.rb의 내용을 기반으로 작업을 수행하게 된다.  
간혹 마이그레이션 파일의 내용을 수정하고 `rake db:migrate` 명령을 실행했음에도 테이블에 변화가 없는 경우가 있었다.  
이런 경우 `schema.rb` 파일에 수정한 내용이 반영되어있지 않았을 가능성이 크다.  
`rake db:migrate:reset` 명령어를 실행하면 `schema.rb`를 다시 생성하므로 문제를 해결할 수 있다.

<br></br>


## Reference
https://guides.rubyonrails.org/v4.1/getting_started.html