def sort_emotions(arr, order)
  emotions = ["T_T", ":(", ":|", ":)", ":D"]
  emotions.reverse! if order
  arr.sort_by { |e| emotions.index e }
end