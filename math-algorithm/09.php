<?php

// 3.3.5
$n = trim(fgets(STDIN));
$stdin = explode(' ', trim(fgets(STDIN)));

$result = array_count_values($stdin);

$red = $result[1];
$yellow = $result[2];
$blue = $result[3];

echo $red * ($red - 1) / 2 + $yellow * ($yellow - 1) / 2 + $blue * ($blue - 1) / 2;
