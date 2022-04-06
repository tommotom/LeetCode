class Solution {
  public int threeSumMulti(int[] arr, int target) {
    HashMap<Integer, Long> counter = new HashMap<>();
    for (int num : arr) {
      counter.put(num, counter.getOrDefault(num, 0L) + 1);
    }

    long ans = 0, mod = 1_000_000_007;

    // a == b == c
    for (int a = 0; a < 101; a++) {
      if (!counter.containsKey(a) || counter.get(a) < 3 || target != 3 * a) {
        continue;
      }
      Long count = counter.get(a);
      ans += count * (count - 1) * (count - 2) / 6;
      ans %= mod;
    }

    // a == b
    for (int a = 0; a < 101; a++) {
      if (!counter.containsKey(a) || counter.get(a) < 2) {
        continue;
      }
      int c = target - (2*a);
      if (!counter.containsKey(c) || a == c) {
        continue;
      }
      Long count1 = counter.get(a);
      Long count2 = counter.get(c);
      ans += count1 * (count1 - 1) * count2 / 2;
      ans %= mod;
    }

    // a != b != c
    for (int a = 0; a < 101; a++) {
      if (!counter.containsKey(a)) {
        continue;
      }
      for (int b = a+1; b < 101; b++) {
        if (!counter.containsKey(b) || ! counter.containsKey(target - a - b)) {
          continue;
        }
        int c = target - a - b;
        if (!counter.containsKey(c) || c <= b) {
          continue;
        }
        ans += counter.get(a) * counter.get(b) * counter.get(c);
        ans %= mod;
      }
    }


    return (int) ans;
  }
}
