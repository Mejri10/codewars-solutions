class Person {

  constructor(name) {
    this.name = name;
  }
  
  greet(person_name) {
    return `Hello ${person_name}, my name is ${this.name}`
  }

}
