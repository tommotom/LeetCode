use std::collections::{HashMap, HashSet, VecDeque};
use std::cmp::Ordering;

#[derive(Debug, Clone, Hash, PartialEq, Eq)]
struct Packet {
    source: i32,
    destination: i32,
    timestamp: i32
}

struct Router {
    destination_queue: HashMap<i32, VecDeque<Packet>>,
    queue: VecDeque<Packet>,
    set: HashSet<Packet>,
    capacity: i32
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Router {

    fn new(memoryLimit: i32) -> Self {
        Self {
            destination_queue: HashMap::new(),
            queue: VecDeque::new(),
            set: HashSet::new(),
            capacity: memoryLimit
        }
    }

    fn add_packet(&mut self, source: i32, destination: i32, timestamp: i32) -> bool {
        let packet = Packet {
            source,
            destination,
            timestamp
        };
        if self.set.contains(&packet) {
            return false;
        }
        self.destination_queue.entry(destination).or_insert(VecDeque::new()).push_back(packet.clone());
        self.queue.push_back(packet.clone());
        self.set.insert(packet);
        self.capacity -= 1;
        if self.capacity < 0 {
            self.forward_packet();
        }
        true
    }

    fn forward_packet(&mut self) -> Vec<i32> {
        if let Some(packet) = self.queue.pop_front() {
            self.destination_queue.get_mut(&packet.destination).unwrap().pop_front();
            self.set.remove(&packet);
            self.capacity += 1;
            return vec![packet.source, packet.destination, packet.timestamp];
        } else {
            return Vec::new();
        }
    }

    fn get_count(&self, destination: i32, start_time: i32, end_time: i32) -> i32 {
        if !self.destination_queue.contains_key(&destination) {
            return 0
        }
        let queue = self.destination_queue.get(&destination).unwrap();
        self.search(queue, end_time+1) - self.search(queue, start_time)
    }

    fn search(&self, queue: &VecDeque<Packet>, time: i32) -> i32 {
        let (mut l, mut r) = (0, queue.len());
        while l < r {
            let m = l + (r - l) / 2;
            let t = queue.get(m).unwrap().timestamp;
            if t < time {
                l = m + 1;
            } else {
                r = m;
            }
        }
        l as i32
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * let obj = Router::new(memoryLimit);
 * let ret_1: bool = obj.add_packet(source, destination, timestamp);
 * let ret_2: Vec<i32> = obj.forward_packet();
 * let ret_3: i32 = obj.get_count(destination, startTime, endTime);
 */
