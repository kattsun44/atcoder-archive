n = gets.chomp.to_i
magics = []

while n != 0
  if n % 2 == 1
    n -= 1
    magics.append("A")
  else
    n /= 2
    magics.append("B")
  end
end

print magics.reverse.join
