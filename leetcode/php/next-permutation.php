<?php
class Solution {


    function swap(&$nums, $i, $j)
    {
        $temp = $nums[$i];
        $nums[$i] = $nums[$j];
        $nums[$j] = $temp;
    }

    function reverse(&$nums, $start)
    {
        $i = $start;
        $j = count($nums)-1;
        while ($i < $j) {
            $this->swap($nums, $i, $j);
            $i++;
            $j--;
        }
    }

    /**
     * @param Integer[] $nums
     * @return NULL
     */
    function nextPermutation(&$nums) {
        $i = count($nums)-2;

        while ($i >= 0 && $nums[$i+1] <= $nums[$i]){
            $i--;
        }

        $j = count($nums)-1;
        while ($i >= 0 && $j > $i) {
            if ($nums[$i] < $nums[$j]) {
                $this->swap($nums, $i, $j);
                break;
            }
            $j--;
        }
        $this->reverse($nums,$i+1);
    }
}

$solution = new Solution();
$nums = [1,2,3];
$solution->nextPermutation($nums).PHP_EOL;
//$nums1 = [3, 2, 1];
//echo $solution->nextPermutation($nums1).PHP_EOL;
//$nums2 = [1, 1, 5];
//echo $solution->nextPermutation($nums2).PHP_EOL;
//$nums3 = [1];
//echo $solution->nextPermutation($nums3).PHP_EOL;