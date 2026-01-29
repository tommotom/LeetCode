impl Solution {
    pub fn minimum_cost(source: String, target: String, original: Vec<char>, changed: Vec<char>, cost: Vec<i32>) -> i64 {
        let (mut source, mut target) = (source.chars(), target.chars());

        use std::collections::{BinaryHeap, HashMap};
        let adj_graph = {
            let mut graph: HashMap<char, Vec<(char, i32)>> = HashMap::new();
            for i in 0..cost.len() {
                graph
                    .entry(original[i])
                    .and_modify(|v| v.push((changed[i], cost[i])))
                    .or_insert(vec![(changed[i], cost[i])]);
            }
            graph
        };

        fn dijkstra_from<'a>(from: char, cost: &'a mut HashMap<char, HashMap<char, i32>>, adj_graph: &HashMap<char, Vec<(char, i32)>>) -> &'a HashMap<char, i32> {
            cost.entry(from).or_insert({
                let (mut cost_to, mut visited) = (HashMap::new(), BinaryHeap::new());

                cost_to.entry(from).or_insert(0);
                visited.push((0, from));

                while !visited.is_empty() {
                    let (cost_at, c) = {
                        let (cost, c) = visited.pop().unwrap();
                        (-cost, c)
                    };
                    if cost_at > cost_to[&c] {
                        continue;
                    }

                    if let Some(neighbors) = adj_graph.get(&c) {
                        for (neighbor, cost_to_neighbor) in neighbors {
                            let new_cost = cost_at + *cost_to_neighbor;
                            if let Some(old_cost) = cost_to.get_mut(neighbor) {
                                if *old_cost <= new_cost {
                                    continue;
                                }
                                *old_cost = new_cost;
                            } else {
                                cost_to.insert(*neighbor, new_cost);
                            }
                            visited.push((-cost_to[neighbor], *neighbor));
                        }
                    }
                }

                cost_to
            })
        }

        let (mut cost, mut min_cost) = (HashMap::new(), 0);
        let (cached_source, cache) = (&mut [false; 26], &mut [[None; 26]; 26]);
        loop {
            match (source.next(), target.next()) {
                (Some(s), Some(t)) => {
                    if s == t {
                        continue;
                    }
                    let (si, ti) = (s as usize - 'a' as usize, t as usize - 'a' as usize);
                    if !cached_source[si] {
                        let cost_from_s = dijkstra_from(s, &mut cost, &adj_graph);
                        for (to, cost) in cost_from_s {
                            cache[si][*to as usize - 'a' as usize] = Some(*cost);
                        }
                        cached_source[si] = true;
                    }
                    if let Some(cost) = cache[si][ti] {
                        min_cost += cost as i64;
                    } else {
                        return -1;
                    }
                }
                (None, None) => break,
                _ => unsafe { core::hint::unreachable_unchecked() },
            }
        }

        min_cost
    }
}
