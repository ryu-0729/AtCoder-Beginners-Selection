<?php

// 029 動的計画法 階段の上がり方
$n = trim(fgets(STDIN));

$array = [];
for ($i = 0; $i <= $n; $i++) {
  if ($i === 0) $array[$i] = 1;
  if ($i === 1) $array[$i] = 1;
  if ($i >= 2) {
    $array[$i] = $array[$i - 1] + $array[$i - 2];
  }
}

echo $array[$n];
