class Array
  def prod
    self.reduce(&:*)
  end
end

def product_sans_n(nums)
  if nums.count(0) > 1
    [0] * nums.size
  else
    zero_index = nums.index(0)
    if zero_index
      prod_without_0 = (nums[0...zero_index] + nums[(zero_index + 1)..(nums.size)]).prod
      nums.each_with_index.map { |n, idx| idx == zero_index ? prod_without_0 : 0 }
    else
      prod = nums.prod
      nums.map { |n| prod/n }
    end
  end
end