impl Solution {
    pub fn construct_distanced_sequence(n: i32) -> Vec<i32> {
        let n = n as usize;
        let mut seq = vec![0; 2*n - 1];
        let mut used = vec![false; n+1];
        Self::backtrack(&mut seq, &mut used, 0, n);
        seq
    }

    fn backtrack(seq: &mut Vec<i32>, used: &mut Vec<bool>, mut start: usize, n: usize) -> bool {
        while start < seq.len() && seq[start] != 0 {
            start += 1;
        }
        if start >= seq.len() {
            return true;
        }

        for i in (1..=n).rev() {
            if !used[i] {
                if i == 1 {
                    seq[start] = 1;
                    used[1] = true;
                    if Self::backtrack(seq, used, start + 1, n) {
                        return true;
                    }
                    seq[start] = 0;
                    used[1] = false;
                } else {
                    let j = start + i;
                    if j < seq.len() && seq[j] == 0 {
                        seq[start] = i as i32;
                        seq[j] = i as i32;
                        used[i] = true;

                        if Self::backtrack(seq, used, start + 1, n) {
                            return true;
                        }
                        seq[start] = 0;
                        seq[j] = 0;
                        used[i] = false;
                    }
                }
            }
        }

        false
    }
}
