<?php

// アルゴリズムとデータ構造の学習
// 時間の差を求めるアルゴリズム

// 標準入力は h時 m分 s秒 の形で2行入力されるものとする 例）1 30 30
$stdin1 = explode(' ', fgets(STDIN));
$stdin2 = explode(' ', fgets(STDIN));

// 時間を秒に変換
$time1 = ($stdin1[0] * 3600) + ($stdin1[1] * 60) + (int)$stdin1[2];
$time2 = ($stdin2[0] * 3600) + ($stdin2[1] * 60) + (int)$stdin2[2];
// 差分を比較する
$diff = ($time1 > $time2) ? $time1 - $time2 : $time2 - $time1;
// 秒からh時m分s秒の形に戻す ※整数値の徐算にはintdiv()を使用する
$h = intdiv($diff, 3600);
$m = intdiv($diff % 3600, 60);
$s = ($diff % 3600) % 60;
echo $h . '時' . $m . '分' . $s . '秒';
