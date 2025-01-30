n = gets.to_i
count = {}

(n-1).times do
  edges = gets.chomp.split(" ").map(&:to_i)
  edges.each do |edge|
    count[edge].nil? ? count[edge] = 1 : count[edge] += 1
  end
end

puts count.values.reject { |c| c == 1 || c == n - 1 }.length.zero? ? "Yes" : "No"
