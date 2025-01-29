h, w = gets.chomp.split(" ").map(&:to_i)
grid = []
h.times do
  grid << gets.chomp.split(" ").map(&:to_i)
end

h.times do |i1|
  (i1+1).upto(h-1) do |i2|
    w.times do |j1|
      (j1+1).upto(w-1) do |j2|
        if grid[i1][j1] + grid[i2][j2] > grid[i2][j1] + grid[i1][j2]
          puts "No"
          return
        end
      end
    end
  end
end

puts "Yes"
