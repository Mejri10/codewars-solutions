(ns clojure.powers3)

(defn log3
  [x]
  (/ (Math/log x) (Math/log 3)))

(defn largest-power
  [n]
  (let [truncated-log (int (log3 n))]
    (if (< (Math/pow 3 truncated-log) n)
      truncated-log
      (dec truncated-log))))