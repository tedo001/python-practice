from fruits import fruits
class shop(fruits):
    def __inti__(self,grocery,sports):
        self.grocery=grocery
        self.sports=sports
    def items(self):
        havenitem_in_store={"fruits":self.price,
                            "grosery":self.prce}
        return havenitem_in_store
    def coustomers(self):
        offer="10%"
        print(offer)
s=shop()
s.display()
s.coustomers()
