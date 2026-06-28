impl Solution {
    pub fn maximum_element_after_decrementing_and_rearranging(mut arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let mut counts = vec![0; n+1];
        for num in arr {
            counts[n.min(num as usize)] += 1;
        }

        let mut ans = 1;
        for num in 2..=n {
            ans = (num as i32).min(ans + counts[num]);
        }
        ans
    }
}
