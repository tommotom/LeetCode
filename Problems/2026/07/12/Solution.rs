impl Solution {
    pub fn array_rank_transform(arr: Vec<i32>) -> Vec<i32> {
        let mut a = Vec::new();
        for (i, x) in arr.iter().enumerate() {
            a.push((x, i));
        }
        a.sort();
        let mut rank = vec![0; arr.len()];
        let mut r = 0;
        let mut last = i32::MIN;
        for (x, i) in a {
            if last < *x {
                r += 1;
            }
            last = *x;
            rank[i] = r;
        }
        rank
    }
}
