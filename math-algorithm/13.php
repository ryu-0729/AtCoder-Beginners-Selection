<?php

// 再帰関数 階乗
$n = trim(fgets(STDIN));

function gmp(int $n)
{
  if ($n === 1) return 1;

  return gmp($n - 1) * $n;
}

echo gmp($n);
