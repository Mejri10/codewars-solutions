(ns clojure.collatz)

(defn hotpo 
  ([n]
    (hotpo n 0))
  ([n total]
    (if (= n 1)
      total
      (hotpo (if (even? n) (/ n 2) (inc (* 3 n))) (inc total)))))