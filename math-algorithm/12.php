<?php

// 3.3.4
$n = trim(fgets(STDIN));

$answer = 0;
for ($i = (int)$n; $i >= 1; $i--) {
  $answer += 1 * $n / $i;
}

echo $answer;
