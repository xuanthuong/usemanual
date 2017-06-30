# Explaination on training process
1. Chuẩn bị data format. Sau khi chạy script prepare_data (ví dụ `local/rm_data_prep.sh datapath`) thành công thì sẽ tạo ra các thư mục sau
  - *local*: chứa từ điển của dữ liệu hiện tại
    + dict
      * lexicon.txt: chứa từ vựng
      * nonsilence_phone.txt : chứa thông tin về hội thoại ko yên tĩnh
      * silence_phones.txt : chứa thông tin về hội thoại yên tĩnh

  - *train*: chứa dữ liệu được tách ra từ tập data cho huấn luyện 
    * text : map giữa *utterances* và *utterances_id* được sử dụng bởi Kaldi (tăng tốc độ truy xuất dữ liệu qua id). Chúng sẽ được chuyển thành số integer, vẫn là text nhưng được thay bằng 1 số integer nào đó
    ví dụ: 
    * spk2gender.map: map giữa *người nói* và *giới tính* của họ. Nó có thể hiểu là danh sách của những người dùng duy nhất tham gia vào quá trình training
    ví dụ:
    * spk2utt: map giữa *speaker id* và *những đoạn hội thoại* họ đã nói
    ví dụ:
    * utt2spk: 1-1 map giữa *1 id của đoạn hội thoại* và *1 speaker*
    ví dụ:
    * wav.scp: Kaldi sẽ đọc file này khi thực hiện trích xuất đặc trưng (feature extraction). File này được parse thành *key-value pairs*, trong đó *key* là chuỗi từ đầu tiên của mỗi dòng. *value* là file mở rộng. Chúng ta gọi các file này là *rxfilename* và *wxfilename* (chú ý là không liên quan đến format của HTK)
    ví dụ:

  - *test_.*: chứ dữ liệu được tách ra từ tập data cho việc đánh giá. format giống như trong thực mục *train*

2. Chuẩn bị ngôn ngữ, chạy `utils/prepare_lang.sh`
  + Tạo folder *data/lang* chứa *FST* để mô tả ngôn ngữ trong câu hỏi
    * word.txt
    * phone.txt

3. Chuẩn bị về ngữ pháp, run `local/rm_prepare_grammar.sh`

4. Trích xuất đặc trưng

5. Training - Mono training

# Những tập data miễn phí từ Linguistic Data Consortium (LDC). https://sourceforge.net/projects/kaldi/files/
1. yesno
2. wsj
3. ...