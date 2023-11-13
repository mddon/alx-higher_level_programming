#!/usr/bin/node
const len= Math.floor(Number(process.argv[2]));
if (isNaN(length)) {
  console.log('Missing size');
} else {
  for (let h = 0; h < length; h++) {
    let row = '';
    for (let w = 0; w < length; w++) row += 'X';
    console.log(row);
  }
}
