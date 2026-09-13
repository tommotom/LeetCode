impl Solution {
    pub fn largest_overlap(img1: Vec<Vec<i32>>, img2: Vec<Vec<i32>>) -> i32 {
        let n = img1.len() as i32;
        let mut ans = 0;
        for dx in -(n-1)..n {
            for dy in -(n-1)..n {
                let mut count = 0;
                for r in 0..n {
                    let i = r + dx;
                    if i < 0 || i >= n {
                        continue;
                    }
                    for c in 0..n {
                        let j = c + dy;
                        if j < 0 || j >= n {
                            continue;
                        }
                        if img1[i as usize][j as usize] == 1 && img2[r as usize][c as usize] == 1 {
                            count += 1;
                        }
                    }
                }
                ans = ans.max(count);
            }
        }
        ans
    }
}
