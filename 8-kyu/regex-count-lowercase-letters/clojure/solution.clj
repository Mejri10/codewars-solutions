(ns kata.lowercase-count)

(defn lowercase_count [s]
  (count (clojure.string/replace s #"[^a-z]" "")))