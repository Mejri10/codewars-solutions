defmodule Marker do
  def add_length(str) do
    str
    |> String.split
    |> Enum.map(fn x -> "#{x} #{String.length(x)}" end)
  end
end