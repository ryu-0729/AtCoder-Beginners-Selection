<?php

// 028 動的計画法 カエルの移動の一般化
$n = trim(fgets(STDIN));
$array = explode(' ', trim(fgets(STDIN)));

$dp = [];
for ($i = 0; $i < $n; $i++) {
  if ($i === 0) $dp[$i] = 0;
  if ($i === 1) $dp[$i] = abs((int)$array[$i - 1] - (int)$array[$i]);
  if ($i >= 2) {
    $value1 = $dp[$i - 1] + abs((int)$array[$i - 1] - (int)$array[$i]);
    $value2 = $dp[$i - 2] + abs((int)$array[$i - 2] - (int)$array[$i]);
    $dp[$i] = min($value1, $value2);
  }
}

echo $dp[$n - 1];
