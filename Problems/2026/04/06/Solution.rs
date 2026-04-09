use std::collections::HashSet;

impl Solution {
    pub fn robot_sim(commands: Vec<i32>, obstacles: Vec<Vec<i32>>) -> i32 {
        let obstacles: HashSet<(i32, i32)> = obstacles.into_iter().map(|obstacle| (obstacle[0], obstacle[1])).collect();
        let dirs = vec![[0, 1], [1, 0], [0, -1], [-1, 0]];
        let mut d = 0 as usize;
        let (mut x, mut y, mut ans) = (0, 0, 0);
        for command in commands {
            if command == -1 {
                d = (d + 1) % 4;
            } else if command == -2 {
                d = (d + 3) % 4;
            } else {
                for _ in 0..command {
                    let next_x = x + dirs[d][0];
                    let next_y = y + dirs[d][1];
                    let key = (next_x, next_y);
                    if obstacles.contains(&key) {
                        break;
                    }
                    x = next_x;
                    y = next_y;
                    ans = ans.max(x * x + y * y);
                }
            }
        }
        ans
    }
}
