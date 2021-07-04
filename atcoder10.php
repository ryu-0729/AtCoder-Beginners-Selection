<?php
    // 標準出力を受け取る
    $stdin = trim(fgets(STDIN));

    // 文字検索配列作成
    $hakutyuumu = [
        'eraser','erase','dreamer','dream'
    ];

    foreach ($hakutyuumu as $code) {
        // 標準入力内の検索配列に一致する文字をリプレース
        $stdin = str_replace($code, '', $stdin);
    }

    echo $stdin ? 'NO' : 'YES';
?>