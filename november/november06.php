<?php

// AtCoder Beginner Contest 155 Papers, Please

$count = trim(fgets(STDIN));
$stdin = explode(' ', trim(fgets(STDIN)));

// $stdinの中の偶数を特定
for ($i = 0; $i <= $count; $i++) {
    if ($stdin[$i] % 2 == 0 && $stdin[$i] % 3 != 0 && $stdin[$i] % 5 != 0) {
        echo 'DENIED';
        exit;
    }
}
echo 'APPROVED';
