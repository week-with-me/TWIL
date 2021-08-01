# Rails로 간단한 게시판을 만들어보자 - 모델 2편

컨트롤러에서 CRUD 로직을 구현하는 방법은 아래와 같다.  
CRUD를 위해 필요한 로직은 크게 2가지가 있다.  
하나는 값을 입력받기 위한 페이지를 반환하는 메서드(액션)이고 다른 하나는 실제로 DB의 로직을 처리하는 메서드이다.  
CRUD로직에 해당하는 이름은 보통 `index, read, new, create, edit, update, destory`의 명칭을 사용한다.  
물론 개별적으로 이름을 지정하는것도 가능하지만, Scaffolding으로 생성하는 경우 위의 명칭으로 자동 생성되므로 Rails의 컨벤션을 활용하기 위해서는 위의 네이밍을 따르는 것이 좋다.  
`new, edit`의 경우 데이터 등록, 수정 시 값을 입력하기 위한 페이지를 반환한다.  
`index, read, create, update, destroy`의 경우 DB와 관한 처리를 담당한다.

<br></br>


## 1. CRUD 만들기
``` ruby
class PostsController < ApplicationController
    # Read all
    def index
        @post = Post.all
    end
    # Read single row
    def show
        @post = Post.find(params[:id])
    end
    # Return Add post page
    def new
        @post = Post.new
    end
    # Create a row
    def create
        @post = Post.new(post_params)
        @post.save
    end
    # Return Edit post page
    def edit
        @post = Post.find(params[:id])
    end
    # Update a row
    def update
        @post = Post.find(params[:id])
        if @post.update(post_params)
            redirect_to "/posts"
        else
            render "edit"
        end
    end
    # Delete a row
    def destroy
        @post = Post.find(params[:id])
        @post.destroy
        redirect_to "/posts"
    end

    # Strong parameter
    private
    def post_params
        params.require(:post).permit(:title)
    end
end
```

CRUD로직의 기본적인 코드는 위와 같다.  

<br></br>


### 1.1 CREATE
``` ruby
    # Create a row
    def create
        @post = Post.new(post_params)
        @post.save
    end
```
Post 객체를 생성하고 매핑되는 테이블에 데이터를 저장하는 로직이다.  
`Post.new`코드는 객체를 새로 생성하며 id, timestamp 컬럼에 해당하는 값을 자동으로 초기화한다.  
그리고 뷰에서 입력받은 값들이 저장된 `post_params`를 객체에 매핑한다.  
`post_params`는 맨 아래에 정의된 메서드로 스트롱 파라미터라는 기능이다.  
`require`와 `permit`을 통해 의도하는 값만을 받게 하는 역할을 담당한다.  
덕분에 클라이언트가 악의적으로 파라미터를 변조해 넘기는 경우를 방지할 수 있고, 만약 허용된 파라미터 외의 값이 전달되는 경우 오류를 발생시킨다.  

<br></br>

### 1.2 READ
```ruby
    # Read all
    def index
        @post = Post.all
    end

    # Read single row
    def show
        @post = Post.find(params[:id])
    end
```
조회의 경우 보통 2가지 기능을 구현하게 된다.  
게시판을 예로 들면 게시글 목록(List)과 게시글 내용에 해당한다.  
먼저 데이터 전체를 조회해서 목록을 만들고 싶은 경우 `Post.all` 을 사용해 전체 데이터를 받아올 수 있다.  
일부 특정한 데이터를 선택하는 경우 `Post.find(id)`를 통해 `id`값을 기준으로 단건의 데이터를 가져올 수 있다.

<br></br>


### 1.3 UPDATE
``` ruby
    # Update a row
    def update
        @post = Post.find(params[:id])
        if @post.update(post_params)
            redirect_to "/posts"
        else
            render "edit"
        end
    end
```
수정은 조회때와 마찬가지로 `Post.find(id)`를 통해 수정할 대상을 찾는다.  
그 다음 `@post.update(post_params)`로 뷰에서 넘겨 받은 값들로 수정을 한다.  
`@post.update`의 반환값은 `boolean`형태인데 정상적으로 update가 수행되면 `true` 오류가 생기는 경우 `false`를 반환한다.  
로직도 이에 맞게 정상적으로 수정이 완료되는 경우 목록 페이지인 `/posts`로 리다이렉트한다.  
실패하는 경우 수정 페이지인 `edit`을 반환해서 다시 수정작업을 할 수 있게 하는 로직이다.  

<br></br>



### 1.4 DELETE
``` ruby
    # Delete a row
    def destroy
        @post = Post.find(params[:id])
        @post.destroy
        redirect_to "/posts"
    end
```
`Post.find(id)`로 삭제할 대상을 찾은 다음 `@post.destroy`로 대상을 삭제한다.  
삭제가 완료되면 `/posts` 페이지로 리다이렉트한다.  

<br></br>

## 마무리
간단하게 CRUD 로직을 구현하는 방법에 대해서 알아보았다.  
다음에는 실제로 View와 연동해 값이 어떻게 이동하고 입력받는지 살펴볼 계획이다.

<br></br>

## Reference
https://guides.rubyonrails.org/v4.1/getting_started.html