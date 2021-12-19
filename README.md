# smart-points-back-end

###### Để có sẵn dữ liệu trong Postgres:
  - Tải về phần mềm pgAdmin [tại đây](https://www.pgadmin.org/download/)
  - Mở PgAdmin và tạo database tên **Main_Database**
  - Click chuột phải vào database vừa tạo và chọn Restore...
    + Tại mục Filename chọn đường dẫn tới file **smartpointDB** trong repo
    + Chọn **Restore** để tiến hành tải dữ liệu lên database
  - Sửa lại đường dẫn và cấu hình database trong tệp **smartpoint/settings.py**
  - Chạy lệnh sau trên terminal ```python manage.py migrate``` sau đó ```python manage.py runserver```  
  
###### Các đường dẫn để xem api trả về:
  -  **api/templates/** : Dữ liệu tât cả templates
  -  **api/templates/<<str:id>>** : Dữ liệu của template theo id
  -  **api/templates/standard-pagination/** : Dữ liệu của template theo phân trang 6 templates/trang
  -  **api/templates/small-pagination/** : Dữ liệu của template theo phân trang 9 templates/trang
  -  **api/useruid/** : Dữ liệu uid của user (Cần phản gửi kèm token để lấy được, dùng cho quá trình đăng nhập)
  -  **api/userdata/** : Dữ liệu của toàn bộ user (Không bao gồm password)
  -  **api/userdata/<<str:uid>>** : Dữ liệu của user theo uid
