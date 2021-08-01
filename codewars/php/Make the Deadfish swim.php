<?php

require_once "helpers/print.php";

function parse(string $data): array
{
    $output = [];
    $value = 0;

    $command = [
        'i' => function () use (&$value) {
            $value++;
        },
        'd' => function () use (&$value) {
            $value--;
        },
        's' => function () use (&$value) {
            $value *= $value;
        },
        'o' => static function () use (&$output, &$value) {
            $output[] = $value;
        },
    ];

    foreach (str_split($data) as $letter){
        if(isset($command[$letter])){
            $command[$letter]();
        }
    }

    return $output;
}

c_print(implode(' ', parse('iiisdoso')));
c_print(implode(' ', parse('iiisxxxdoso')));
