<?php

require_once "helpers/print.php";

function solution($number)
{
    return array_sum(array_filter(range(0, $number - 1), static fn($value) => $value % 3 === 0 || $value % 5 === 0));
}

c_print(solution(10));