use std::collections::{BTreeSet, HashMap};

#[derive(Default)]
struct NumberContainers {
    map: HashMap<i32, i32>,
    sets: HashMap<i32, BTreeSet<i32>>,
}

impl NumberContainers {

    fn new() -> Self {
        Self::default()
    }

    fn change(&mut self, index: i32, number: i32) {
        if let Some(n) = self.map.insert(index, number) {
            self.sets.get_mut(&n).unwrap().remove(&index);
        }
        self.sets.entry(number).or_default().insert(index);
    }

    fn find(&mut self, number: i32) -> i32 {
        self.sets
            .get(&number)
            .and_then(BTreeSet::first)
            .map_or(-1, i32::to_owned)
    }
}
