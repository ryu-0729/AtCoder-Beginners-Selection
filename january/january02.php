<?php

// AtCoder Beginner Contest 234 B - Longest Segment
// 標準入力
$stdin = (int)trim(fgets(STDIN));
$array = [];
while ($line = trim(fgets(STDIN))) {
    list($x, $y) = explode(' ', $line);
    $array[] = [(int)$x, (int)$y];
}

/**
 * 2次元平面上の2点の距離を求める関数
 *
 * @param array $distanceP
 * @param array $distanceQ
 * @return float
 */
function distanceCalculation(array $distanceP, array $distanceQ): float
{
    // $xと$yの作成
    $x = ($distanceQ[0] - $distanceP[0]) ** 2;
    $y = ($distanceQ[1] - $distanceP[1]) ** 2;
    // sqrt()で平方根を求める
    return sqrt($x + $y);
}

$answer = -1;
for ($i = 0; $i < count($array); $i++) {
    for ($j = $i + 1; $j < count($array); $j++) {
        $answer = max($answer, distanceCalculation($array[$i], $array[$j]));
    }
}

echo $answer;
