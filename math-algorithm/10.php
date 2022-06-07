<?php

// TODO: 処理手順の理解不十分
// 3.3.6
$n = trim(fgets(STDIN));
$array = explode(' ', trim(fgets(STDIN)));

$cnt = [];
for ($i = 0; $i < 100000; $i++) $cnt[$i] = 0;
for ($i = 0; $i < $n; $i++) $cnt[(int)$array[$i]] += 1;

$answer = 0;
for ($i = 1; $i < 50000; $i++) {
  $answer += $cnt[$i] * $cnt[100000 - $i];
}
$answer += $cnt[50000] * ($cnt[50000] - 1) / 2;

echo $answer;
