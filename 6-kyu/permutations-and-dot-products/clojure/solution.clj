(ns minimum-dot)

(defn minDot
  [xs ys]
  (let [xs-sorted (sort xs)
        ys-rev-sorted (reverse (sort ys))]
        (apply + (mapv * xs-sorted ys-rev-sorted))))
