(ns exclamation-mark.core)

(defn remove-bang [s]
  (-> s
    (clojure.string/replace #"!" "")
    (str "!")))