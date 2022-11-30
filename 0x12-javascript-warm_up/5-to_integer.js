#!/usr/bin/node
// A script that prints "My number: <first argument converted in integer>" if the first argument can be converted to an integer
const args = process.argv;
if (args.length === 2) {
    console.log('Not a number');
        }
if (args.length > 2) {
    console.log('My number: ' + parseInt(args[2]));
        }
