<?php //倍数判定問題
  fscanf(STDIN, "%d %d", $a, $b);
  $c = ($a * $b);
  if ($c % 2 === 0) {
    echo "Even";
  } else {
    echo "Odd";
  }
?>