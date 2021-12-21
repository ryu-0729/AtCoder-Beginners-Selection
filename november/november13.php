<?php
// AtCoder Beginner Contest 218 qwerty

// abc配列 0 => 'a'なので注意
$arrayAbc = range('a', 'z');
// 標準入力
$arrayStdin = explode(' ', trim(fgets(STDIN)));

$text = '';
foreach ($arrayStdin as $value) {
    $text .= $arrayAbc[(int)$value - 1];
}
echo $text;
