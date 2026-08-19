impl Solution {
    pub fn stone_game_ii(piles: Vec<i32>) -> i32 {
        let total_piles = piles.len();
        let mut suffix_sums = vec![0; total_piles + 1];
        for i in (0..total_piles).rev() {
            suffix_sums[i] = suffix_sums[i + 1] + piles[i];
        }

        let mut memo = vec![vec![0; total_piles + 1]; total_piles];

        fn max_stones_alice_can_get(m: usize, current_pile: usize, suffix_sums: &Vec<i32>, memo: &mut Vec<Vec<i32>>) -> i32 {
            let total_piles = suffix_sums.len() - 1;

            if current_pile >= total_piles {
                return 0;
            }

            if current_pile + 2 * m >= total_piles {
                return suffix_sums[current_pile];
            }

            if memo[current_pile][m] != 0 {
                return memo[current_pile][m];
            }

            let mut max_stones = 0;

            for x in 1..=2*m {
                let current_stones = suffix_sums[current_pile] - max_stones_alice_can_get(m.max(x), current_pile + x, suffix_sums, memo);
                max_stones = max_stones.max(current_stones);
            }

            memo[current_pile][m] = max_stones;
            max_stones
        }

        max_stones_alice_can_get(1, 0, &suffix_sums, &mut memo)
    }
}
