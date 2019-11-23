(ns clojure.string-repeat)

(defn repeat-str [n strng]
  (String/join "" (repeat n strng))
)