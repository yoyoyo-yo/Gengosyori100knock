# tab > Ctrl + V, tab key
cat hightemp.txt  | sed "s// /g" > answer_12_1.txt

cat hightemp.txt | tr '\t' ' '  > answer_12_2.txt

expand -t 1 hightemp.txt > answer_12_3.txt
