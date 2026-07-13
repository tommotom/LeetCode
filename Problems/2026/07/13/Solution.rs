impl Solution {
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        let mut ans = Vec::new();
        for start in 1..10 {
            let mut d = start;
            let mut cur = 0;
            while d < 10 {
                cur *= 10;
                cur += d;
                if high < cur {
                    break;
                }
                if low <= cur {
                    ans.push(cur);
                }
                d += 1;
            }
        }
        ans.sort();
        ans
    }
}
