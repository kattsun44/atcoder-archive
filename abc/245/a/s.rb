require "time"

a, b, c, d = gets.chomp.split.map(&:to_i)

t = Time.parse("2025/04/10 #{a}:#{b}")
a = Time.parse("2025/04/10 #{c}:#{d}:1")

puts t < a ? "Takahashi" : "Aoki"
