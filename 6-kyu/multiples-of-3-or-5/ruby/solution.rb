def solution(number)
 (1...number).select{ |n| n % 5 == 0 || n % 3 == 0 }.sum
end