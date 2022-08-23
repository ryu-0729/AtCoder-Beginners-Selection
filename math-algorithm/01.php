<?php

$stdin = explode(' ', trim(fgets(STDIN)));

$answer = 0;
foreach ($stdin as $value) {
  $answer += $value;
}

echo $answer;
