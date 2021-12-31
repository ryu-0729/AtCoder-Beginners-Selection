<?php

// アルゴリズムとデータ構造の学習
// ユークリッドの互除法 ※最大公約数を求める

// 標準入力は m n の形で入力される 例）128
$stdin1 = (int)trim(fgets(STDIN));
$stdin2 = (int)trim(fgets(STDIN));

echo greatestCommonDivisor($stdin1, $stdin2);

/**
 * 最大公約数を求める
 *
 * @param integer $number
 * @param integer $anotherNumber
 * @return integer
 */
function greatestCommonDivisor(int $number, int $anotherNumber): int
{
    if ($number > $anotherNumber) {
        if ($anotherNumber === 1) return $number;
        $remainder = $number % $anotherNumber;
        while ($remainder >= 0) {
            if ($remainder === 0) {
                return $anotherNumber;
                break;
            }
            $number = $anotherNumber;
            $anotherNumber = $remainder;
            $remainder = $number % $anotherNumber;
        }
    } else {
        if ($number === 1) return $anotherNumber;
        $remainder = $anotherNumber % $number;
        while ($remainder >= 0) {
            if ($remainder === 0) {
                return $number;
                break;
            }
            $anotherNumber = $number;
            $number = $remainder;
            $remainder = $anotherNumber % $number;
        }
    }
}
