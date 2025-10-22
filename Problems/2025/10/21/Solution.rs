use std::collections::HashMap;

impl Solution {
    pub fn max_frequency(mut nums: Vec<i32>, k: i32, num_operations: i32) -> i32 {
        nums.sort_unstable();

        let fst = nums.iter().enumerate().map(|(i,&x)|(x,i)).rev().collect::<HashMap<i32, usize>>();
        let lst = nums.iter().enumerate().map(|(i,&x)|(x,i)).collect::<HashMap<i32, usize>>();

        let freq : HashMap::<i32, i32>  = nums.iter()
            .fold(HashMap::new(), |mut a, &x| {
                *a.entry(x).or_default() += 1;
                a});

        let mut best = 0;
        let n = nums.len();
        let mut vals = freq.keys().cloned().collect::<Vec<_>>();
        vals.sort_unstable();

        for target in nums[0]..=nums[n-1] {
            let a = match vals.binary_search(&(target - k))
            { Ok(i) | Err(i) => *fst.get(&vals[i]).unwrap()};
            let b = match vals.binary_search(&(target + k)) {
                Ok(i) => *lst.get(&vals[i]).unwrap(),
                Err(i) => *lst.get(&vals[i-1]).unwrap()};
            let mut fix = freq.get(&target).unwrap_or(&0);
            if b >= a {
                best = best.max(((b-a+1) as i32 -fix).min(num_operations)+fix);
            }

        }

        best
    }
}
