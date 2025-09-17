use std::collections::{HashMap, BTreeSet};
use std::cmp::Ordering;

#[derive(Debug, Clone, PartialEq, Eq)]
struct FoodItem {
    name: String,
    rating: i32,
}

impl PartialOrd for FoodItem {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for FoodItem {
    fn cmp(&self, other: &Self) -> Ordering {
        match other.rating.cmp(&self.rating) {
            Ordering::Equal => self.name.cmp(&other.name),
            other_ord => other_ord,
        }
    }
}

pub struct FoodRatings {
    food_to_info: HashMap<String, (String, i32)>,
    cuisine_to_foods: HashMap<String, BTreeSet<FoodItem>>,
}

impl FoodRatings {
    pub fn new(foods: Vec<String>, cuisines: Vec<String>, ratings: Vec<i32>) -> Self {
        let mut food_to_info = HashMap::new();
        let mut cuisine_to_foods: HashMap<String, BTreeSet<FoodItem>> = HashMap::new();

        for ((food, cuisine), rating) in foods.into_iter().zip(cuisines).zip(ratings) {
            food_to_info.insert(food.clone(), (cuisine.clone(), rating));

            cuisine_to_foods
                .entry(cuisine)
                .or_insert_with(BTreeSet::new)
                .insert(FoodItem {
                    name: food,
                    rating,
                });
        }

        Self {
            food_to_info,
            cuisine_to_foods,
        }
    }

    pub fn change_rating(&mut self, food: String, new_rating: i32) {
        if let Some((cuisine, old_rating)) = self.food_to_info.get_mut(&food) {
            if let Some(food_set) = self.cuisine_to_foods.get_mut(cuisine) {
                food_set.remove(&FoodItem {
                    name: food.to_string(),
                    rating: *old_rating,
                });

                food_set.insert(FoodItem {
                    name: food.to_string(),
                    rating: new_rating,
                });
            }

            *old_rating = new_rating;
        }
    }

    pub fn highest_rated(&self, cuisine: String) -> String {
        self.cuisine_to_foods
            .get(&cuisine)
            .unwrap()
            .iter()
            .next()
            .map(|item| item.name.clone())
            .unwrap()
    }
}
