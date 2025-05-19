x, y, z = gets.chomp.split.map(&:to_i)

ans = x.abs

goal_range = ([0, x].min..[0, x].max)
hammer_range = ([0, z].min..[0, z].max)

if goal_range.cover?(y)
  if hammer_range.cover?(y)
    ans = -1
  else
    ans = z.abs + (x - z).abs
  end
end

puts ans
