<?php

// AtCoder Beginner Contest 162 FizzBuzz Sum
$stdin = (int)trim(fgets(STDIN));

$total = null;
for ($i = 0; $i <= $stdin; $i++) {
    if (($i % 3 === 0) && ($i % 5 === 0)) continue;
    if ($i % 3 === 0) continue;
    if ($i % 5 === 0) continue;
    $total += $i;
}

echo $total;
