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