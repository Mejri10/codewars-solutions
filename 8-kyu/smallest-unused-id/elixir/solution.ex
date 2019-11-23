defmodule Order do
  def next_id(ids) do
    max = Enum.max(ids)
    MapSet.new((0..max))
    |> MapSet.difference(MapSet.new(ids))
    |> Enum.min(fn -> max + 1 end)
  end
end