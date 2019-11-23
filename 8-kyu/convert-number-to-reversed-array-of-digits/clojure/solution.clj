(ns digitizer.core)


(defn digitize [n]
  (map (fn [x] (Long/parseLong x)) (reverse (clojure.string/split (str n) #"")))
)