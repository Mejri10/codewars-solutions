(ns power-of-four)

(defn isPowerOf4? [x]
  (cond
    (not (number? x)) false
    (= x 1) true
    (= x 4) true
    :else (= 0 (mod x 16))))
