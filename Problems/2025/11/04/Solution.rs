use std::collections::HashSet;

impl Solution {
    pub fn find_x_sum(nums: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        fn x_sum(counter: &Vec<usize>, x: usize) -> i32 {
            let mut arr = Vec::new();
            for i in 1..51 {
                if counter[i] > 0 {
                    arr.push([i, counter[i]]);
                }
            }
            arr.sort_by(|a, b| if a[1] == b[1] {b[0].cmp(&a[0])} else {b[1].cmp(&a[1])});
            let x_set: HashSet<usize> =  arr.iter().take(x).map(|num| num[0]).collect();
            arr.iter().filter(|num| x_set.contains(&num[0])).map(|num| (num[0] * num[1]) as i32).sum()
        }

        let k = k as usize;
        let x = x as usize;
        let nums: Vec<usize> = nums.iter().map(|num| *num as usize).collect();
        let mut counter = vec![0; 51];
        for i in 0..(k-1) {
            counter[nums[i]] += 1;
        }

        let mut ans = Vec::new();
        for i in (k-1)..nums.len() {
            counter[nums[i]] += 1;
            ans.push(x_sum(&counter, x));
            counter[nums[i-k+1]] -= 1;
        }

        ans
    }
}
