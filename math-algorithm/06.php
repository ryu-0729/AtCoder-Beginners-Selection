<?php

$stdin = trim(fgets(STDIN));
$bcsqrt = bcsqrt($stdin, 0);

$answer = [];
for ($i = 2; $i <= $bcsqrt; $i++) {
  while ($stdin % $i === 0) {
    $stdin /= $i;
    $answer[] = $i;
  }
}

if ($stdin >= 2) $answer[] = $stdin;

foreach ($answer as $value) {
  echo $value . ' ';
}
