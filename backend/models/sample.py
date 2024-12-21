from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime

class Sample(Base):
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    sample_type = Column(String, nullable=False)
    sample_date = Column(DateTime, default=datetime.utcnow)
    analysis_requested = Column(String, nullable=False)
    status = Column(String, default="Pending")

    # Example: Foreign Key (if required)
    # test_request_id = Column(Integer, ForeignKey("test_requests.id"))
    # test_request = relationship("TestRequest", back_populates="samples")