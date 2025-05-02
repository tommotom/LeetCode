impl Solution {
    pub fn push_dominoes(dominoes: String) -> String {
        let mut state: Vec<char> = dominoes.chars().collect();
        let mut q = Vec::new();
        for i in 0..state.len() {
            if state[i] != '.' {
                q.push(i);
            }
        }

        while q.len() > 0 {
            let mut next: Vec<(usize, char)> = Vec::new();
            for i in q {
                let n = next.len();
                if n > 0 && next[n-1].0 == i-1 && next[n-1].1 == 'R' && state[i] == 'L' {
                    next.pop();
                    continue;
                }
                if state[i] == 'L' && i > 0 && state[i-1] == '.'{
                    next.push((i-1, 'L'));
                } else if state[i] == 'R' && i+1 < state.len() && state[i+1] == '.' {
                    next.push((i+1, 'R'));
                }
            }
            for (i, dir) in &next {
                state[*i] = *dir;
            }
            q = next.into_iter().map(|a| a.0).collect();
        }
        state.iter().collect()
    }
}
