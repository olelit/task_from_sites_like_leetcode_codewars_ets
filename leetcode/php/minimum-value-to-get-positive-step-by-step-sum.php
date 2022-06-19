<?php

class Solution
{
    function minStartValue(array $nums): int
    {
        return $this->calculate($nums, 1);
    }

    private function calculate(array $nums, int $start): int
    {
        $total = $start;
        foreach ($nums as $value) {
            $total += $value;
            if($total < 1)
            {
                return $this->calculate($nums, $start+1);
            }
        }
        return $start;
    }
}

$sol = new Solution();
$arr1 = [-3, 2, -3, 4, 2];
print_r($sol->minStartValue($arr1).PHP_EOL);
$arr2 = [1, 2];
print_r($sol->minStartValue($arr2).PHP_EOL);
$arr3 = [1, -2, -3];
print_r($sol->minStartValue($arr3).PHP_EOL);
