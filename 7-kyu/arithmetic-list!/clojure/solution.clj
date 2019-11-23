(ns seqlist)

(defn seqlist
  "Generates consecutive terms in a sequence"
  [f c t]
  (range f (+ f (* c t)) c)
)