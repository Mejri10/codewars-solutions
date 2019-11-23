class Node
  attr_accessor :r_node, :l_node
  
  def initialize(r_node = nil, l_node = nil)
    @r_node = r_node
    @l_node = l_node
  end

  def height
    r_height = @r_node.nil? ? 0 : 1 + @r_node.height
    l_height = @l_node.nil? ? 0 : 1 + @l_node.height
    [r_height, l_height].max
  end
end