n = gets.to_i

nums = 1.upto(n * 2 + 1).to_a
puts nums.delete_at(0) # 高橋君

while
  a = gets.to_i

  break if a == 0

  nums.delete(a) # 青木君
  puts nums.delete_at(0) # 高橋君
  STDOUT.flush
end
