impl Solution {
    pub fn max_active_sections_after_trade(s: String) -> i32 {
        let n = s.len();
        let cnt1 = s.chars().filter(|&c| c == '1').count() as i32;

        let mut zero_blocks = Vec::new();
        let mut i = 0;
        let bytes = s.as_bytes();

        while i < n {
            let start = i;
            while i < n && bytes[i] == bytes[start] {
                i += 1;
            }
            if bytes[start] == b'0' {
                zero_blocks.push((i - start) as i32);
            }
        }

        let m = zero_blocks.len();
        if m < 2 {
            return cnt1;
        }

        let mut best_gain = 0; // Optimal Increment
        for j in 0..m - 1 {
            best_gain = best_gain.max(zero_blocks[j] + zero_blocks[j + 1]);
        }

        cnt1 + best_gain
    }
}
