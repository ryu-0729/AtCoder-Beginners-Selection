<?php

// 再帰関数 ユークリッドの互除法

$array = explode(' ', trim(fgets(STDIN)));

function gcd(int $a, int $b)
{
  if ($b === 0) return $a;
  return gcd($b, $a % $b);
}

if ($array[0] > $array[1]) {
  echo gcd((int)$array[0], (int)$array[1]);
} else {
  echo gcd((int)$array[1], (int)$array[0]);
}
