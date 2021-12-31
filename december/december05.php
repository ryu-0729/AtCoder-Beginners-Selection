<?php

// AtCoder Beginner Contest 233 A Reverse

$stdin = explode(' ', trim(fgets(STDIN)));
$string = trim(fgets(STDIN));

// 処理手順
// 1.$stdinの[1]から[0]を引いた数の取得→何文字目までの数
// 2.substrで特定の文字を取得
// 3.strrevで2の文字反転
// 4.str_replaceで$stringの2を3に変換
$endNumber = (int)$stdin[1] - (int)$stdin[0] + 1;
$substrString = substr($string, (int)$stdin[0] - 1, $endNumber);
$strrevString = strrev($substrString);
$replaceString = str_replace($substrString, $strrevString, $string);
echo $replaceString;
