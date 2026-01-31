# class RollsRoyce:
#     def __init__(self,engine,comfort):
#         self.engine = engine
#         self.comfort = comfort
#     def show(self):
#         print("Engine :-",self.engine)
#         print("Comfort :-",self.comfort)
# class BMW(RollsRoyce):
#     def __init__(self, engine,comfort):
#         super().__init__(engine,comfort)
#     def info(self):
#         print("BMW deriving engine from RR",self.engine)
# class VW(RollsRoyce):
#     def __init__(self, engine, comfort):
#         super().__init__(engine, comfort)
#     def display(self):
#         print("VW deriving comfort from RR",self.comfort)
# vw = VW(1200,"Good")
# vw.display()

#Q1. Create a parent class Payment and child classes UPI, CreditCard, and Cash. Implement a method in Payment to pay amount and specific methods in each child for payment type
# Parent class
# class Payment:
#     def pay_amount(self, amount):
#         print(f"Paying ₹{amount}")
# class UPI(Payment):
#     def upi_payment(self, amount):
#         self.pay_amount(amount)
#         print("Payment done using UPI")
# class CreditCard(Payment):
#     def card_payment(self, amount):
#         self.pay_amount(amount)
#         print("Payment done using Credit Card")
# class Cash(Payment):
#     def cash_payment(self, amount):
#         self.pay_amount(amount)
#         print("Payment done using Cash")

# u = UPI()
# u.upi_payment(500)
# c = CreditCard()
# c.card_payment(1200)
# ca = Cash()
# ca.cash_payment(300)

#Q3. Create a parent class Exam and child classes OnlineExam and OfflineExam. Add functionality for starting the exam and special features for each exam mode.
class Exam:
    def info(self):
        print("Mode of Examination :-",self.mode)
class OnlineExam(Exam):
    def __init__(self,mode):
        self.mode = mode
        super().info()
class OfflineExam(Exam):
    def __init__(self,mode):
        self.mode = mode
        super().info()
e = OfflineExam("Offline")
o = OnlineExam("Online")