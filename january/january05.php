<?php

// HHKB プログラミングコンテスト 2022（AtCoder Beginner Contest 235） B - Climbing Takahashi

$stdin = trim(fgets(STDIN));
$array = explode(' ', trim(fgets(STDIN)));

// 初期位置
$currentPosition = $array[0];
for ($i = 1; $i < count($array); $i++) {
    if ($currentPosition < $array[$i]) {
        $currentPosition = $array[$i];
    } else {
        break;
    }
}
echo $currentPosition;
