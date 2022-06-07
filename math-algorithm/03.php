<?php

$stdin = trim(fgets(STDIN));
echo gmp_fact((int) $stdin);
