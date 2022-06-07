<?php

// 3.3.3
$stdin = explode(' ', trim(fgets(STDIN)));

$factN = 1;
$factR = 1;
$factNR = 1;

for ($i = 1; $i <= $stdin[0]; $i++) $factN *= $i;
for ($i = 1; $i <= $stdin[1]; $i++) $factR *= $i;
for ($i = 1; $i <= $stdin[0] - $stdin[1]; $i++) $factNR *= $i;

echo $factN / ($factR * $factNR);
