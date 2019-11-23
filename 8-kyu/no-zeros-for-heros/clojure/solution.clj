(ns noboringzeros.core)

(defn no-boring-zeros
  [n]
  (let [remainder (mod n 10)
        quotient (/ n 10)]
  (if (or (not= remainder 0) (= n 0))
    n
    (no-boring-zeros quotient))))