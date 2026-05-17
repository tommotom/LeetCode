use std::collections::VecDeque;

impl Solution {
    pub fn can_reach(arr: Vec<i32>, start: i32) -> bool {
        let n = arr.len();
        let mut q: VecDeque<usize> = VecDeque::new();
        let mut visited = vec![false; n];
        q.push_back(start as usize);
        while q.len() > 0 {
            let i = q.pop_front().unwrap();
            if arr[i] == 0 {
                return true;
            }
            let back = i + arr[i] as usize;
            let front = i - arr[i] as usize;
            if back < n && !visited[back] {
                visited[back] = true;
                q.push_back(back);
            }
            if 0 <= front && front < n && !visited[front] {
                visited[front] = true;
                q.push_back(front);
            }
        }
        false
    }
}
