impl Solution {
    pub fn min_operations(grid: Vec<Vec<i32>>, x: i32) -> i32 {
        let mut arr = Vec::new();
        for row in grid {
            for num in row {
                arr.push(num);
            }
        }
        arr.sort();

        for i in 1..arr.len() {
            if (arr[i] - arr[i-1]) % x != 0 {
                return -1;
            }
        }

        let mut ans = i32::MAX;
        let mut l = 0;
        let mut r: i32 = arr.iter().sum();
        for i in 0..arr.len() {
            r -= arr[i];
            let r_num = (r - arr[i] * (arr.len()-i-1) as i32) / x;
            let l_num = (arr[i] * i as i32 - l) / x;
            ans = ans.min(r_num + l_num);
            l += arr[i];
        }
        ans
    }
}
