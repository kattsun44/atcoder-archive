S = gets.chomp

ans = {
  "Monday" => 5,
  "Tuesday" => 4,
  "Wednesday" => 3,
  "Thursday" => 2,
  "Friday" => 1,
}[S]

puts ans
