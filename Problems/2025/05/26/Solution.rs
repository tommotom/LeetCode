impl Solution {
    pub fn largest_path_value(colors: String, edges: Vec<Vec<i32>>) -> i32 {
        let n = colors.len();
        let mut adj = vec![vec![]; n];
        edges.iter().for_each(|edge| adj[edge[0] as usize].push(edge[1] as usize));

        let mut count = vec![[0; 26]; n];
        let mut visited = vec![false; n];
        let mut in_stack = vec![false; n];
        let colors: Vec<char> = colors.chars().collect();
        let ans = (0..n).fold(0, |acc, i| acc.max(Self::dfs(i, &colors, &adj, &mut count, &mut visited, &mut in_stack)));

        if ans == i32::MAX { -1 } else { ans }
    }

    fn dfs(node: usize, colors: &Vec<char>, adj: &Vec<Vec<usize>>, count: &mut Vec<[i32; 26]>, visited: &mut Vec<bool>, in_stack: &mut Vec<bool>) -> i32 {
        if in_stack[node] { return i32::MAX };
        if visited[node] { return count[node][colors[node] as usize - 97] };

        visited[node] = true;
        in_stack[node] = true;

        for &neighbor in adj[node].iter() {
            if Self::dfs(neighbor, colors, adj, count, visited, in_stack) == i32::MAX {
                return i32::MAX;
            }
            (0..26).for_each(|i| count[node][i] = count[node][i].max(count[neighbor][i]));
        }

        in_stack[node] = false;
        count[node][colors[node] as usize - 97] += 1;
        return count[node][colors[node] as usize - 97];
    }
}
