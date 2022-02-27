import * as fs from 'fs';

// HHKB プログラミングコンテスト 2022（AtCoder Beginner Contest 235） B - Climbing Takahashi

const arg = fs.readFileSync('/dev/stdin', 'utf-8');

export const Main = (input: string): void => {
  const array: string[] = input.trim().split('\n');
  const [n] = array[0].split(' ').map((x: string): number => +x);
  const t = array[1].split(' ').map((y: string): number => +y);

  let currentPosition = t[0];
  for (let i = 1; i < t.length; i++) {
    if (currentPosition < t[i]) {
      currentPosition = t[i];
    } else {
      break;
    }
  }

  console.log(currentPosition);
};

Main(arg);
