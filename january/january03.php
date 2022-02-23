<?php

// AtCoder Beginner Contest 234 C - Happy New Year!
// 標準入力を受け取り2進数に変換
$binaryNumber = decbin((int)trim(fgets(STDIN)));
// 1を2に置き換えて出力
echo str_replace('1', '2', $binaryNumber);

// 解説 https://atcoder.jp/contests/abc234/editorial/3224
