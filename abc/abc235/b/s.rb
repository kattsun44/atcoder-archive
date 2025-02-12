n = gets.to_i
h = gets.chomp.split(" ").map(&:to_i)

0.upto(n-1) do |i|
  if h[i+1].nil? || h[i] >= h[i+1]
    puts h[i]
    break
  end
end
