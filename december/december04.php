<?php

// AtCoder Beginner Contest 233 10yen Stamp

$stdin = explode(' ', trim(fgets(STDIN)));

// 貼られている切手
$stamp = (int)$stdin[0];
// 合計金額
$total = (int)$stdin[1];

if ($stamp >= $total) {
    echo 0;
} else {
    for ($i = 0; $stamp <= $total; $i++) {
        $stamp += 10;
        if ($stamp >= $total) {
            echo $i + 1;
            break;
        }
    }
}
