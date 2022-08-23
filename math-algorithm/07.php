<?php

// 3.3.4
$n = trim(fgets(STDIN));
$stdin = explode(' ', trim(fgets(STDIN)));

$result = array_count_values($stdin);

$ad = $result[100] * $result[400];
$bc = $result[200] * $result[300];

echo $ad + $bc;
