use std::{
    cmp::{Ordering, Reverse},
    collections::BinaryHeap,
};

#[derive(Debug, PartialEq, Eq)]
struct Event {
    end_time: i32,
    value: i32,
}

impl Event {
    fn new(end_time: i32, value: i32) -> Self {
        Self {
            end_time: end_time,
            value: value,
        }
    }
}

impl PartialOrd for Event {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(&other))
    }
}

impl Ord for Event {
    fn cmp(&self, other: &Self) -> Ordering {
        other.end_time.cmp(&self.end_time)
    }
}

impl Solution {
    pub fn max_two_events(mut events: Vec<Vec<i32>>) -> i32 {
        events.sort_by(|a, b| a[0].cmp(&b[0]));
        let mut q: BinaryHeap<Event> = BinaryHeap::new();
        let mut max = 0;
        let mut ans = 0;
        for event in events {
            while q.len() > 0 && q.peek().unwrap().end_time < event[0] {
                let e = q.pop().unwrap();
                max = max.max(e.value);
            }
            ans = ans.max(event[2] + max);
            q.push(Event::new(event[1], event[2]));
        }
        ans
    }
}
