defmodule Datemizer do
  def shorten_to_date(datetime) do
    datetime
    |> String.split(",")
    |> List.first
  end
end