<?php

$stdin = trim(fgets(STDIN));

$answer = 1;
for ($i = 2; $i <= (int) $stdin; $i++) {
  $answer *= $i;
}

echo $answer;
