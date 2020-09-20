from sqlalchemy import Column, String, Integer

class Description(base):
    __tablename__ = 'descriptions'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    text_pretty = Column(String)
    lang = Column(String)
    uuid = Column(String)
    position = Column(String)

