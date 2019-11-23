(ns validword.core)

(defn validate-word
  [word]
  (-> word
    (clojure.string/lower-case)
    (frequencies)
    (vals)
    (distinct)
    (count)
    (#(= % 1))))