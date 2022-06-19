<?php

require_once "helpers/print.php";

function solve($s)
{
    $max = 0;
    $alphabet = range('A', 'Z');
    foreach (str_split($s) as $letter) {
        $alphabetKey = array_search(strtoupper($letter), $alphabet, true);
        if ($alphabetKey > $max) {
            $max = $alphabetKey;
        }
    }

    return $max;
}


c_print(solve("zodiac"));
c_print(solve("chruschtschov"));
c_print(solve("khrushchev"));
