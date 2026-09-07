impl Solution {
    pub fn distinct_subseq_ii(s: String) -> i32 {
        const q: i64 = 1_000_000_007;
        s.chars().fold((0_i64, [0i64; 26]), |(mut total, mut last), c| {
            let i = (c as u8 - b'a') as usize;
            (total, last[i]) = ((total * 2 + 1 - last[i] + q) % q, (total + 1) % q);
            (total, last)
        }).0 as _
    }
}
