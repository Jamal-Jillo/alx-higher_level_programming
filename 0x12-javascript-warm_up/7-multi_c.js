#!/usr/bin/node
// A script that prints a square
const args = process.argv;
if (args.length === 2) {
    console.log('Missing size');
        }
if (args.length > 2) {
    for (let i = 0; i < parseInt(args[2]); i++) {
        console.log('X'.repeat(parseInt(args[2])));
            }
        }
