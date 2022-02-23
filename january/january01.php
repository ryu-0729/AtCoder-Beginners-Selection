<?php

// AtCoder Beginner Contest 234 A - Weird Function
// 標準入力
$stdin = (int)trim(fgets(STDIN));

function calculation($int)
{
    $result = ($int * $int) + (2 * $int) + 3;

    return $result;
}

$answer = calculation(calculation(calculation($stdin) + $stdin) + calculation(calculation($stdin)));

echo $answer;
