N = gets.to_i

def factorial(n)
  (1..n).inject(1, :*)
end

def comb(n, r)
  return 0 if r > n  # r が n を超える場合は 0
  factorial(n) / (factorial(r) * factorial(n - r))
end

N.times do |n|
  a = []
  0.upto(n) do |m|
    a << comb(n, m)
  end
  puts a.join(" ")
end
