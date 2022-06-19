<?php

require_once "helpers/print.php";

function createPhoneNumber($numbersArray) {
    $f = implode(array_slice($numbersArray, 0, 3));
    $f2 = implode(array_slice($numbersArray, 3, 3));
    $f3 = implode(array_slice($numbersArray, 6, 4));
    return "($f) $f2-$f3";
}

c_print(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]));
c_print(createPhoneNumber([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]));