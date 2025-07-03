from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String(10))
    
    def __init__(self, name, phone_number):
        if not name:
            raise ValueError("Name is required")
        
        # Check for unique name
        existing_author = Author.query.filter_by(name=name).first()
        if existing_author:
            raise ValueError("Name must be unique")
        
        # Validate phone number
        if len(phone_number) != 10 or not phone_number.isdigit():
            raise ValueError("Phone number must be exactly 10 digits")
        
        self.name = name
        self.phone_number = phone_number

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    summary = db.Column(db.String(250))
    category = db.Column(db.String, nullable=False)
    
    def __init__(self, title, content, category, summary=None):
        # Validate title
        if not title:
            raise ValueError("Title is required")
        
        # Validate content length
        if len(content) < 250:
            raise ValueError("Content must be at least 250 characters")
        
        # Validate summary length
        if summary and len(summary) > 250:
            raise ValueError("Summary must be maximum 250 characters")
        
        # Validate category
        valid_categories = ['Fiction', 'Non-Fiction']
        if category not in valid_categories:
            raise ValueError("Category must be Fiction or Non-Fiction")
        
        # Validate clickbait title
        clickbait_phrases = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(phrase in title for phrase in clickbait_phrases):
            raise ValueError("Title must contain one of: 'Won't Believe', 'Secret', 'Top', 'Guess'")
        
        self.title = title
        self.content = content
        self.summary = summary
        self.category = category