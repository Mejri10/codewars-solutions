class Dictionary {
  constructor() {
    this._dict = {};
  }
  
  newEntry(key, value) {
    this._dict[key] = value;
  }
  
  look(key) {
    if (this._dict[key] !== undefined) {
      return this._dict[key];
    } else {
      return `Can't find entry for ${key}`;
    }
  }
}