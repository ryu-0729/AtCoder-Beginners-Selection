<?php

$stdin = explode(' ', fgets(STDIN));

// バスの運賃を求める
$busPrice = intdiv((int)$stdin[1], 2);
$total = $stdin[0] + $busPrice;
echo $total;
