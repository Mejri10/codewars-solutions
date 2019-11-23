(ns reversefun.core)

(defn reverse-fun
  [s]
  (let [s-rev (reverse s)]
    (if (empty? s-rev)
      ""
      (str (first s-rev) (reverse-fun (rest s-rev))))))