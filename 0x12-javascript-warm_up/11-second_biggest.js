#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments
const args = process.argv;
if (args.length === 2) {
    console.log('0');
        }
if (args.length === 3) {
    console.log('0');
        }
if (args.length > 3) {
    const arr = [];
    for (let i = 2; i < args.length; i++) {
        arr.push(parseInt(args[i]));
            }
    arr.sort(function (a, b) { return a - b; });
    console.log(arr[arr.length - 2]);
        }
