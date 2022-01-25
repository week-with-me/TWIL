function Student(name, studentId, age) {
  this.name = name;
  this.studentId = studentId;
  this.age = age;
}

Student.prototype.getInfo = function () {
  return (
    "Name: " +
    this.name +
    " Student ID: " +
    this.studentId +
    " Age: " +
    this.age
  );
};

var student = new Student("James");
console.log(student.getInfo());

console.log(Student);
