#!/usr/bin/node
// A script that computes and prints a factorial
// using a function prototype: function factorial(a)
function factorial (a) {
  if (a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}
const args = process.argv;
if (args.length === 2) {
  console.log('1');
}
if (args.length === 3) {
    console.log(factorial(parseInt(args[2])));
    }
