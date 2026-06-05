impl Solution {
    pub fn total_waviness(num1: i32, num2: i32) -> i32 {
        fn waviness(num: i32) -> i32 {
            let arr: Vec<char> = num.to_string().chars().collect();
            let mut ret = 0;
            for i in 1..(arr.len()-1) {
                if arr[i-1] < arr[i] && arr[i] > arr[i+1] {
                    ret += 1;
                } else if arr[i-1] > arr[i] && arr[i] < arr[i+1] {
                    ret += 1;
                }
            }
            ret
        }
        let mut ans = 0;
        for num in num1..=num2 {
            ans += waviness(num);
        }
        ans
    }
}
