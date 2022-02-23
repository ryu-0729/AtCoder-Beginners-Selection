<?php

// AOJ Insertion Sort 挿入ソート
// 標準入力
$elementCount = (int)trim(fgets(STDIN));
$stdinArray = explode(' ', trim(fgets(STDIN)));
// ソート前の配列順
echo implode(' ', $stdinArray) . PHP_EOL;
for ($i = 1; $i <= $elementCount - 1; $i++) {
    // 一時保持変数
    $temporaryHoldingValue = $stdinArray[$i];
    // ソート済みの部分列から一時保持変数を挿入する箇所を特定するループ変数
    $positionParticular = $i - 1;
    // 挿入ソート処理
    while ($positionParticular >= 0 && $stdinArray[$positionParticular] > $temporaryHoldingValue) {
        $stdinArray[$positionParticular + 1] = $stdinArray[$positionParticular];
        $positionParticular--;
    }
    $stdinArray[$positionParticular + 1] = $temporaryHoldingValue;
    // 挿入ソート処理後の配列順
    echo implode(' ', $stdinArray) . PHP_EOL;
}
