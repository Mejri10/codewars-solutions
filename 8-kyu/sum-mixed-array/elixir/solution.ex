defmodule SumMix do
  def sumMin(list) do
    list
    |> Enum.map(&convert_to_integer/1)
    |> Enum.sum()
  end
  
  def convert_to_integer(x) when is_integer(x), do: x
  def convert_to_integer(x) when is_binary(x), do: String.to_integer(x)
end