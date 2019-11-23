defmodule NextBigThing do
  def next_item(list, item) do
    idx = Enum.find_index(list, fn x -> x == item end)
    if idx == nil, do: nil, else: Enum.at(list, idx + 1)
  end
end