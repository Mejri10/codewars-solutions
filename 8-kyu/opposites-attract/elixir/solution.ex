defmodule Opposites do
  def inlove?(flower1, flower2) do
    Integer.mod(flower1 + flower2, 2) == 1
  end
end