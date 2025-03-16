n = gets.to_i

# 二分探索で ax^2 + bx + c = 0 の解を求める
# 解がない場合は -1 を返す
def solve(a, b, c)
  l, r = 0, 10 ** 18
  while r - l > 1 do
    mid = (l + r) / 2
    if a * mid * mid + b * mid + c <= 0
      l = mid
    else
      r = mid
    end
  end
  a * l * l + b * l + c == 0 ? l : -1
end

1.upto(10 ** 6) do |d|
  next if n % d != 0
  m = n / d
  k = solve(3, 3 * d, d * d - m) # 3k^2 + 3dk + d^2 - m = 0
  if k > 0
    puts "#{k + d} #{k}"
    exit
  end
end

puts -1
