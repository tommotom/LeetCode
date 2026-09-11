impl Solution {
    pub fn total_numbers(digits: Vec<i32>) -> i32 {
        let mut counter = vec![0; 10];
        for d in digits {
            counter[d as usize] += 1;
        }
        let mut ans = 0;
        for i in 1..=9 {
            if counter[i] == 0 {
                continue;
            }
            counter[i] -= 1;
            for j in 0..=9 {
                if counter[j] == 0 {
                    continue;
                }
                counter[j] -= 1;
                for k in 0..=8 {
                    if k % 2 == 1 || counter[k] == 0 {
                        continue;
                    }
                    ans += 1;
                }
                counter[j] += 1;
            }
            counter[i] += 1;
        }
        ans
    }
}
