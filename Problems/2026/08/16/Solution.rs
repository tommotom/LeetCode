impl Solution {
    pub fn stone_game_ix(stones: Vec<i32>) -> bool {
        let mut count = [0i32; 3];
        for stone in stones {
            count[(stone % 3) as usize] += 1;
        }

        if count[1] == 0 || count[2] == 0 {
            return count[1].max(count[2]) > 2 && count[0] % 2 == 1;
        }

        (count[1] - count[2]).abs() > 2 || count[0] % 2 == 0
    }
}
