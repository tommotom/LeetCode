impl Solution {
    pub fn remove_subfolders(folder: Vec<String>) -> Vec<String> {
        let mut folders = folder;
        folders.sort();

        let mut ans = vec![folders[0].clone()];

        for i in 1..folders.len() {
            let last_folder = ans.last().unwrap().clone() + "/";
            if !folders[i].starts_with(&last_folder) {
                ans.push(folders[i].clone());
            }
        }

        ans
    }
}
