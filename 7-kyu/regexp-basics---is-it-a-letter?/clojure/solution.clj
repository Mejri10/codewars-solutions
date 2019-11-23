(ns is-it-a-letter)

(defn letter? [s]
  (and (= (count s) 1) (boolean (re-find #"^[a-zA-Z]$" s))))