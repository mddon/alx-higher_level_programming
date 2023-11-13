#!/usr/bin/node

const len= Math.floor(Number(process.argv[2]));

if (isNaN(len)) {
  console.log('Missing size');
} else {
  for (let h = 0; h < len; h++) {
    let row = '';
    for (let w = 0; w < len; w++) row += 'X';
    console.log(row);
  }
}
