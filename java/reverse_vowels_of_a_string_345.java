import java.util.ArrayList;
import java.util.List;

public class Solution {
    public String reverseVowels(String s) {
        String[] word = s.split("");
        String vowels = "aeiouAEIOU";
        int j = word.length - 1, i = 0;

        while (i < j) {

            if (vowels.contains(word[i]) && vowels.contains(word[j])) {
                var temp = word[i];
                word[i] = word[j];
                word[j] = temp;

                i++;
                j--;
            }

            if(!vowels.contains(word[i])){
                i++;
            }

            if(!vowels.contains(word[j])){
                j--;
            }
        }

        return String.join("", word);
    }
}


public void main(String[] args) {
    var solution = new Solution();
    System.out.println(solution.reverseVowels("hello"));
    System.out.println(solution.reverseVowels("leetcode"));
}