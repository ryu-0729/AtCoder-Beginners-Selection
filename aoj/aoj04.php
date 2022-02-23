<?php

// AOJ
// 標準入力
$elementCount = (int)trim(fgets(STDIN));
$stdinArray = explode(' ', trim(fgets(STDIN)));

// todo 解説の確認
function selectionSort($arrayData, $elementCount)
{
    // 交換回数を保持する変数
    $swapTimes = 0;
    for ($i = 0; $i <= $elementCount - 1; $i++) {
        $min = $$i;
        for ($j = $i; $j <= $elementCount; $j++) {
            if ($arrayData[$j] < $arrayData[$min]) {
                $min = $j;
                $temporaryHoldingValue = $arrayData[$i];
                $arrayData[$i] = $arrayData[$min];
                $arrayData[$min] = $temporaryHoldingValue;
                $swapTimes++;
            }
        }
    }
    return [$swapTimes, $arrayData];
}

list($count, $selectSortData) = selectionSort($stdinArray, $elementCount);
echo implode(' ', $selectSortData) . PHP_EOL;
echo $count . PHP_EOL;
