use std::cmp::Ordering;
impl Solution {
    pub fn stone_game_iii(stone_value: Vec<i32>) -> String {
        let n = stone_value.len();

        let alice_minus_bob = (0..n)
        .rev()
        .fold([0; 3], |net_scores, i| {
            let new_net_score = (0..3)
            .map(|j| stone_value[i..].iter().take(j+1).sum::<i32>() - net_scores[j])
            .max()
            .unwrap();

            [new_net_score, net_scores[0], net_scores[1]]
        })[0];

        match alice_minus_bob {
            0 => "Tie",
            x if x > 0 => "Alice",
            _ => "Bob"
        }.into()
    }
}
