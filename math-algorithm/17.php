<?php

// 030 動的計画法 ナップザック問題
[$N, $W] = explode(' ', trim(fgets(STDIN)));

$dp = array_fill(0, $N + 1, array_fill(0, $W + 1, 0));

for ($i = 0; $i < $N; $i++) {
  [$w, $v] = explode(' ', trim(fgets(STDIN)));
  for ($j = 0; $j < $W + 1; $j++) {
    $dp[$i + 1][$j] = $j < $w
      ? $dp[$i][$j]
      : max($dp[$i][$j], $dp[$i][$j - $w] + $v);
  }
}

echo max($dp[$N]);
