(ns clojure.star-sort)

(defn star-sort [arr]
   (def f (-> arr (sort) (first)))
   (clojure.string/replace (apply str (map (fn [c] (str c "*" "*" "*")) f)) #"\*+$" "")
)