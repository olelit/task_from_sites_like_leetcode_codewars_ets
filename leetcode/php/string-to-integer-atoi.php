<?php

class Solution
{
    public const LIMIT = 2147483647;

    private function buildDigit(string $s): int
    {
        $val = '';
        $sArr = str_split($s);
        for($i = 0; $i < count($sArr); $i++)
        {
            $value = $sArr[$i];

            if (ctype_alpha($value) || $value === '.') {
                break;
            }

            $val .= $value;
        }

        return (int)$val;
    }

    /**
     * @param String $s
     * @return Integer
     */
    function myAtoi($s)
    {
        $value = $this->buildDigit($s);
        if (abs($value) > self::LIMIT) {
            $coof = $value >= 0 ? 1 : -1;
            $value = (self::LIMIT) * $coof;
            $value = $value < 0 ? $value - 1 : $value;
        }
        return $value;
    }
}

$sol = new Solution();
print_r($sol->myAtoi('+0 123') . PHP_EOL);
print_r($sol->myAtoi('+004500') . PHP_EOL);
print_r($sol->myAtoi('words and 987') . PHP_EOL);
print_r($sol->myAtoi('42') . PHP_EOL);
print_r($sol->myAtoi('   -42') . PHP_EOL);
print_r($sol->myAtoi('4193 with words') . PHP_EOL);
print_r($sol->myAtoi('3.14159') . PHP_EOL);
print_r($sol->myAtoi('-91283472332') . PHP_EOL);
print_r($sol->myAtoi('21474836460') . PHP_EOL);
print_r($sol->myAtoi('  -0012a42') . PHP_EOL);
