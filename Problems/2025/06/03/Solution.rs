impl Solution {
    pub fn max_candies(mut status: Vec<i32>, candies: Vec<i32>, keys: Vec<Vec<i32>>, contained_boxes: Vec<Vec<i32>>, initial_boxes: Vec<i32>) -> i32 {
        let n = status.len();

        let mut found_box = vec![false; n];
        for i in &initial_boxes {
            found_box[*i as usize] = true
        }

        let mut found_key = vec![false; n];
        for i in 0..n {
            if status[i] == 1 {
                found_key[i] = true;
            }
        }

        let mut q = initial_boxes.clone();
        let mut ans = 0;
        while q.len() > 0 {
            let i = q.pop().unwrap() as usize;
            if (status[i] == 0 && !found_key[i]) || status[i] == 2 {
                continue;
            }
            ans += candies[i];
            status[i] = 2;
            for j in &contained_boxes[i] {
                found_box[*j as usize] = true;
                if found_key[*j as usize] {
                    q.push(*j);
                }
            }

            for j in &keys[i] {
                found_key[*j as usize] = true;
                if found_box[*j as usize] {
                    q.push(*j);
                }
            }
        }
        ans
    }
}
