(ns penultimate)

(defn penultimate
  [lst]
  (-> lst (butlast) (last)))