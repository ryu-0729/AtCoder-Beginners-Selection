<?php

$count = trim(fgets(STDIN));
$stdin = explode(' ', trim(fgets(STDIN)));

$total = 0;
foreach ($stdin as $value) {
  $total += $value;
}

echo $total % 100;
