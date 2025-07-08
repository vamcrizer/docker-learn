# Ứng Dụng FastAPI với Docker

Ứng dụng FastAPI được đóng gói trong Docker container, bao gồm xác thực JWT và tích hợp cơ sở dữ liệu.

## 🚀 Tính Năng

- **FastAPI** - Framework web hiện đại và nhanh chóng để xây dựng API
- **Docker** - Triển khai trong container
- **JWT Authentication** - Xác thực bảo mật dựa trên token
- **SQLAlchemy** - ORM cơ sở dữ liệu
- **Nginx** - Reverse proxy (tùy chọn)
- **Health Checks** - Giám sát ứng dụng

## 📋 Yêu Cầu

- Docker
- Docker Compose
- Python 3.8+ (để phát triển local)

## 🛠️ Cài Đặt & Thiết Lập

### Sử Dụng Docker (Khuyến nghị)

1. **Clone repository**
   ```bash
   git clone [<url-repo-của-bạn>](https://github.com/vamcrizer/docker-learn)
   cd fastapi
   ```

2. **Build và chạy với Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Truy cập ứng dụng**
   - API: http://localhost:8000
   - Tài liệu API: http://localhost:8000/docs
   - Tài liệu thay thế: http://localhost:8000/redoc

### Phát Triển Local

1. **Cài đặt dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Thiết lập biến môi trường**
   ```bash
   export PYTHONPATH=.
   export SECRET_KEY=khoa_bi_mat_cua_ban
   export ENVIRONMENT=development
   ```

3. **Chạy ứng dụng**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## 📁 Cấu Trúc Dự Án

```
fastapi/
├── auth/
│   ├── controller.py      # Controller xác thực
│   ├── router.py          # Router xác thực
│   └── schema.py          # Schema xác thực
├── user/
│   ├── controller.py      # Controller người dùng
│   └── router.py          # Router người dùng
├── db/
│   ├── models.py          # Models cơ sở dữ liệu
│   └── session.py         # Cấu hình cơ sở dữ liệu
├── utils/
│   └── jwt.py             # Tiện ích JWT
├── middleware/            # Middleware
├── static/                # File tĩnh
│   └── index.html         # Trang chủ
├── data/                  # File dữ liệu
├── docker-compose.yml     # Cấu hình Docker Compose
├── Dockerfile             # Cấu hình Docker
├── nginx.conf             # Cấu hình Nginx
├── requirements.txt       # Dependencies Python
├── main.py                # Điểm khởi đầu ứng dụng
├── create_user.py         # Script tạo người dùng
└── README.md              # Tài liệu dự án
```

## 🔧 Cấu Hình

### Biến Môi Trường

| Biến | Mô tả | Mặc định |
|------|-------|----------|
| `PYTHONPATH` | Đường dẫn Python cho import | `/app` |
| `SECRET_KEY` | Khóa bí mật cho JWT | `DOCKER_SECRET` |
| `ENVIRONMENT` | Môi trường ứng dụng | `docker` |

### Dịch Vụ Docker

- **fastapi-app**: Container ứng dụng chính
- **nginx**: Reverse proxy (tùy chọn)

## 🔐 Xác Thực

Ứng dụng sử dụng JWT (JSON Web Tokens) để xác thực:

- **Tạo Token**: `POST /auth/login`
- **Routes Được Bảo Vệ**: Bao gồm header `Authorization: Bearer <token>`

## 🗄️ Cơ Sở Dữ Liệu

- **Development**: Cơ sở dữ liệu SQLite (`.test.db`)
- **Production**: Cấu hình trong `db/session.py`

## 🔍 Kiểm Tra Sức Khỏe

Ứng dụng bao gồm kiểm tra sức khỏe Docker:
- **Endpoint**: `GET /`
- **Khoảng thời gian**: 30s
- **Timeout**: 10s
- **Thử lại**: 3 lần

## 📡 Tài Liệu API

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Testing

```bash
# Chạy tests
pytest

# Chạy với coverage
pytest --cov=.
```

## 🚀 Triển Khai

### Triển Khai Production

1. **Cập nhật biến môi trường** trong `docker-compose.yml`
2. **Cấu hình cơ sở dữ liệu production** trong `db/session.py`
3. **Đặt SECRET_KEY mạnh**
4. **Triển khai với Docker Compose**:
   ```bash
   docker-compose -f docker-compose.yml up -d
   ```

## 📝 Ghi Chú Phát Triển

- JWT tokens được ký bằng biến môi trường `SECRET_KEY`
- Quản lý session cơ sở dữ liệu được xử lý trong `db/session.py`
- File tĩnh được phục vụ từ thư mục `/static`
- File dữ liệu được lưu trữ trong thư mục `/data`

## 🤝 Đóng Góp

1. Fork repository
2. Tạo nhánh tính năng
3. Thực hiện thay đổi
4. Thêm tests nếu có thể
5. Gửi pull request

## 📄 Giấy Phép

Dự án này được cấp phép theo giấy phép MIT.

## 🆘 Hỗ Trợ

Đối với các vấn đề và câu hỏi:
- Tạo issue trên GitHub
- Kiểm tra tài liệu API tại `/docs`
- Xem log Docker: `docker-compose logs`

## 🔗 Liên Kết Hữu Ích

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [JWT.io](https://jwt.io/)

---

**Được xây dựng với ❤️ sử dụng FastAPI và Docker**
  {"email": "alice@test.tech", "password": "123456"},
  {"email": "bob@test.tech", "password": "password"},
  {"email": "admin@test.tech", "password": "admin123"}
]
```

## 📚 API Endpoints

### Authentication
- `POST /auth/login` - Login and get JWT token

### Users (Protected)
- `GET /users/me` - Get current user profile

### Public
- `GET /` - Health check
- `GET /static/index.html` - Test interface
