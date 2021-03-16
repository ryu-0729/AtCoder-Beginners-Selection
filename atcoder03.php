<?php
  /* fscanf(STDIN, "%d", $a);
  var_dump($a); */ //←これだと取得した値がint型
  $stdin = trim(fgets(STDIN)); //←string型で取得する
  $ball_total = 0;
  if ($stdin[0] === '1') {
    $ball_total += 1;
  }
  if ($stdin[1] === '1') {
    $ball_total += 1;
  }
  if ($stdin[2] === '1') {
    $ball_total += 1;
  }

  echo $ball_total;
?>