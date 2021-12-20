<?php

class CombinationIterator
{
    private $combinations = [];
    private $counter = 0;
    private $characters;
    private $combinationLength;

    function __construct($characters, $combinationLength)
    {
        $this->characters = $characters;
        $this->combinationLength = $combinationLength;
        $this->buildCombinations('', 0);
    }

    public function buildCombinations($combo, $start)
    {
        if (strlen($combo) === $this->combinationLength) {
            $this->combinations[] = $combo;
        }

        $chars = str_split($this->characters);

        for ($i = $start; $i < count($chars); $i++) {
            $value = $chars[$i];
            $this->buildCombinations($combo . $value, $i + 1);
        }
    }

    /**
     * @return String
     */
    function next()
    {
        $res = $this->combinations[$this->counter];
        $this->counter++;
        return $res;
    }

    /**
     * @return Boolean
     */
    function hasNext()
    {
        return $this->counter < count($this->combinations);
    }
}

$itr = new CombinationIterator("abc", 2);
print_r($itr->next() . PHP_EOL);
print_r($itr->hasNext() . PHP_EOL);
print_r($itr->next() . PHP_EOL);
print_r($itr->hasNext() . PHP_EOL);
print_r($itr->next() . PHP_EOL);
print_r($itr->hasNext() . PHP_EOL);
