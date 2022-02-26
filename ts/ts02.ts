import * as fs from 'fs';

// AtCoder Beginner Contest 240 B - Count Distinct Integers

const arg = fs.readFileSync('/dev/stdin', 'utf-8');

export const Main = (input: string): void => {
  const array: string[] = input.trim().split('\n');
  const numberData = array[1].split(' ').map((x: string): number => +x);
  
  const uniqueData = new Set(numberData);
  console.log(uniqueData.size);
}

Main(arg);
