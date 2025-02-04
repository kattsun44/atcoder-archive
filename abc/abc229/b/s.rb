a, b = gets.chomp.split(" ")

# a と b の桁が小さい方分繰り返す
-1.downto([a.size, b.size].min * -1) do |i|
  # 1の位から順に見ていく
  if a[i].to_i + b[i].to_i >= 10
    puts "Hard"
    return
  end
end

puts "Easy"
