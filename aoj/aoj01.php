<?php

// AOJ Maximum Profit 最大利益
// 標準入力
$elementCount = (int)trim(fgets(STDIN));
$stdinArray = [];
for ($i = 0; $i < $elementCount; $i++) {
    $stdinArray[$i] = (int)trim(fgets(STDIN));
}

// 最大値の初期値
$maxValue = (int)-2000000000;
// 最小値
$minValue = $stdinArray[0];

// 最大、最小値の更新
for ($i = 1; $i < $elementCount; $i++) {
    $maxValue = max($maxValue, $stdinArray[$i] - $minValue);
    $minValue = min($minValue, $stdinArray[$i]);
}

echo $maxValue . PHP_EOL;
