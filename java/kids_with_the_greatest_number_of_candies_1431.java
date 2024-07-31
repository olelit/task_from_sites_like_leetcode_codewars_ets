import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        var result = new ArrayList<Boolean>(candies.length);
        int max = candies[0];

        for (int i = 1; i < candies.length; i++) {
            if (candies[i] > max) {
                max = candies[i];
            }
        }

        for (var candy : candies) {
            if (candy + extraCandies >= max) {
                result.add(true);
            } else {
                result.add(false);
            }
        }

        return result;
    }
}


public void main(String[] args) {
    var solution = new Solution();
    System.out.println(solution.kidsWithCandies(new int[]{2, 3, 5, 1, 3}, 3));
    System.out.println(solution.kidsWithCandies(new int[]{4, 2, 1, 1, 2}, 1));
    System.out.println(solution.kidsWithCandies(new int[]{12, 1, 12}, 10));
}