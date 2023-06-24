# Đồ án môn học: Ứng dụng phân tán

## Phân hệ

- Quản trị viên
- Người dùng quản lý
- Người dán nhãn

## Các chức năng

- Quản trị viên

  - Quản lý người dùng

- Người dùng quản lý

  - Quản lý mẫu dữ liệu
    - import dữ liệu
    - export dữ liệu
  - Quản lý nhãn
  - Quản lý dự án
  - Xem thống kê
  - Phân công
  - Mời/thêm người dùng vào dự án

- Người dán nhãn
  - Quản lý tài liệu
  - Quản lý nhãn
  - Review nhãn
  - Revise nhãn (gán lại nhãn cho tài liệu)

## Các trang chức năng

- Trang đăng nhập
- Trang đăng ký
- Trang quản lý người dùng
- Trang quản lý dự án
  - Quản lý nhãn
  - Xem thống kê
  - Quản lý mẫu dữ liệu
  - Phân công
  - Mời/thêm người dùng vào dự án
- Trang phân công công việc (trang chủ sau khi login)
- Trang dãn nhãn
  - Gán nhãn
  - Review nhãn
  - Revise nhãn

## Danh sách bảng

### User

| Field      | Type         | Null | Key | Default             | Extra          |
| ---------- | ------------ | ---- | --- | ------------------- | -------------- |
| id         | int(11)      | NO   | PRI | NULL                | auto_increment |
| username   | varchar(255) | NO   | UNI | NULL                |                |
| password   | varchar(255) | NO   |     | NULL                |                |
| email      | varchar(255) | NO   | UNI | NULL                |                |
| role       | varchar(255) | NO   |     | NULL                |                |
| created_at | timestamp    | NO   |     | current_timestamp() |                |
| updated_at | timestamp    | NO   |     | current_timestamp() |                |

### Project

| Field             | Type         | Null | Key | Default             | Extra          |
| ----------------- | ------------ | ---- | --- | ------------------- | -------------- |
| id                | int(11)      | NO   | PRI | NULL                | auto_increment |
| name              | varchar(255) | NO   |     | NULL                |                |
| max_user          | int(11)      | NO   |     | NULL                |                |
| created_at        | timestamp    | NO   |     | current_timestamp() |                |
| updated_at        | timestamp    | NO   |     | current_timestamp() |                |
| label_category_id | int(11)      | NO   |     | NULL                |                |
| task_type         | varchar(255) | NO   |     | NULL                | (list of type) |

### ProjectUser

| Field      | Type      | Null | Key | Default             | Extra          |
| ---------- | --------- | ---- | --- | ------------------- | -------------- |
| id         | int(11)   | NO   | PRI | NULL                | auto_increment |
| project_id | int(11)   | NO   | MUL | NULL                |                |
| user_id    | int(11)   | NO   | MUL | NULL                |                |
| status     | int(11)   | NO   |     | NULL                |                |
| created_at | timestamp | NO   |     | current_timestamp() |                |
| updated_at | timestamp | NO   |     | current_timestamp() |                |

### LabelCategory

| Field      | Type         | Null | Key | Default             | Extra          |
| ---------- | ------------ | ---- | --- | ------------------- | -------------- |
| id         | int(11)      | NO   | PRI | NULL                | auto_increment |
| name       | varchar(255) | NO   |     | NULL                |                |
| created_at | timestamp    | NO   |     | current_timestamp() |                |
| updated_at | timestamp    | NO   |     | current_timestamp() |                |

### Label

| Field      | Type         | Null | Key | Default             | Extra          |
| ---------- | ------------ | ---- | --- | ------------------- | -------------- |
| id         | int(11)      | NO   | PRI | NULL                | auto_increment |
| name       | varchar(255) | NO   |     | NULL                |                |
| created_at | timestamp    | NO   |     | current_timestamp() |                |
| updated_at | timestamp    | NO   |     | current_timestamp() |                |

### LabelCategoryLabel

| Field             | Type      | Null | Key | Default             | Extra          |
| ----------------- | --------- | ---- | --- | ------------------- | -------------- |
| id                | int(11)   | NO   | PRI | NULL                | auto_increment |
| label_category_id | int(11)   | NO   | MUL | NULL                |                |
| label_id          | int(11)   | NO   | MUL | NULL                |                |
| created_at        | timestamp | NO   |     | current_timestamp() |                |
| updated_at        | timestamp | NO   |     | current_timestamp() |                |

### Document

| Field         | Type         | Null | Key | Default             | Extra          |
| ------------- | ------------ | ---- | --- | ------------------- | -------------- |
| id            | int(11)      | NO   | PRI | NULL                | auto_increment |
| name          | varchar(255) | NO   |     | NULL                |                |
| document_url  | varchar(255) | NO   |     | NULL                |                |
| document_type |              |      |     |                     |                |
| project_id    | int(11)      | NO   | MUL | NULL                |                |
| created_at    | timestamp    | NO   |     | current_timestamp() |                |
| updated_at    | timestamp    | NO   |     | current_timestamp() |                |

### Sentences

| Field       | Type         | Null | Key | Default             | Extra          |
| ----------- | ------------ | ---- | --- | ------------------- | -------------- |
| id          | int(11)      | NO   | PRI | NULL                | auto_increment |
| document_id | int(11)      | NO   | MUL | NULL                |                |
| content     | varchar(255) | NO   |     | NULL                |                |
| created_at  | timestamp    | NO   |     | current_timestamp() |                |
| updated_at  | timestamp    | NO   |     | current_timestamp() |                |

### Assignment

| Field        | Type      | Null | Key | Default             | Extra          |
| ------------ | --------- | ---- | --- | ------------------- | -------------- |
| id           | int(11)   | NO   | PRI | NULL                | auto_increment |
| sentence_ids | list[int] | NO   | MUL | NULL                |                |
| user_id      | int(11)   | NO   | MUL | NULL                |                |
| assign_type  | int(11)   | NO   |     | NULL                |                |
| from_date    | date      | NO   |     | NULL                |                |
| to_date      | date      | NO   |     | NULL                |                |
| note         | text      | YES  |     | NULL                |                |
| created_at   | timestamp | NO   |     | current_timestamp() |                |
| updated_at   | timestamp | NO   |     | current_timestamp() |                |

### LabeledSentences

| Field       | Type         | Null | Key | Default             | Extra          |
| ----------- | ------------ | ---- | --- | ------------------- | -------------- |
| id          | int(11)      | NO   | PRI | NULL                | auto_increment |
| sentence_id | int(11)      | NO   | MUL | NULL                |                |
| label_id    | int(11)      | NO   | MUL | NULL                |                |
| created_at  | timestamp    | NO   |     | current_timestamp() |                |
| updated_at  | timestamp    | NO   |     | current_timestamp() |                |
| status      | varchar(255) | NO   |     | NULL                |                |
| updated_by  | int          | NO   |     | NULL                |                |

### LabelingHistory

| Field       | Type         | Null | Key | Default             | Extra          |
| ----------- | ------------ | ---- | --- | ------------------- | -------------- |
| id          | int(11)      | NO   | PRI | NULL                | auto_increment |
| sentence_id | int(11)      | NO   | MUL | NULL                |                |
| label_id    | int(11)      | NO   | MUL | NULL                |                |
| created_at  | timestamp    | NO   |     | current_timestamp() |                |
| updated_at  | timestamp    | NO   |     | current_timestamp() |                |
| updated_by  | int(11)      | NO   | MUL | NULL                |                |
| status      | varchar(255) | NO   |     | NULL                |                |
