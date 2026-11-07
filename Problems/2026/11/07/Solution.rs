use std::collections::BinaryHeap;
use std::cmp::{Ordering, Reverse};

#[derive(Copy, Clone, Eq, PartialEq)]
struct Server {
    index: usize,
    weight: i32,
}

impl Ord for Server {
    fn cmp(&self, other: &Self) -> Ordering {
        if self.weight == other.weight {
            return other.index.cmp(&self.index);
        }
        other.weight.cmp(&self.weight)
    }
}

impl PartialOrd for Server {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}


impl Solution {
    pub fn assign_tasks(servers: Vec<i32>, tasks: Vec<i32>) -> Vec<i32> {
        let mut free: BinaryHeap<Server> = BinaryHeap::new();
        for (index, weight) in servers.into_iter().enumerate() {
            free.push(Server {index, weight});
        }
        let mut using: BinaryHeap<Reverse<(usize, Server)>> = BinaryHeap::new();
        let mut ans = Vec::new();
        let mut cur = 0;
        for j in 0..tasks.len() {
            cur = cur.max(j);
            if free.len() == 0 && using.peek().unwrap().0.0 > cur {
                cur = using.peek().unwrap().0.0;
            }
            while using.len() > 0 && using.peek().unwrap().0.0 <= cur {
                let (_, server) = using.pop().unwrap().0;
                free.push(server);
            }
            let server = free.pop().unwrap();
            ans.push(server.index as i32);
            let tmp = (cur + tasks[j] as usize, server);
            using.push(Reverse(tmp));
        }
        ans
    }
}
