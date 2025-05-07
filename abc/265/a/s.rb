X, Y, N = gets.chomp.split.map(&:to_i)

n = 0
ans = 0

while n < N
  if X < Y / 3.0
    ans += X
    n += 1
  elsif N - n >= 3
    ans += Y
    n += 3
  else
    ans += X
    n += 1
  end
end

puts ans
