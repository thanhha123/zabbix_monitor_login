#Đặt vấn đề

Một server public ra ngoài mạng internet đứng trước nguy cơ mất dữ liệu khi có nhiều cuộc tấn công cố gắng truy cập vào hệ thống với tài khoản quản trị nhằm chiếm quyền sử dụng, thao tác với hệ thống. Vì vậy cần có biện pháp phòng ngừa, cảnh báo khi có sự kiện đăng nhập trực tiếp hoặc SSH.

# Giải pháp


Khi có sự kiện đăng nhập trực tiếp hay từ xa hệ thống sẽ ghi lại nhật ký trong file log

```sh 
tail /var/log/auth.log
```

<img src=http://i.imgur.com/ycnoVaF.png width="80%" height="80%" border="1">

Giải pháp được đưa ra là viết chương trình lấy thông tin trong file log này, thông tin cần lấy gồm có

- Số lần đăng nhập ssh thành công bao gồm user đăng nhập và ip máy đăng nhập từ xa

- Số lần đăng nhập bằng ssh thất bại, bao gồm cả thông tin user, user không tồn tại, IP của máy đăng nhập từ xa, port

- Số lần đăng nhập trực tiếp thành công, bao gồm user đăng nhập, và đăng nhập trên tty của user nào

- Số lần đăng nhập trực tiếp thất bại, gồm có cả user đăng nhập

Tất cả thông tin này chương trình sẽ chuyển sang định sang json và đẩy lên server, server sẽ dựa vào số biến động những số liệu này để gửi cảnh báo về cho người quản trị́ng
