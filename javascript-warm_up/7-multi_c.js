#!/usr/bin/node
const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let message = '';
  for (let i = 0; i < num; i++) {
    message += 'C is fun\n';
  }
  console.log(message.trim());
}
