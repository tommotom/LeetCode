impl Solution {
    pub fn number_of_beams(bank: Vec<String>) -> i32 {
        let counts: Vec<i32> = bank
            .iter()
            .map(|s| s.chars().filter(|&c| c == '1').count() as i32)
            .filter(|&count| count > 0)
            .collect();

        counts.windows(2)
            .map(|pair| pair[0] * pair[1])
            .sum()
    }
}
