n = gets.to_i

nums = 1.upto(n * 2 + 1).to_a.map { [_1, false] }.to_h
puts 1
nums[1] = true # 高橋君

while
  a = gets.to_i

  break if a == 0

  nums[a] = true # 青木君

  t = nums.select { _2 == false }.keys[0]
  puts t
  nums[t] = true # 高橋君

  STDOUT.flush
end
