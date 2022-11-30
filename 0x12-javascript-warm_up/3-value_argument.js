#!/usr/bin/node
// A script that prints the first argument passed to it
const args = process.argv;
if (args.length === 2) {
  console.log('No argument');
    }
if (args.length > 2) {
    console.log(args[2]);
    }
