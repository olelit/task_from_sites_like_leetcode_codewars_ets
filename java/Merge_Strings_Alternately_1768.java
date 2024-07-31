import java.util.Arrays;

public class Solution {
    public String mergeAlternately(String word1, String word2) {

        var megred = new StringBuilder(word1.length() + word2.length());
        for (int i = 0; i < word1.length(); i++) {
            megred.append(word1.charAt(i));

            if(i < word2.length()){
                megred.append(word2.charAt(i));
            }
        }

        if(word1.length() < word2.length()){
            megred.append(word2, word1.length(), word2.length());
        }


        return megred.toString();
    }
}


public void main(String[] args) {
    var solution = new Solution();
    System.out.println(solution.mergeAlternately("abc", "pqr"));
    System.out.println(solution.mergeAlternately("ab", "pqrs"));
    System.out.println(solution.mergeAlternately("abcd", "pq"));
}