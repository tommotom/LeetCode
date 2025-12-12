use std::collections::VecDeque;

impl Solution {
    pub fn count_mentions(n: i32, mut events: Vec<Vec<String>>) -> Vec<i32> {
        let n = n as usize;
        let mut events :Vec<(String, i32, String)> = events.iter().map(|e| (e[0].clone(), e[1].parse::<i32>().unwrap(), e[2].clone())).collect();
        events.sort_by(|a, b| if a.1 != b.1 {a.1.cmp(&b.1)} else {b.0.cmp(&a.0)});
        println!("{:?}", events);
        let mut ans = vec![0; n];
        let mut q: VecDeque<(i32, usize)> = VecDeque::new();
        let mut isOnline = vec![true; n];
        for event in events {
            let t = event.1;
            while q.len() > 0 && q[0].0 <= t {
                let tmp = q.pop_front().unwrap();
                isOnline[tmp.1] = true;
            }
            if event.0 == "MESSAGE" {
                if event.2 == "ALL" {
                    for i in 0..n {
                        ans[i] += 1;
                    }
                } else if event.2 == "HERE" {
                    for i in 0..n {
                        if isOnline[i] {
                            ans[i] += 1;
                        }
                    }
                } else {
                    for id in event.2.split(' ') {
                        if let Some(num_str) = id.strip_prefix("id") {
                            if let Ok(i) = num_str.parse::<usize>() {
                                ans[i] += 1;
                            }
                        }
                    }
                }
            } else {
                let i = event.2.parse::<usize>().unwrap();
                q.push_back((t + 60, i));
                isOnline[i] = false;
            }
        }
        ans
    }
}
