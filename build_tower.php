<?php

require_once "helpers/print.php";

const TOWER_BLOCK = "*";
const EMPTY_BLOCK = " ";

function tower_builder(int $n): array {
    $len = ($n*2)-1;
    $tree = [];
    for($i = $len; $i > 0; $i-=2) {
        //можно было через str_repeat, тогда тело цикло было бы 1-2 строки
        $towerLine = array_fill($n-1, $len-$i+1, TOWER_BLOCK);
        $emptyLine = array_fill(0, $len, EMPTY_BLOCK);
        $tree[] = implode("",array_replace($emptyLine, $towerLine));
        $n--;
    }
    return $tree;
}

foreach(tower_builder(6) as $val){
    c_print($val);
}



