class Dinglemouse {
  constructor() {
    this.name = this.age = this.sex = 0
    this._propertiesSetted = new Map();
  }

  setAge(age) {
    this.age = age
    this._propertiesSetted.set("age", `I am ${age}.`);
    return this
  }

  setSex(sex) {
    this.sex = sex
    this._propertiesSetted.set("sex", `I am ${sex == 'M' ? "male" : "female"}.`);
    return this
  }

  setName(name) {
    this.name = name
    this._propertiesSetted.set("name", `My name is ${name}.`);
    return this
  }

  hello() {
    const attributtesFormatted = [...this._propertiesSetted.values()].join(" ");
    return attributtesFormatted.length > 0 ?
      `Hello. ${attributtesFormatted}`:
      "Hello.";
  }
}
