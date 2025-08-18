use itertools::Itertools;

impl Solution {
    pub fn reordered_power_of2(n: i32) -> bool {
        let chars = n.to_string().chars().collect::<Vec<char>>();
        for order in (0..chars.len()).permutations(chars.len()) {
            if chars[order[0]] == '0' {
                continue;
            }
            let mut num: i32 = order.into_iter().map(|i| chars[i]).collect::<String>().parse().unwrap();
            let mut valid = true;
            while num > 1 {
                if num % 2 == 1 {
                    valid = false;
                    break;
                }
                num /= 2;
            }
            if valid && num == 1 {
                return true;
            }
        }
        false
    }
}
