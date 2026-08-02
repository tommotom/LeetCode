use std::collections::HashMap;

impl Solution {
    pub fn stone_game(piles: Vec<i32>) -> bool {
        fn can_alice_win(alice: i32, bob: i32, l: usize, r: usize, piles: &Vec<i32>, memo: &mut HashMap<(i32, i32, usize, usize), bool>) -> bool {
            if l > r || r == usize::MAX {
                return alice > bob;
            }
            let key = (alice, bob, l, r);
            if !memo.contains_key(&key) {
                let res = !can_bob_win(alice + piles[l], bob, l + 1, r, piles, memo) || !can_bob_win(alice + piles[r], bob, l, r - 1, piles, memo);
                memo.insert(key, res);
            }
            *memo.get(&key).unwrap()
        }
        fn can_bob_win(alice: i32, bob: i32, l: usize, r: usize, piles: &Vec<i32>, memo: &mut HashMap<(i32, i32, usize, usize), bool>) -> bool {
            if l > r || r == usize::MAX {
                return bob > alice;
            }
            let key = (alice, bob, l, r);
            if !memo.contains_key(&key) {
                let res = !can_alice_win(alice, bob + piles[l], l + 1, r, piles, memo) && !can_alice_win(alice, bob + piles[r], l, r - 1, piles, memo);
                memo.insert(key, res);
            }
            *memo.get(&key).unwrap()
        }
        let mut memo = HashMap::new();
        can_alice_win(0, 0, 0, piles.len()-1, &piles, &mut memo)
    }
}
