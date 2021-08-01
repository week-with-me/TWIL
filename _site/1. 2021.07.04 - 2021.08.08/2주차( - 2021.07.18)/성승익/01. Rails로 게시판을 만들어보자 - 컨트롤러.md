# Rails로 간단한 게시판을 만들어보자

## 1. Rails에서 웹개발 시작하기

* Model - 비즈니스 로직을 처리.
* View - 처리한 내용을 보기좋게 만듦.
* Controller - 요청을 받아서 담당자에게 전달.

Rails는 기본적으로 MVC 패턴에 맞게 개발하도록 되어있다.  
그래서 MVC를 편리하게 개발할 수 있게 도와주는 명령어들을 제공하며, 컨벤션을 통해 코드를 압축할 수 있다.  
컨벤션을 통한 암묵적인(implicit) 로직들이 많아서, 웹 애플리케이션 아키텍처에 대해 잘 모르는 경우  혼란스러울 수 있다는 문제도 존재한다.  
하지만 기초 지식이 있다면 Rails 덕분에 코드가 얼마나 간결해지는지 충분히 느낄 수 있다.  

<br></br>

## 2. Rails 프로젝트 만들기

* Ruby
* SQLite3
* Node.js

Rails 프로젝트를 시작하기 위해서는 위와 같은 준비물이 필요하다.  
Ruby는 Linux와 MacOS 아키텍처를 기준으로 만들어졌기 때문에 해당 OS에서 개발하는것이 편하다.  
물론 Windows에서도 Ruby Installer 또는 WSL(Windows Subsystem for Linux)을 사용해서 개발을 할 수 있지만, 실행환경 관리가 복잡해서 이 글에서는 다루지 않는다.  
오늘 날짜인 2021.07.16 기준으로 현재 최신 Ruby는 3.0.2버전, Rails는 6.1.4 버전이다.  
나는 실무에서 사용중인 버전에 대해 학습하기 위해 낮은 버전의 Ruby와 Rails를 설치했는데, Ruby를 설치하는 과정에서 의존성 문제로 고생을 많이했다.  
Linux와 MacOS의 버전이 업데이트 되면서 기존 openssl(기존 1.0에서 현재는 1.1을 사용한다), libssl등의 라이브러리도 같이 업데이트 되었기 때문에 이전 버전에 의존하는 낮은 버전의 Ruby는 오류가 많이 발생한다고 한다.  
때문에 특별한 이유가 없다면 최신버전을 설치하는것이 가장 쉽다.

``` sh
# 준비물이 설치되었나 버전 확인하기 (설치 버전에 따라 내용이 다를 수 있음)
$ ruby --version
ruby 2.2.5
$ sqlite3 --version
3.32.3
$ node --version
v12.22.1

# rails install
$ gem install rails
$ rails --version
Rails 4.1.12

# example 이라는 이름의 Rails 프로젝트 만들기 - 현재 디렉토리 기준 example이라는 디렉토리가 생긴다.
$ rails new example
```

`rails new example`이라는 명령어를 입력하면 아래와 같은 구조의 프로젝트가 생성된다.  

![Rails 프로젝트 구조](./images/week02-01-project.png)  


<br></br>

## 3. 컨트롤러 생성하기
``` sh
# 컨트롤러 생성하기
$ rails g controller [이름] [액션]  
# 컨트롤러 제거하기
$ rails d controller [이름]
```
기본적인 설정이 끝났다고 가정했을 때, 다음으로 하게되는 작업은 클라이언트의 요청을 받기 위한 컨트롤러를 만드는 일이다.  
Rails는 위 명령어를 통해 쉽게 컨트롤러를 생성하고 제거할 수 있다.  
참고로 g, d는 각각 generate, destroy 의 약자이다.  
액션은 컨트롤러 클래스 내부에 정의되는 메서드를 의미한다.  
일반적으로 액션의 내부에는 모델을 통해 비즈니스 로직을 수행하거나 뷰를 반환하는 코드를 작성한다.  
다음은 Rails의 명령어와 컨벤션대로 컨트롤러를 생성하는 방법이다.

