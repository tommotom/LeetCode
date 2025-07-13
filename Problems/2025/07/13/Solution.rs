impl Solution {
    pub fn match_players_and_trainers(mut players: Vec<i32>, mut trainers: Vec<i32>) -> i32 {
        players.sort();
        trainers.sort();
        let mut ans = 0;
        let mut i = 0;
        for trainer in trainers {
            if i < players.len() && players[i] <= trainer {
                ans += 1;
                i += 1;
            }
        }
        ans
    }
}
