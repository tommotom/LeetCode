impl Solution {
    pub fn max_absolute_sum(nums: Vec<i32>) -> i32 {
        let mut record = [0, 0];
        let mut cur = 0;
        let mut ans = 0;
        for num in nums {
            cur += num;
            ans = ans.max((cur - record[0]).abs());
            ans = ans.max((cur - record[1]).abs());
            record[0] = record[0].min(cur);
            record[1] = record[1].max(cur);
        }
        ans
    }
}
