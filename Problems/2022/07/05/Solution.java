class Solution {

  private int[] nums;
  private int[] length;
  private Map<Integer, Integer> numMap;

  public int longestConsecutive(int[] nums) {
    if (nums.length == 0) {
      return 0;
    }

    int n = nums.length;
    this.nums = nums;
    numMap = new HashMap<>();
    for (int i = 0; i < n; i++) {
      numMap.put(nums[i], i);
    }

    length = new int[nums.length];
    for (int i = 0; i < n; i++) {
      length[i] = length(i);
    }
    return Arrays.stream(length).max().getAsInt();
  }

  private int length(int i) {
    if (length[i] != 0) {
      return length[i];
    }
    int num = nums[i];
    if (numMap.containsKey(num+1)) {
      length[i] = length(numMap.get(num+1)) + 1;
    } else {
      length[i] = 1;
    }
    return length[i];
  }
}
