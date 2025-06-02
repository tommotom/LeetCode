impl Solution {
    pub fn candy(ratings: Vec<i32>) -> i32 {
        let n = ratings.len();
        let mut arr: Vec<(usize, i32)> = Vec::new();
        for i in 0..n {
            arr.push((i, ratings[i]));
        }
        arr.sort_by(|a: &(usize, i32), b: &(usize, i32)| a.1.cmp(&b.1));

        let mut candies = vec![0; n];
        for (i, r) in arr {
            let mut num = 1;
            if i > 0 && ratings[i-1] < r {
                num = num.max(candies[i-1] + 1);
            }
            if i + 1 < n && ratings[i+1] < r {
                num = num.max(candies[i+1] + 1);
            }
            candies[i] = num;
        }
        candies.into_iter().sum()
    }
}
