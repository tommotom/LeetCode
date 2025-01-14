impl Solution {
    pub fn find_the_prefix_common_array(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
        let mut ans = Vec::new();
        let mut freq = [0; 51];
        let mut count = 0;
        for i in 0..a.len() {
            let A = a[i] as usize;
            let B = b[i] as usize;
            freq[A] += 1;
            freq[B] += 1;
            if freq[A] == 2 {
                count += 1;
                freq[A] = 0;
            }
            if freq[B] == 2 {
                count += 1;
                freq[B] = 0;
            }
            ans.push(count);
        }
        ans
    }
}
