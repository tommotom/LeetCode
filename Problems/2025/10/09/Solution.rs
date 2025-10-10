use std::cmp::max;

impl Solution {
    pub fn min_time(skill: Vec<i32>, mana: Vec<i32>) -> i64 {
        let wizard_count = skill.len();
        let potion_count = mana.len();
        let mut done_time = vec![0i64; wizard_count + 1];
        let skill = skill.iter().map(|&x| i64::from(x)).collect::<Vec<i64>>();
        let mana = mana.iter().map(|&x| i64::from(x)).collect::<Vec<i64>>();
        for potion_idx in 0..potion_count {
            for wizard_idx in 0..wizard_count {
                done_time[wizard_idx + 1] = max(done_time[wizard_idx], done_time[wizard_idx + 1])
                    + skill[wizard_idx] * mana[potion_idx];
            }
            for wizard_idx in (0..wizard_count).rev() {
                done_time[wizard_idx] =
                    done_time[wizard_idx + 1] - mana[potion_idx] * skill[wizard_idx];
            }
        }
        *done_time.last().unwrap()
    }
}
