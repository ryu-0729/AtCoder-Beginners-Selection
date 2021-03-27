<?php
  $n = fgets(STDIN); //N枚の円形の餅の取得
  while ($d = fgets(STDIN)) { //複数行のdcmの取得
    $ds[] = trim($d); 
  }

  //$dsで同じ値を削除しその数を取得し$uniqueDに代入
  $uniqueD = count(array_unique($ds));

  echo $uniqueD;
?>