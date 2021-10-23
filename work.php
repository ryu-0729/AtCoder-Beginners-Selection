<?php

// Tires
$stdin = trim(fgets(STDIN));
// er
$mt = substr($stdin, -2);
if ($mt === 'er') echo 'er';
// ist
$ist = substr($stdin, -3);
if ($ist === 'ist') echo 'ist';
