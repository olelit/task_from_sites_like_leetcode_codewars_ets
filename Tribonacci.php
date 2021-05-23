<?php

function tribonacci($signature, $n)
{
    if($n === 0)
        return [];

    if($n < count($signature))
        return array_slice($signature, 0, $n);

    $i = count($signature);
    while ($i < $n){
        $signature[] = array_sum(array_slice($signature, -3));
        $i++;
    }

    return $signature;
}

function c_print(string $val)
{
    echo $val.PHP_EOL;
}

c_print(implode(",", tribonacci([1,1,1],10)));
c_print(implode(",", tribonacci([0,0,1],10)));
c_print(implode(",", tribonacci([0,1,1],10)));
c_print(implode(",", tribonacci([1,1,1],1)));
c_print(implode(",", tribonacci([300,200,100],0)));