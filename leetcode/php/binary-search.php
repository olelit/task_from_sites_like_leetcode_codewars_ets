<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function search($nums, $target)
    {
        $left = 0;
        $right = count($nums);
        $pos = -1;

        while ($left != $right) {
            $medium = (int)(($left + $right) / 2);
            if ($nums[$medium] === $target) {
                return $medium;
            } else {
                if ($target > $nums[$medium]) {
                    $left = $medium + 1;
                } else {
                    $right = $medium;
                }
            }
        }

        return $pos;
    }
}

$solution = new Solution();
echo $solution->search([-1, 0, 3, 5, 9, 12], 9) . PHP_EOL;
echo $solution->search([-1, 0, 3, 5, 9, 12], 2);
