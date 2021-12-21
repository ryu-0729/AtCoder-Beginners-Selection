<?php

// AtCoder Beginner Contest 209 Can you buy them all?
$firstLine = explode(' ', trim(fgets(STDIN)));
$secondLine = explode(' ', trim(fgets(STDIN)));

$totalPrice = 0;
for ($i = 0; $i < $firstLine[0]; $i++) {
    if ($i % 2 != 0) {
        $totalPrice += $secondLine[$i] - 1;
    } else {
        $totalPrice += $secondLine[$i];
    }
}
echo ((int)$firstLine[1] >= $totalPrice) ? 'Yes' : 'No';
