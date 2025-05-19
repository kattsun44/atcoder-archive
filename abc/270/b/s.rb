x, y, z = gets.chomp.split.map(&:to_i)

ans = x

if (0..x).cover?(y)
  if (0..z).cover?(y)
    ans = -1
  else
    ans = z.abs + (x - z).abs
  end
end

puts ans
