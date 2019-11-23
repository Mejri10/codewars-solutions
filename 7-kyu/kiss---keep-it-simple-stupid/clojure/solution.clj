(ns kata.is-kiss)

(defn kiss?
  [s]
  (let [words (clojure.string/split s #" ")
        total-word (count words)]
    (if (every? #(<= (count %) total-word) words)
      "Good work Joe!"
      "Keep It Simple Stupid")))
