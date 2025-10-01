impl Solution {
    pub fn num_water_bottles(mut num_bottles: i32, num_exchange: i32) -> i32 {
        let mut ans = 0;
        let mut empty = 0;
        while num_bottles > 0 {
            ans += num_bottles;
            empty += num_bottles;
            num_bottles = empty / num_exchange;
            empty %= num_exchange;
        }
        ans
    }
}
