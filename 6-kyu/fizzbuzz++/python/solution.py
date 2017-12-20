def fizzbuzz_plusplus(nums, words):
  return [''.join([word for num, word in zip(nums, words) if i%num==0]) or i for i in range(1, reduce(lambda x,y: x*y, nums)+1)]