<?php

class Solution {

    /**
     * @param String[] $words
     * @param String[] $puzzles
     * @return Integer[]
     */
    function findNumOfValidWords($words, $puzzles) {
        $validWords = [];
        foreach ($puzzles as $key=>$puzzle)
        {
            $splitPuzzle = str_split($puzzle);
            $firstLetter = $splitPuzzle[0];
            $validWords[$key] = 0;
            foreach ($words as $word)
            {
                $uniquePuzzle = array_unique($splitPuzzle);
                $splitWord = array_unique(str_split($word));
                $intersect = count(array_intersect($uniquePuzzle, $splitWord));

                if(in_array($firstLetter, $splitWord) && count($splitWord) === $intersect)
                {
                    $validWords[$key] = $validWords[$key] + 1;
                }
            }
        }

        return $validWords;
    }
}

$sol = new Solution();

$words = ["aaaa","asas","able","ability","actt","actor","access"];
$puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"];
print_r($sol->findNumOfValidWords($words, $puzzles));
