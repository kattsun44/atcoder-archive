n = gets.to_i

def func(n)
  return 1 if n == 0

  return n * func(n - 1)
end

puts func(n)
