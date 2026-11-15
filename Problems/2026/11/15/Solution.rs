impl Solution {
    pub fn num_of_subarrays(arr: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut sum = 0;
        let (mut odd, mut even) = (0, 1);
        for num in arr {
            sum += num;
            if sum % 2 == 0 {
                even += 1;
                ans += odd;
            } else {
                odd += 1;
                ans += even;
            }
            ans %= 1000000007;
        }
        ans
    }
}
