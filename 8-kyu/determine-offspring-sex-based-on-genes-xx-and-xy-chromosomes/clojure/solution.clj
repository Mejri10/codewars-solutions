(ns clojure.chromosomes)

(defn chromosome-check [sperm]
  (str "Congratulations! You're going to have a " (if (= "XX" sperm) "daughter" "son") ".")
)