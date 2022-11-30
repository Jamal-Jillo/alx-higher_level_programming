#!/usr/bin/node
// A script that prints the addition of 2 integers
// using a function prototype: function add(a, b)
function add (a, b) {
  return a + b;
}
const args = process.argv;
if (args.length === 2) {
    console.log('NaN');
        }
if (args.length === 3) {
    console.log('NaN');
        }
if (args.length > 3) {
    console.log(add(parseInt(args[2]), parseInt(args[3])));
        }