<br></br>

### 3.1 Posts 컨트롤러 생성

다음 명령어를 입력하면 게시판의 글들을 담당할 Postx컨트롤러와 여러 파일들이 생성된다.  
여기서 눈여겨 볼 것은 컨트롤러의 이름을 복수형(plural)으로 지정했다는 점이다.  
Rails에서는 컨벤션에 따라 컨트롤러 이름을 복수형으로 지정해야한다.  
뒤에 나올 resources를 통한 RESTful API 경로생성과 관련된 부분이라 지키는것이 좋다.  
```sh
$ rails g controller Posts index
      create  app/controllers/posts_controller.rb
      invoke  erb
      create    app/views/posts
      invoke  test_unit
      create    test/controllers/posts_controller_test.rb
      invoke  helper
      create    app/helpers/posts_helper.rb
      invoke    test_unit
      create      test/helpers/posts_helper_test.rb
      invoke  assets
      invoke    coffee
      create      app/assets/javascripts/posts.js.coffee
      invoke    scss
      create      app/assets/stylesheets/posts.css.scss
```
```ruby
# post_controller.rb
class PostsController < ApplicationController
    def index
    end
end

```

<br></br>

### 3.2 routes.rb 파일 작성하기
다음으로 할 일은 요청을 어느 컨트롤러에 전달할 것인지 라우팅하는 작업이다.  
`config` 디렉토리에 있는 `routes.rb`는 요청에 관한 경로를 정의하는 파일이다.  
`routes.rb`는 아래의 코드처럼 작성한다.  
주석된 부분의 get처럼 별도의 경로를 지정하는것도 가능하지만, 대부분의 경우 resources 를 통해 자동 생성되는 경로를 따른다.  
그 이유는 `resources`에게 생성을 맡기면 RESTful path와 Prefix를 자동생성 해주기 떄문이다.  
Prefix는 Url을 대신 사용할 수 있는 이름으로 컨트롤러, 뷰에서 자주 사용된다.  
Url을 의미있는 이름으로 대체 가독성이 좋은 코드를 만들 수 있게 해준다.  
물론 `as` 키워드를 통해 별도로 Prefix 를 지정하는것도 가능하지만, 일일히 지정하는것은 꽤 피곤한 작업이다.  
`routes.rb`파일에 내용을 입력한 다음 터미널에 `rake routes` 라고 입력하면 Rails가 생성해준 경로들과 Prefix를 확인할 수 있다.  
RESTful 경로를 생성해주므로 Rails 컨벤션을 따르는 것만으로도 REST API를 개발하게 된다.  


```ruby
# routes.rb
Rails.application.routes.draw do
  root "posts#index"
  # get "/posts", to: "posts#index"
  resources :posts do
  end
end

```
```sh
iksflow@iksflow example % rake routes
   Prefix Verb   URI Pattern               Controller#Action
     root GET    /                         posts#index
    posts GET    /posts(.:format)          posts#index
          POST   /posts(.:format)          posts#create
 new_post GET    /posts/new(.:format)      posts#new
edit_post GET    /posts/:id/edit(.:format) posts#edit
     post GET    /posts/:id(.:format)      posts#show
          PATCH  /posts/:id(.:format)      posts#update
          PUT    /posts/:id(.:format)      posts#update
          DELETE /posts/:id(.:format)      posts#destroy
```

<br></br>

### 3.3 View 파일 작성하기
컨트롤러는 요청을 받으면 모델에 전달을 하고, 모델에서는 해아할 작업을 마치면 컨트롤러에게 알려준다.  
그 다음 처리된 내용을 템플릿엔진을 통해 예쁘게 만들어 보여줄지(html), 아니면 데이터만 보내줄지(xml, json...etc) 둘 다 아니라면 사용자가 다른 업무를 처리할 수 있도록 다른 페이지로 이동시킬지 등등 어떤 결과를 보내줄지 정해야한다.  
Rails는 컨트롤러의 액션에 반환할 포맷을 정해두지 않으면 기본적으로  `/views/{컨트롤러이름}`의 경로에서 액션이름의 파일(.html.erb)을 찾아서 반환한다.  
Posts 컨트롤러의 index 액션에는 별다른 내용이 없으므로 `/views/posts/index.html.erb`라는 파일을 반환하게 된다.  
현재는 파일이 없으므로 요청을 보내면 아래의 `Template is missing`이라는 오류를 만나게된다.  

