import * as fs from 'fs';

// AtCoder Beginner Contest 240 A - Edge Checker

const arg = fs.readFileSync('/dev/stdin', 'utf-8');

export const Main = (input: string): void => {
  const array: string[] = input.trim().split('\n');
  const [n, m] = array[0].split(" ").map((x: string): number => +x);

  let answer = 'No';
  if ((n === 1 && m === 10) || (n === 10 && m === 1)) answer = 'Yes';
  if ((n - m === 1) || (m - n === 1)) answer = 'Yes';

  console.log(answer);
};

Main(arg);
