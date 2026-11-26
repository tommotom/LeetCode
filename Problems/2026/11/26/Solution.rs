impl Solution {
    pub fn can_alice_win(mut n: i32) -> bool {
        let mut stones = 10;
        let mut is_alice = true;
        while n > 0 {
            if n < stones {
                return !is_alice;
            }
            n -= stones;
            stones -= 1;
            is_alice = !is_alice
        }
        !is_alice
    }
}
