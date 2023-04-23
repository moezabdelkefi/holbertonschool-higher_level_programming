#!/usr/bin/node
class Rectangle {
    constructor() {

    }

toString() {
    return `[Class: Rectangle]`;
  }
}

const rect = new Rectangle();
console.log(rect); // output: Rectangle {}
console.log(rect.toString());
