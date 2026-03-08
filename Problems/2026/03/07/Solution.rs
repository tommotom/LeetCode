impl Solution {
    pub fn min_flips(s: String) -> i32 {
        let s = s.as_bytes();
        let n = s.len();

        // number of flips to make s[1..i] alternating
        let mut prefix_dist = Vec::with_capacity(n+1);
        prefix_dist.push([0; 2]);

        // number of flips to make s[n..i] alternating
        let mut suffix_dist = Vec::with_capacity(n+1);
        suffix_dist.push([0; 2]);

        for (i, c) in s.iter().enumerate() {
            let mut moves_to_one = if *c == ('0' as u8) { 1 } else { 0 };
            let mut moves_to_zero = 1 - moves_to_one;
            prefix_dist.push([
                prefix_dist[i][0] + if i%2 == 0 { moves_to_zero } else { moves_to_one },
                prefix_dist[i][1] + if i%2 == 0 { moves_to_one } else { moves_to_zero },
            ]);

            let suff_len = i + 1;
            moves_to_one = if s[n-suff_len] == ('0' as u8) { 1 } else { 0 };
            moves_to_zero = 1 - moves_to_one;
            suffix_dist.push([
                suffix_dist[i][1] + moves_to_zero,
                suffix_dist[i][0] + moves_to_one,
            ]);
        }

        let mut min = i32::MAX;
        for split_pos in 0..=n {
            // find answer for join s[i..] + s[..i]
            let left = suffix_dist[n-split_pos];
            let mut right = prefix_dist[split_pos];

            let best_in_split = std::cmp::min(
                left[(n-split_pos)%2] + right[0],
                left[1-(n-split_pos)%2] + right[1],
            );

            min = std::cmp::min(min, best_in_split)
        }

        return min;
    }
}
