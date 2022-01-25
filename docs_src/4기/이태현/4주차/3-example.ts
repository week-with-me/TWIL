class Student {
  static staticMethod(): string {
    return `This is static method. Name: ${this.name}`;
  }

  public name: string;
  private studnetId: string;
  public age: number;

  constructor(name: string, studentId: string, age?: number) {
    this.name = name;
    this.studnetId = studentId;
    this.age = age;
  }

  getInfo() {
    return `Name: ${this.name} Student ID: ${this.studnetId}, Age: ${this.age}`;
  }
}

console.log(Student.staticMethod());

const student = new Student("James", "ABCD1234");
console.log(student.getInfo());

export {};
