impl Solution {
    pub fn num_subseq(mut n: Vec<i32>, t: i32) -> i32 {
        let (M, mut c, mut j) = (1_000_000_007, 0, n.len());
        n.sort_unstable(); let mut f = vec![0; n.len() + 2]; f[1] = 1;
        for (i, x) in n.iter().enumerate() {
            f[i + 2] = (f[i + 1] * 2) % M;
            while j > 0 && x + n[j - 1] > t { j -= 1 }
            if i + 1 >= j { c = (c + f[i + 1 - j]) % M }
        } (f[n.len() + 1] - c - 1 + M) % M
    }
}
