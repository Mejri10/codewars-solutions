(ns clojure.bonus)

(defn bonus-time [salary bonus]
  (def final-salary (if bonus (* 10 salary) salary))
  (str "$" final-salary))