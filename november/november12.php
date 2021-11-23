<?php
// AtCoder Beginner Contest 218 Weather Forecast

$n = trim(fgets(STDIN));
$s = trim(fgets(STDIN));
// 文字列特定
$wether = substr($s, (int)$n - 1, 1);

if ($wether === 'o') {
    echo 'Yes';
} else {
    echo 'No';
}
