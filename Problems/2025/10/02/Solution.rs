impl Solution {
    pub fn max_bottles_drunk(mut num_bottles: i32, mut num_exchange: i32) -> i32 {
        let mut empty = 0;
        let mut ans = 0;
        while num_bottles > 0 {
            empty += num_bottles;
            ans += num_bottles;
            num_bottles = 0;
            while empty >= num_exchange {
                empty -= num_exchange;
                num_exchange += 1;
                num_bottles += 1;
            }
        }
        ans
    }
}
