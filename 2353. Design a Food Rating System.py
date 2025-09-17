Design a food rating system that can do the following:
Modify the rating of a food item listed in the system.
Return the highest-rated food item for a type of cuisine in the system.
Implement the FoodRatings class:
FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
foods[i] is the name of the ith food,
cuisines[i] is the type of cuisine of the ith food, and
ratings[i] is the initial rating of the ith food.
void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.
Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

 import java.util.*;

public class FoodRatings {
    // Maps food name to its rating
    private Map<String, Integer> foodToRating;
    // Maps food name to its cuisine
    private Map<String, String> foodToCuisine;
    // Maps cuisine to a TreeSet of foods sorted by rating and name
    private Map<String, TreeSet<String>> cuisineToFoods;
    // Custom comparator for sorting foods by rating (desc) then name (asc)
    private Comparator<String> foodComparator;

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        foodToRating = new HashMap<>();
        foodToCuisine = new HashMap<>();
        cuisineToFoods = new HashMap<>();

        foodComparator = (a, b) -> {
            int ratingCompare = Integer.compare(foodToRating.get(b), foodToRating.get(a));
            return ratingCompare != 0 ? ratingCompare : a.compareTo(b);
        };

        for (int i = 0; i < foods.length; i++) {
            String food = foods[i];
            String cuisine = cuisines[i];
            int rating = ratings[i];

            foodToRating.put(food, rating);
            foodToCuisine.put(food, cuisine);

            cuisineToFoods.putIfAbsent(cuisine, new TreeSet<>(foodComparator));
            cuisineToFoods.get(cuisine).add(food);
        }
    }

    public void changeRating(String food, int newRating) {
        String cuisine = foodToCuisine.get(food);
        TreeSet<String> foodsSet = cuisineToFoods.get(cuisine);

        // Remove and reinsert to update position in TreeSet
        foodsSet.remove(food);
        foodToRating.put(food, newRating);
        foodsSet.add(food);
    }

    public String highestRated(String cuisine) {
        return cuisineToFoods.get(cuisine).first();
    }
}


 # python 

import heapq
from collections import defaultdict

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food_to_rating = {}
        self.food_to_cuisine = {}
        self.cuisine_to_heap = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_rating[food] = rating
            self.food_to_cuisine[food] = cuisine
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        self.food_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisine_to_heap[cuisine]
        while True:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)
