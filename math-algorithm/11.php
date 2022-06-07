<?php

// 3.4.3
$n = trim(fgets(STDIN));
$a = explode(' ', trim(fgets(STDIN)));
$b = explode(' ', trim(fgets(STDIN)));

$answer = 0;
for ($i = 0; $i < $n; $i++) {
  $result = ((int)$a[$i] * (1 / 3)) + ((int)$b[$i] * (2 / 3));
  $answer += $result;
}

echo $answer;
