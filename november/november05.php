<?php

// AtCoder Beginner Contest 155 Poor
$stdin = explode(' ', trim(fgets(STDIN)));

$answer = ($stdin[0] === $stdin[1] || $stdin[0] === $stdin[2] || $stdin[1] === $stdin[2]) ? 'Yes' : 'No';
// 全ての値が等しい時
if ($stdin[0] === $stdin[1] && $stdin[0] === $stdin[2]) {
    $answer = 'No';
}
echo $answer;
