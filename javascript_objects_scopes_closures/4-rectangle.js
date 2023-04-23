#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || !Number.isInteger(w) || h <= 0 || !Number.isInteger(h)) {
      return this;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let row = '';
    for (let i = 0; i < this.height; i++) {
      row += 'X'.repeat(this.width);
      if (i < this.height - 1) {
        row += '\n';
      }
    }
    console.log(row);
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
