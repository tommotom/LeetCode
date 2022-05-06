class Solution {
  public String removeDuplicates(String s, int k) {
    char[] arr = s.toCharArray();
    int n = arr.length;
    char[] chars = new char[n];
    int[] count = new int[n];
    int top = -1;
    for (int i = 0; i < n; i++) {
      top++;
      count[top] = 1;
      chars[top] = arr[i];
      if (top > 0 && chars[top-1] == arr[i]) {
        count[top] += count[top-1];
      }

      if (count[top] == k) {
        top -= k;
      }
    }

    return new String(chars, 0, top+1);
  }
}
