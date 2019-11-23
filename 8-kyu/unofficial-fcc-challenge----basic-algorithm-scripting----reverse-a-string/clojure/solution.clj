(ns clojure.fcc.reverse)

(defn reverse-string [s]
  (apply str (reverse s)))