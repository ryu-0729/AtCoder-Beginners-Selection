<?php

// HHKB プログラミングコンテスト 2022（AtCoder Beginner Contest 235） A - Rotate

$stdin = trim(fgets(STDIN));

$bca = $stdin[1] . $stdin[2] . $stdin[0];
$cab = $stdin[2] . $stdin[0] . $stdin[1];

echo $stdin + $bca + $cab;
