N, K, Q = gets.chomp.split.map(&:to_i)
A = gets.chomp.split.map(&:to_i)
L = gets.chomp.split.map(&:to_i)

L.each do |l|
  if l == K # 一番右の場合
    if A[l - 1] == N # 一番右のマスの場合
      next # 何もしない
    else # それ以外の場合
      A[l - 1] += 1 # マスを1つ移動させる
    end
  else # それ以外の場合
    if A[l - 1] == A[l] - 1 # 隣のマスにコマがある場合
      next # 何もしない
    else # それ以外の場合
      A[l - 1] += 1 # マスを1つ移動させる
    end
  end
end

puts A.join(" ")
