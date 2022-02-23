<?php

// AOJ Bubble Sort バブルソート
// 標準入力
$elementCount = (int)trim(fgets(STDIN));
$stdinArray = explode(' ', trim(fgets(STDIN)));

/**
 * バブルソートによる交換回数と配列を返す
 *
 * @param $arrayData
 * @param $elementCount
 * @return array
 */
function bubleSort($arrayData, $elementCount)
{
    // 交換回数を保持する変数
    $swapTimes = 0;
    $flag = true;
    for ($i = 0; $flag; $i++) {
        $flag = false;
        for ($j = $elementCount - 1; $j >= $i + 1; $j--) {
            if ($arrayData[$j] < $arrayData[$j - 1]) {
                // 隣接部分の交換
                $temporaryHoldingValue = $arrayData[$j];
                $arrayData[$j] = $arrayData[$j - 1];
                $arrayData[$j - 1] = $temporaryHoldingValue;
                $flag = true;
                $swapTimes++;
            }
        }
    }

    return [$swapTimes, $arrayData];
}

list($count, $bubleData) = bubleSort($stdinArray, $elementCount);
echo implode(' ', $bubleData) . PHP_EOL;
echo $count . PHP_EOL;
