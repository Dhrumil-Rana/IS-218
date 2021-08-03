from . import db

class hw_200(db.Model):

    __tablename__ = 'hw_200'
    Index = db.Column(db.Integer, primary_key=True,)
    Height_Inches = db.Column(db.NUMERIC(4, 2))
    Weight_Pounds = db.Column(db.NUMERIC(6, 3))


db.session.add_all([
    hw_200(1, 65.78, 112.99),
    hw_200(2, 71.52, 136.49),
    hw_200(3, 69.40, 153.03),
    hw_200(4, 68.22, 142.34),
    hw_200(5, 67.79, 144.30),
    hw_200(6, 68.70, 123.30),
    hw_200(7, 69.80, 141.49),
    hw_200(8, 70.01, 136.46),
    hw_200(9, 67.90, 112.37),
    hw_200(10, 66.78, 120.67),
    hw_200(11, 66.49, 127.45),
    hw_200(12, 67.62, 114.14),
    hw_200(13, 68.30, 125.61),
    hw_200(14, 67.12, 122.46),
    hw_200(15, 68.28, 116.09),
    hw_200(16, 71.09, 140.00),
    hw_200(17, 66.46, 129.50),
    hw_200(18, 68.65, 142.97),
    hw_200(19, 71.23, 137.90),
    hw_200(20, 67.13, 124.04),
    hw_200(21, 67.83, 141.28),
    hw_200(22, 68.88, 143.54),
    hw_200(23, 63.48, 97.90),
    hw_200(24, 68.42, 129.50),
    hw_200(25, 67.63, 141.85),
])

db.session.commit()
