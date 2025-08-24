impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let mut arr = Vec::new();
        let mut count = 0;
        for num in nums {
            if num == 0 {
                if count > 0 {
                    arr.push(count);
                    count = 0;
                } else {
                    arr.push(0);
                }
            } else {
                count += 1;
            }
        }
        if count > 0 {
            arr.push(count);
        }
        let mut ans = if arr.len() > 0 {0.max(arr[0] - 1)} else {0};
        for i in 1.. arr.len() {
            ans = ans.max(arr[i-1] + arr[i]);
        }
        ans
    }
}
