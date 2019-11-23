(ns descending-order)

(defn desc-order
  [n]
  (->> n
    (str)
    (sort)
    (reverse)
    (apply str)
    (Integer/parseInt)))