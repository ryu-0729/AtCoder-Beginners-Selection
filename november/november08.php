<?php

// AtCoder Beginner Contest 211 Blood Pressure
$stdin = explode(' ', trim(fgets(STDIN)));
// A - B
(int)$denominator = $stdin[0] - $stdin[1];
$division = $denominator / 3;
$answer = $division + $stdin[1];
echo $answer;
