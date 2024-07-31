import java.util.ArrayList;
import java.util.List;

public class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {

        if (n == 0) return true;

        int l = flowerbed.length;
        for (int i = 0; i < l; i++) {
            int el = flowerbed[i];
            if (el == 0) {

                if ((i > 0 && flowerbed[i - 1] == 1) || (i < l - 1 && flowerbed[i + 1] == 1)) {
                    continue;
                }

                n -= 1;

                if (n == 0) return true;

                flowerbed[i] = 1;
            }
        }

        return false;
    }
}


public void main(String[] args) {
    var solution = new Solution();
    System.out.println(solution.canPlaceFlowers(new int[]{1,0,0,0,0,0,1}, 2));
    System.out.println(solution.canPlaceFlowers(new int[]{0, 1, 0}, 1));
    System.out.println(solution.canPlaceFlowers(new int[]{0, 0, 1, 0, 0}, 1));
    System.out.println(solution.canPlaceFlowers(new int[]{1, 0, 0, 0, 1}, 1));
    System.out.println(solution.canPlaceFlowers(new int[]{1, 0, 0, 0, 1}, 2));
}