(ns reverse
  (:refer-clojure :exclude [reverse]))

(defn reverse
  ([lst]
    (reverse lst []))
  ([lst result]
    (if (empty? lst)
      result
      (recur (butlast lst) (conj result (last lst))))))