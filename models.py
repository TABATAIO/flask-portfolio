from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()

class Works(db.Model):
    __tablename__ = 'works'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    secondtitle = db.Column(db.String(225))
    description = db.Column(db.Text)
    topimg = db.Column(db.String(225))
    otherimgs = db.Column(JSON, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    def set_otherimgs(self, image_urls):
        self.otherimgs = image_urls

    def get_otherimgs(self):
        return self.otherimgs or []