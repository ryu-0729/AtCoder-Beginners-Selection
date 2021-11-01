<?php
// AtCoder Beginner Contest 162 Lucky 7
// 標準入力
$stdin = (string)trim(fgets(STDIN));

$res = strpos($stdin, '7');
$answer = ($res !== false) ? 'Yes' : 'No';
echo $answer;
