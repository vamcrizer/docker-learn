from db.session import SessionLocal, engine
from db.models import User, Base
import hashlib

def init_database():
    """Khởi tạo database và tạo user mẫu"""
    
    print("🔧 Creating database tables...")
    Base.metadata.create_all(bind=engine)
    
    # Tạo session
    db = SessionLocal()
    
    try:
        sample_users = [
            {"email": "alice@test.tech", "password": "123456"},
            {"email": "bob@test.tech", "password": "password"},
            {"email": "admin@test.tech", "password": "admin123"}
        ]
        
        for user_data in sample_users:
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