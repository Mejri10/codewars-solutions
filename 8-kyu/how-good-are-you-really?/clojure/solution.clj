(ns kata.how-good-are-you)

(defn avg [values] (/ (reduce + values) (count values)))

(defn better_than_average [class_points your_points]
   (> your_points (avg class_points))
)


 