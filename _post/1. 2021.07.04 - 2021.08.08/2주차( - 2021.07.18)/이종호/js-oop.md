## class
-  여타 OOP 언어처럼 클래스를 통해 instance를 만들 수 있는 자료형

### static
- 속성이나 메서드를 클래스에 종속되게 사용한다.
- instance를 통해서는 접근할 수 없다.
```ts
class TestObject {
  private static COUNT: number = 7;
  constructor() {}
}
console.log(TestObject.COUNT) // 7

const test = new TestObject();
console.log(test.COUNT) // X
```
## 접근제어자
### private
- 클래스 내부에서만 해당 값이나 메소드를 호출하거나 사용가능하다.
- 보통 getter와 setter를 통해 값을 조작하거나 가져온다.

### protected
- 클래스 내부이거나, 해당 클래스를 상속받은 **클래스**에서만 접근이 가능하다.

### public
- 클래스에 의해 구현된 인스턴스가 해당 속성이나 메서드를 접근할 수 있다.
- 수정도 가능하다.


```ts
  class User {
    get fullName(): string {
      return `${this.firstName} ${this.lastName}`
    }
    
    private internalAge = 4;
    get age(): number {
      return this.internalAge;
    }
    set age(num:number) {
      if(num < 0) {
        throw new Error('age must be greater then 0!')
      }
      this.internalAge = num;
    }

    constructor(private firstName: string, private lastName: string) {}

    /**
     * setter나 getter는 일반 변수처럼 사용 가능하다.
     */
  }

  const user = new User('Steve', 'Job');
  console.log(user.fullName);
  user.age = 6;
  console.log(user.age);
  ```