<?php

require_once "helpers/print.php";

const OPEN_BRACKET = ['(', '{', '['];
const CLOSE_BRACKET = [')', '}', ']'];

function validBraces($braces)
{
    $brackets = [];
    foreach (str_split($braces) as $item) {
        if (in_array($item, OPEN_BRACKET, true)) {
            $brackets[] = $item;
        } else {
            $closeElemKey = array_search($item, CLOSE_BRACKET, true);
            $lastElemKey = array_search(array_pop($brackets), OPEN_BRACKET, true);

            if($closeElemKey !== $lastElemKey){
                return false;
            }
        }
    }
    return empty($brackets);
}

c_print(validBraces("()"));
c_print(validBraces("[(])"));