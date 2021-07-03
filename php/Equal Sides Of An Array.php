<?php

require_once "helpers/print.php";

function find_even_index($arr){
    foreach($arr as $key=>$val){
        $sumLeft = array_sum(array_slice($arr, 0, $key));
        $sumRight = array_sum(array_slice($arr, $key+1));
        if($sumLeft === $sumRight){
            return $key;
        }
    }
    return -1;
}

c_print(find_even_index(array(1,2,3,4,3,2,1)));
c_print(find_even_index([1,100,50,-51,1,1]));
c_print(find_even_index([1,2,3,4,5,6]));
