impl Solution {
    pub fn max_sum_of_squares(mut num: i32, mut sum: i32) -> String {
        if 9 * num < sum {
            return "".to_string();
        }
        let mut ans = Vec::new();
        while num > 0 && sum > 0 {
            num -= 1;
            let n = sum.min(9);
            ans.push(n.to_string());
            sum -= n;
        }
        while num > 0 {
            ans.push('0'.to_string());
            num -= 1;
        }
        ans.join("")
    }
}
