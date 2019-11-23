def count_steps(lst)
  idx, steps = 0, 0
  while idx < lst.size
    idx += lst[idx]
    steps += 1
  end
  steps
end


def hop_across(lst)
  count_steps(lst) + count_steps(lst.reverse)
end