impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        let mut sub1 = 0;
        let mut last1 = 0;
        let mut sub2 = 0;
        let mut last2 = 1;
        let mut sub3 = 0;
        let mut sub4 = 0;
        for num in nums {
            let m = num % 2;
            if last1 != m {
                sub1 += 1;
                last1 = m;
            }
            if last2 != m {
                sub2 += 1;
                last2 = m;
            }
            if m == 0 {
                sub3 += 1;
            }
            if m == 1 {
                sub4 += 1;
            }
        }
        sub1.max(sub2).max(sub3).max(sub4)
    }
}
