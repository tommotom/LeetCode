use std::collections::HashMap;

impl Solution {
    pub fn first_complete_index(arr: Vec<i32>, mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = mat[0].len();
        let mut map = HashMap::new();
        for i in 0..m {
            for j in 0..n {
                map.insert(mat[i][j], (i, j));
            }
        }

        let mut row_count = vec![n; m];
        let mut col_count = vec![m; n];
        for i in 0..arr.len() {
            let (r, c) = map.get(&arr[i]).unwrap();
            row_count[*r] -= 1;
            col_count[*c] -= 1;
            if row_count[*r] == 0 || col_count[*c] == 0 {
                return i as i32;
            }
        }
        0
    }
}
