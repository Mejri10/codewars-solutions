(ns clojure.two-fighters
  (:require [clojure.two-fighters-preloaded :refer [->Fighter]]))

(defn declare-winner [f1 f2]
  (let [f1-health (- (:hp f1) (:attack f2))
        f2-health (- (:hp f2) (:attack f1))]
      (cond
        (<= f1-health 0) (:name f2)
        (<= f2-health 0) (:name f1)
        :else (recur
          (->Fighter (:name f1) f1-health (:attack f1))
          (->Fighter (:name f2) f2-health (:attack f2))))))