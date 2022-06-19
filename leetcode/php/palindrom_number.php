<?php

class Solution {

    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
        $str = (string)$x;
        $revStr = strrev($str);
        return $str === $revStr;
    }
}

$solution = new Solution();
echo $solution->isPalindrome(121) .'<br>';
echo $solution->isPalindrome(-121).'<br>';
echo $solution->isPalindrome(10).'<br>';
echo $solution->isPalindrome(-101).'<br>';