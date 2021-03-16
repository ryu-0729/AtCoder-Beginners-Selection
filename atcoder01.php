<?php //簡単な標準入力を取得し表示する
  fscanf(STDIN, "%d", $a);
  fscanf(STDIN, "%d %d", $b, $c);
  fscanf(STDIN, "%s", $s);
  echo($a+$b+$c) . " " . $s;
?>