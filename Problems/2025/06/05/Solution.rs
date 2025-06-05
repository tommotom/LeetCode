use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn smallest_equivalent_string(s1: String, s2: String, base_str: String) -> String {
        fn dfs(cur: usize, visited: &mut HashSet<usize>, graph: &Vec<HashSet<usize>>, minimum: &mut Vec<usize>) {
            if visited.contains(&cur) {
                return;
            }
            minimum[cur] = minimum[cur].min(cur);
            visited.insert(cur);
            for next in &graph[cur] {
                dfs(*next, visited, graph, minimum);
                minimum[cur] = minimum[cur].min(minimum[*next]);
            }
        }

        let s1_char: Vec<char> = s1.chars().collect();
        let s2_char: Vec<char> = s2.chars().collect();
        let mut graph = vec![HashSet::new(); 26];
        for i in 0..s1.len() {
            let c1 = s1_char[i] as usize - 'a' as usize;
            let c2 = s2_char[i] as usize - 'a' as usize;
            graph[c1].insert(c2);
            graph[c2].insert(c1);
        }
        let mut minimum = vec![26; 26];
        for i in 0..26 {
            let mut visited: HashSet<usize> = HashSet::new();
            dfs(i, &mut visited, &graph, &mut minimum);
        }
        base_str.chars().into_iter().map(|c| (minimum[c as usize - 'a' as usize] + 'a' as usize) as u8 as char).collect()
    }
}
