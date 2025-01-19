use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn trap_rain_water(height_map: Vec<Vec<i32>>) -> i32 {
        if height_map.is_empty() || height_map[0].is_empty() {
            return 0;
        }

        let rows = height_map.len();
        let cols = height_map[0].len();
        let mut visited = vec![vec![false; cols]; rows];
        let mut heap = BinaryHeap::new();
        let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)];

        for r in 0..rows {
            heap.push(Reverse((height_map[r][0], r, 0)));
            heap.push(Reverse((height_map[r][cols - 1], r, cols - 1)));
            visited[r][0] = true;
            visited[r][cols - 1] = true;
        }

        for c in 0..cols {
            heap.push(Reverse((height_map[0][c], 0, c)));
            heap.push(Reverse((height_map[rows - 1][c], rows - 1, c)));
            visited[0][c] = true;
            visited[rows - 1][c] = true;
        }

        let mut total_water_volume = 0;

        while let Some(Reverse((height, row, col))) = heap.pop() {
            for (dr, dc) in &directions {
                let new_row = row as isize + dr;
                let new_col = col as isize + dc;

                if new_row >= 0
                    && new_row < rows as isize
                    && new_col >= 0
                    && new_col < cols as isize
                {
                    let new_row = new_row as usize;
                    let new_col = new_col as usize;

                    if !visited[new_row][new_col] {
                        visited[new_row][new_col] = true;
                        let neighbor_height = height_map[new_row][new_col];

                        if neighbor_height < height {
                            total_water_volume += height - neighbor_height;
                        }

                        heap.push(Reverse((
                            neighbor_height.max(height),
                            new_row,
                            new_col,
                        )));
                    }
                }
            }
        }

        total_water_volume
    }
}
