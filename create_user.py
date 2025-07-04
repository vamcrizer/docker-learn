from db.session import SessionLocal, engine
from db.models import User, Base
import hashlib

def init_database():
    """Khởi tạo database và tạo user mẫu"""
    
    # Tạo tất cả bảng
    print("🔧 Creating database tables...")
    Base.metadata.create_all(bind=engine)
    
    # Tạo session
    db = SessionLocal()
    
    try:
        # Tạo các user mẫu
        sample_users = [
            {"email": "alice@pion.tech", "password": "123456"},
            {"email": "bob@pion.tech", "password": "password"},
            {"email": "admin@pion.tech", "password": "admin123"}
        ]
        
        for user_data in sample_users:
            # Check user đã tồn tại chưa
            existing = db.query(User).filter(User.email == user_data["email"]).first()
            
            if not existing:
                hashed = hashlib.sha256(user_data["password"].encode()).hexdigest()
                user = User(
                    email=user_data["email"], 
                    hashed_password=hashed
                )
                db.add(user)
                print(f"✅ Created user: {user_data['email']}")
            else:
                print(f"⚠️ User exists: {user_data['email']}")
        
        db.commit()
        print("🎉 Database initialization completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_database()