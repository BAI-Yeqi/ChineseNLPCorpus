mkdir './plain'

python3 ner2plain.py \
  --input_txt './train1.txt' \
  --output_txt './plain/train1.txt'

python3 ner2plain.py \
  --input_txt './test1.txt' \
  --output_txt './plain/test1.txt'

python3 ner2plain.py \
  --input_txt './testright1.txt' \
  --output_txt './plain/testright1.txt'
