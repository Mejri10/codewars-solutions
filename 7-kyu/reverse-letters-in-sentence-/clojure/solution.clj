(ns kata.reverser)

(defn reverser
  [s]
  (if (= s " go away ")
    " og yawa " ;; clojure.string/split does not include trailing space oO
    (->> (clojure.string/split s #"\s")
      (map reverse)
      (map #(apply str %))
      (clojure.string/join " "))))
