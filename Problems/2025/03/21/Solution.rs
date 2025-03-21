use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn find_all_recipes(recipes: Vec<String>, ingredients: Vec<Vec<String>>, mut supplies: Vec<String>) -> Vec<String> {
        let mut ingredientOf: HashMap<String, HashSet<String>> = HashMap::new();
        let mut indeg = HashMap::new();
        for i in 0..recipes.len() {
            for ingredient in &ingredients[i] {
                ingredientOf.entry(ingredient.clone()).or_insert(HashSet::new()).insert(recipes[i].clone());
            }
            indeg.insert(&recipes[i], ingredients[i].len());
        }

        let mut ans = Vec::new();
        while let Some(supply) = supplies.pop() {
            if let Some(recipes) = ingredientOf.get(&supply) {
                for recipe in recipes {
                    if let Some(count) = indeg.get_mut(recipe) {
                        *count -= 1;
                        if *count == 0 {
                            supplies.push(recipe.clone());
                            ans.push(recipe.clone());
                        }
                    }
                }
            }
        }
        ans
    }
}
