impl Solution {
    pub fn num_of_subarrays(arr: Vec<i32>) -> i32 {
        let mut count = [1, 0];
        let mut sum = 0;
        let mut ans = 0;
        for num in arr {
            sum = (sum + num) % 2;
            ans = (ans + count[(sum^1) as usize]) % 1000000007;
            count[sum as usize] += 1;
        }
        ans
    }
}
