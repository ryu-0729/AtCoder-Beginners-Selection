<?php
  //処理を考える

  $n = fgets(STDIN); //N枚のカード枚数を取得
  $a = explode(' ', trim(fgets(STDIN))); //N以下のa（カードの値）を取得

  rsort($a); //降順に並び替えキーも順に与える→キーを並び替えることで後のfor文で生きてくる！

  $alice = 0; //Aliceの合計値
  $bob = 0; //Bobの合計値

  //AliceとBobのターン毎に取得したカードを導き出す
  for ($i = 0; $i < $n; $i++) {
    if ($i % 2 === 0) { //ターンが偶数→Aliceのターン
      $alice += $a[$i];
    } else {
      $bob += $a[$i];
    }
  }

  $total = $alice - $bob; //AliceがBobより何点多く取得しているか求める

  echo $total;
?>