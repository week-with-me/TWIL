class Student {
  constructor(name, studentId, age) {
    this.name = name;
    this.studentId = studentId;
    this.age = age;
  }

  getInfo() {
    return `Name: ${this.name} Student ID: ${this.studentId} Age: ${this.age}`;
  }

  static staticMethod() {
    return `This is static method. Name: ${this.name}`;
  }
}

console.log(Student.staticMethod());

const student = new Student("James");
console.log(student.getInfo());

console.log(Student);
