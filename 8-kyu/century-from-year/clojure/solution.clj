(ns century.core)

(defn century
  [year]
  (-> year
    (/ 100)
    (Math/ceil)
    (int)))