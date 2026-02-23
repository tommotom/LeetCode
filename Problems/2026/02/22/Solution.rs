impl Solution {
    pub fn binary_gap(mut n: i32) -> i32 {
        let mut ans = 0;
        let mut seenAt = usize::MAX;
        let mut i = 0;
        while n > 0 {
            if n % 2 == 1 {
                if seenAt != usize::MAX {
                    ans = ans.max(i - seenAt);
                }
                seenAt = i;
            }
            n /= 2;
            i += 1;
        }
        ans as i32
    }
}
