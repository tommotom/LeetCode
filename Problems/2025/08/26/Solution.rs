impl Solution {
    pub fn area_of_max_diagonal(dimensions: Vec<Vec<i32>>) -> i32 {
        let (mut max, mut area) = (0, 0);
        for d in dimensions {
            let diagonal = d[0] * d[0] + d[1] * d[1];
            if max < diagonal {
                max = diagonal;
                area = d[0] * d[1];
            } else if max == diagonal {
                area = area.max(d[0] * d[1]);
            }
        }
        area
    }
}
