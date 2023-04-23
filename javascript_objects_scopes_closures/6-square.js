#!/usr/bin/node
const Square = require('./5-square');

class Square2 extends Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let row = '';
    for (let i = 0; i < this.height; i++) {
      if (i === this.height - 1) {
        row += c.repeat(this.width);
      } else {
        row += c.repeat(this.width) + '\n';
      }
    }
    console.log(row);
  }
}

module.exports = Square2;
