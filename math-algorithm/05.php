<?php

// 素数判定

$stdin = trim(fgets(STDIN));
$bcsqrt = bcsqrt($stdin, 0);

function isPrime(int $x, string $bcsqrt)
{
  for ($i = 2; $i <= $bcsqrt; $i++) {
    if ($x % $i === 0) {
      return false;
    }
  }
  return true;
}

echo isPrime($stdin, $bcsqrt) ? 'Yes' : 'No';
