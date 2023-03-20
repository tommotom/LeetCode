class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int canPlace = 0;
        for (int i = 0; i < flowerbed.length; i++) {
            if (flowerbed[i] == 1) {
                continue;
            }
            if (i > 0 && flowerbed[i-1] == 1) {
                continue;
            }
            if (i+1 < flowerbed.length && flowerbed[i+1] == 1) {
                continue;
            }
            flowerbed[i] = 1;
            canPlace++;
        }
        return n <= canPlace;
    }
}
