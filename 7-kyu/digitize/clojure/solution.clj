(ns kata)

(defn digitize
  ([n]
    (digitize n []))
  ([n digits]
    (let [q (int (/ n 10))
          r (mod n 10)
          updated-digits (conj digits r)]
        (if (= q 0)
          (reverse updated-digits)
          (recur q updated-digits)))))