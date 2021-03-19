<?php
  fscanf(STDIN, "%d", $totalNumber); //数字の数を取得

  $numbers = explode(' ', fgets(STDIN)); //スペース区切りの数字の取得

  $counts = []; //処理を行った回数を記録するため空の配列を準備

  for ($i = 0; $i < $totalNumber; $i++) { //1行目で取得した数値以下であれば処理を行う
    $count = 0; //奇数だった場合処理は行わせないので0
    while ($numbers[$i] % 2 === 0) { //$numbersの中の配列1個ごとに処理を行う
      $count += 1; //処理が走った時点で$countを+1
      $numbers[$i] /= 2; //$numbers[$i]自身を割る2
    }
    $counts[$i] = $count; //処理が終わった時点で空の配列の中にいれる
  }

  echo min($counts);
?>