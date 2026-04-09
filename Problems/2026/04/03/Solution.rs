use std::collections::HashMap;

impl Solution {
    pub fn max_walls(robots: Vec<i32>, distance: Vec<i32>, walls: Vec<i32>) -> i32 {
        let n = robots.len();

        let mut robots_to_distance: HashMap<i32, i32> = HashMap::new();
        for i in 0..n {
            robots_to_distance.insert(robots[i], distance[i]);
        }

        let mut sorted_robots = robots.clone();
        sorted_robots.sort();
        let mut sorted_walls = walls.clone();
        sorted_walls.sort();

        let mut left = vec![0; n];
        let mut right = vec![0; n];
        let mut num = vec![0; n];

        for i in 0..n {
            let pos1 = sorted_walls.partition_point(|&x| x <= sorted_robots[i]);

            let left_pos = if i >= 1 {
                sorted_walls.partition_point(|&x|
                    x < (sorted_robots[i] - robots_to_distance[&sorted_robots[i]]).max(sorted_robots[i - 1] + 1))
            } else {
                sorted_walls.partition_point(|&x|
                    x < sorted_robots[i] - robots_to_distance[&sorted_robots[i]])
            };
            left[i] = pos1 - left_pos;

            let right_pos = if i < n - 1 {
                sorted_walls.partition_point(|&x|
                    x <= (sorted_robots[i] + robots_to_distance[&sorted_robots[i]]).min(sorted_robots[i + 1] - 1))
            } else {
                sorted_walls.partition_point(|&x|
                    x <= sorted_robots[i] + robots_to_distance[&sorted_robots[i]])
            };

            let pos2 = sorted_walls.partition_point(|&x| x < sorted_robots[i]);
            right[i] = right_pos - pos2;

            if i == 0 {
                continue;
            }

            let pos3 = sorted_walls.partition_point(|&x| x < sorted_robots[i - 1]);
            num[i] = pos1 - pos3;
        }

        let mut sub_left = left[0];
        let mut sub_right = right[0];

        for i in 1..n {
            let current_left = (sub_left + left[i]).max(
                sub_right - right[i - 1] + (left[i] + right[i - 1]).min(num[i])
            );
            let current_right = (sub_left + right[i]).max(sub_right + right[i]);
            sub_left = current_left;
            sub_right = current_right;
        }

        sub_left.max(sub_right) as i32
    }
}
