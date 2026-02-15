impl Solution {
    pub fn champagne_tower(poured: i32, query_row: i32, query_glass: i32) -> f64 {
        let poured = poured as f64;
        let query_row = query_row as usize;
        let query_glass = query_glass as usize;
        let mut glasses = Vec::new();
        glasses.push(vec![poured]);
        for row in 0..query_row+1 {
            let mut next = vec![0.0; row + 2];
            for i in 0..glasses[row].len() {
                let excess = if glasses[row][i] > 1.0 { glasses[row][i] - 1.0 } else { 0.0 };
                if glasses[row][i] > 1.0 {
                    glasses[row][i] = 1.0;
                }
                next[i] += excess / 2.0;
                next[i+1] += excess / 2.0;
            }
            glasses.push(next);
        }

        glasses[query_row][query_glass]
    }
}
