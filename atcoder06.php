<?php
  function sumDigit($digit) //各桁の和を計算する関数を用意
  {
    $sum = 0; //各桁の和
    while ($digit > 0) { //$digitが0になるまで処理を続ける
      $sum += $digit % 10; //合計値に$digitを10で割った余りをたす
      $digit /= 10; //$digit自身に10で割った数をセット
    }
    return $sum; //各桁の和を返す
  }

  list($n, $a, $b) = explode(' ', fgets(STDIN)); //標準入力をlist()でそれぞれに代入

  $totalSum = 0;

  for ($i = 1; $i <= $n; $i++) { //N以下の数値の処理
    $digitTotal = sumDigit($i); //各桁の和を$digitTotalに代入
    if ($digitTotal >= $a && $digitTotal <= $b) { //各桁の和がA以上B以下であれば処理
      $totalSum += $i; //合計値に足す
    }
  }

  echo $totalSum; //A以上B以下の合計値を出力
?>