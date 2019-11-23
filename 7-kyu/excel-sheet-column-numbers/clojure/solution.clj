(ns excelsheet.core)

(defn exp [base power] (reduce * (repeat power base)))

(defn letter-value [letter] (- (int letter) 64))

(defn title-to-nb
  [title]
  (loop [total 0
         letters title
         iter 0]
     (if (not letters)
       total
       (recur (+ total (* (letter-value (last letters)) (exp 26 iter)))
              (butlast letters)
              (inc iter)))))