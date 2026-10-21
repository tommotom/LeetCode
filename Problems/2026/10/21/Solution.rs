impl Solution {
    pub fn min_operations(s: String) -> i32 {
        let s_vec: Vec<char> = s.chars().collect();
        let mut target: Vec<char> = s_vec.clone();
        target.sort();
        if s_vec == target {
            return 0;
        }
        if s.len() == 2 {
            return -1;
        }
        let n = s_vec.len();
        if s_vec[0] == target[0] || s_vec[n-1] == target[n-1] {
            return 1;
        }
        if s_vec.iter().take(n-1).any(|&c| c == target[0]) || s_vec.iter().rev().take(n-1).any(|&c| c == target[n-1]) {
            return 2;
        }
        3
    }
}
