<?php

$stdin = trim(fgets(STDIN));

function isPrime($x)
{
  for ($i = 2; $i <= $x - 1; $i++) {
    if ($x % $i === 0) {
      return false;
    }
  }
  return true;
}

for ($i = 2; $i <= (int)$stdin; $i++) {
  if (isPrime($i)) {
    echo $i . ' ';
  }
}
