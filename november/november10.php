<?php

// AtCoder Beginner Contest 209 Counting
$stdin = explode(' ', trim(fgets(STDIN)));

if ($stdin[0] >= $stdin[1]) {
    echo 0;
    exit;
} else {
    $answer = $stdin[1] - $stdin[0];
    echo $answer += 1;
}
