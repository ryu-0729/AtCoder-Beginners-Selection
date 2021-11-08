<?php

// AtCoder Beginner Contest 226 Counting Arrays
// 回答できず。。
/* $count = (int)trim(fgets(STDIN));
$stdin = [];
for ($i = 1; $i <= $count; $i++) {
    $stdin[$i] = explode(' ', trim(fgets(STDIN)));
} */

$count = (int)trim(fgets(STDIN));
// 配列に格納
for ($i = 0; $i < $count; $i++) {
    $array[] = trim(fgets(STDIN));
}
// 同一の値の削除
$answer = array_unique($array);
// 配列の数を出力
echo count($answer);
