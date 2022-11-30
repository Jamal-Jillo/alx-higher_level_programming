#!/usr/bin/node
// A script that prints 2 arguments passed to it, in the following format: " is "
const args = process.argv;
if (args.length === 2) {
  console.log('No argument');
    }
if (args.length === 3) {
    console.log(args[2] + ' is ' + args[3]);
    }
if (args.length > 3) {
    console.log(args[2] + ' is ' + args[3]);
    }
