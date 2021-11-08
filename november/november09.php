<?php

// AtCoder Beginner Contest 211 Cycle Hit
while ($line = trim(fgets(STDIN))) {
    $array[] = trim($line);
}

$arrayValues = [
    'H',
    '2B',
    '3B',
    'HR',
];

foreach ($arrayValues as $value) {
    if (!in_array($value, $array, true)) {
        echo 'No';
        exit;
    }
    $answer = 'Yes';
}
if (!empty($answer)) echo $answer;
