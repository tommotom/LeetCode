class Solution {

  private int[] ratings;

  public int candy(int[] ratings) {
    this.ratings = ratings;
    int[] candies = new int[ratings.length];
    Deque<Integer> q = new ArrayDeque<>();
    for (int i = 0; i < ratings.length; i++) {
      if (isBottom(i)) {
        candies[i] = 1;
        q.addLast(i);
      }
    }
    while (q.size() > 0) {
      int i = q.pollFirst();
      if (i > 0 && ratings[i-1] > ratings[i] && (candies[i-1] == 0 || candies[i-1] < candies[i] + 1)) {
        candies[i-1] = candies[i] + 1;
        q.addLast(i-1);
      }
      if (i+1 < candies.length && ratings[i+1] > ratings[i] && (candies[i+1] == 0 || candies[i+1] < candies[i] + 1)) {
        candies[i+1] = candies[i] + 1;
        q.addLast(i+1);
      }
    }
    return Arrays.stream(candies).sum();
  }

  private boolean isBottom(int i) {
    if (i > 0 && ratings[i-1] < ratings[i]) {
      return false;
    }
    if (i+1 < ratings.length && ratings[i] > ratings[i+1]) {
      return false;
    }
    return true;
  }
}
