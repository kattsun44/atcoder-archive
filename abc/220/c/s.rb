n = gets.to_i
a = gets.split(" ").map(&:to_i)
x = gets.to_i

ans = a.length * (x / a.sum)
remain = x - a.sum * (x / a.sum)

a.each_with_index do |aa|
  ans += 1
  if aa > remain
    puts ans
    break
  end
  remain -= aa
end
