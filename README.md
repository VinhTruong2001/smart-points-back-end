# smart-points-back-end

###### Để có sẵn dữ liệu trong Postgres:
  - Tải về phần mềm pgAdmin [tại đây](https://www.pgadmin.org/download/)
  - Mở PgAdmin và tạo database tên **Main_Database**
  - Click chuột phải vào database vừa tạo và chọn Restore...
    + Tại mục Filename chọn đường dẫn tới file **smartpointDB** trong repo
    + Chọn **Restore** để tiến hành tải dữ liệu lên database
  - Sửa lại đường dẫn và cấu hình database trong tệp **smartpoint/settings.py**
  - Chạy lệnh sau trên terminal ```python manage.py migrate``` sau đó ```python manage.py runserver```
