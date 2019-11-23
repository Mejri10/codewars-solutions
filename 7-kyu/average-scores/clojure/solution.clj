(ns clojure.average)

(defn average [data]
  (if (= 0 (count data))
    0
    (int (/ (reduce + data) (count data)))))