![오류](./images/week02-02-error.png)  

`/views/posts`경로에 아래의 코드를 따라서 간단한 `index.html.erb`라는 파일을 만든 다음 `localhost:3000`으로 접속하면 아래의 화면을 확인할 수 있다.  (Rails는 기본값으로 3000번 포트를 사용한다)  
```html
<!-- /views/posts/index.html.erb -->

<h1>Hello, Rails!</h1>
```
![index페이지](./images/week02-03-index.png)


<br></br>

## 4. 마치며
Rails프로젝트를 생성하고 간단한 컨트롤러의 생성과 요청경로를 지정하는 방법에 대해서 알아보았다.  
MVC패턴으로 웹 애플리케이션을 개발해본 경험 덕분에 내용을 이해하기 쉬웠다.  
사실 MVC패턴을 따르는 이상 내용 자체는 어떤 프레임워크마다 큰 차이는 없다고 생각한다.  
하지만 기존의 Spring에서의 개발 경험과 비교했을 때, Rails에서는 `resources`와 `rake routes`를 통해 개발이 더 편해지겠다는 생각이 몇가지 들었다.  

첫번쨰는 url 오타로 인한 오류이다.  
Spring에서 하드코딩해서 작성하는 url의 경우 오타로 인해 경로가 잘못 생성될 위험이 있지만, Rails 에서는 resources를 적극 활용해서 이 부분에 대한 위험을 최소화할 수 있다.  
또한 RESTful한 경로를 자동으로 생성해주기 때문에 Rails의 컨벤션에 익숙해진다면 행위가 명확하고 가독성도 좋은 코드가 될 것이라는 생각이 들었다.  

두번째는 rake routes를 통해 유효한 경로를 쉽게 확인할 수 있는 점이다.  
Spring에서는 애노테이션에 직접 경로를 입력하는 방식이라서 일일히 다 찾아서 확인해야했다.(plugin이 있는지는 모르겠다.)  
하지만 Rails 에서는 `rake routes`를 통해 현재 애플리케이션에서 유효한 요청경로를 한눈에 확인할 수 있다. 그리고 자동생성해주는 Prefix를 통해 긴 Url보다 가독성이 좋고 의미가 명확한 Prefix로 대체할 수 있다.  

마지막으로 아래는 Spring과 Rails에서 각각 Posts컨트롤러를 만드는 상황을 가정해 작성한 코드이다.  
Spring에서는 컨트롤러를 구현하기 위해 많은 코드가 필요하다.  
물론 처음에 JSP/Servlet환경에서 개발하다가 Spring을 접했을 때는 Spring 코드를 보고 엄청 짧고 간결하다고 느꼈던 기억이 난다.  
그런데 Rails코드는 `routes.rb`와 컨벤션 덕분에 훨씬 단순하다.  
개발자가 작성해야할 코드가 훨씬 적다는 것은 당연하게도 생산성과 직결되는 부분이다.  


* Spring Boot의 컨트롤러
    ```Java
    // import blah ...

    @Controller
    public class PostsController {

        @RequestMapping("/posts")
        public String index() {
            return "/posts/index"
        }
    }
    ```
* Rails의 컨트롤러
    ```ruby
    class PostsController < ApplicationController
        def index
        end
    end
    ```


고작 컨트롤러 부분을 살펴보았음에도 많은 부분을 느끼고 배울 수 있었다.  
다음은 모델에 대해서 다룰 예정이다.  



## References
* Ruby on Rails 공식 문서
    * https://guides.rubyonrails.org/  
* Windows 10 에서 Ruby 설치하기
    * https://phoenixnap.com/kb/install-ruby-on-windows-10