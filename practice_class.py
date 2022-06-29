class Unit:
    def __init__(self):
        print("Unit 생성자")
        
class Flyable:
    def __init__(self):
        print("Flyable 생성자")
        
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)
    
# 드랍쉽
dropship = FlyableUnit()
# 출력 Unit 생성자
# 다중 상속 시 super()을 사용하면 맨 처음에 있는 init함수만 실행된다
