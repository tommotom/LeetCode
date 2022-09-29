class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int l = 0, r = arr.length;
        while(l < r) {
            int m = l + (r - l) / 2;
            if (arr[m] < x) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        l--;

        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            if (l < 0) {
                ans.add(arr[r]);
                r++;
            } else if (r == arr.length) {
                ans.add(arr[l]);
                l--;
            } else {
                if (Math.abs(arr[l]-x) > Math.abs(arr[r]-x)) {
                    ans.add(arr[r]);
                    r++;
                } else {
                    ans.add(arr[l]);
                    l--;
                }
            }
        }
        Collections.sort(ans);
        return ans;
    }
}
