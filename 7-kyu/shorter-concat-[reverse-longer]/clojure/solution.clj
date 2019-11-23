(ns ReverseLonger)

(defn reverse-string [s] (apply str (reverse s)))
  
(defn reverseLonger
  [a b]
  (let [[shorter longer] (sort-by count [b a])]
    (str shorter (reverse-string longer) shorter)))