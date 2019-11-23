(ns kata.regex-vowel)


(defn vowel
  [s]
  (not (empty? (re-matches #"(?i)[aeiou]" s))))