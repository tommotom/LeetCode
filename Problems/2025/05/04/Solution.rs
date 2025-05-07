impl Solution {
    pub fn num_equiv_domino_pairs(dominoes: Vec<Vec<i32>>) -> i32 {
        let mut counter = vec![0; 100];
        let mut ans = 0;
        for domino in dominoes {
            let a = domino[0];
            let b = domino[1];
            let i = (10 * a.max(b) + a.min(b)) as usize;
            ans += counter[i];
            counter[i] += 1;
        }
        ans
    }
}
