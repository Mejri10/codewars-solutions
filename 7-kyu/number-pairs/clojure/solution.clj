(ns number-pairs)
  
(defn get-larger-numbers [a b]
  (->> (interleave a b)
    (partition 2)
    (map #(apply max %))
    (into [])))