defmodule Calculator do
  def get_average(marks) do
    Enum.sum(marks)/Enum.count(marks) |> Float.floor
  end
end