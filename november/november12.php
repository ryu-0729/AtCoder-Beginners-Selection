<?php
// AtCoder Beginner Contest 218 Weather Forecast

$n = trim(fgets(STDIN));
$s = trim(fgets(STDIN));
// 文字列特定
$wether = substr($s, (int)$n - 1, 1);

echo ($wether === 'o') ? 'Yes' : 'No';
