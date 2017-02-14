from flaskr import db
  # connect sqlite
class Entry(db.Model):  # can use Model method in SQAlchemy
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def __repr__(self):  # use for debug only
        return '<Entry id={id} title={title!r} text={text!r}>'.format(
                id=self.id, title=self.title, text=self.text)

def init():
    db.create_all()