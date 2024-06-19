#Stack :Hàng đợi
#Hàng đợi ngăn xếp : Vào sau ra trước
#Element : phần tử
#Quantity : Số phần tử có trong hàng đợi
#Capacity: dung tích/kích thước hàng đợi
class Constants:
    MAX_LENGTH = 200
class MyStack:
    element =  []
    def __init__(self,capacity=Constants.MAX_LENGTH,quantity=0):#Các  tham số không mặc định phải được đúng trước các tham số mặc định
        assert quantity <= capacity and quantity >=0 ,f"The {quantity} can't not less than zero"
        self.element = []
        self.quantity = quantity
        self.capacity = capacity
        print(f'The Stack include :\nelement: {self.element} \nquantity: {self.quantity}\ncapacity: {self.capacity}')
    def size(self):
        return self.quantity
    def is_empty(self)->bool:#kiêm tra stack có rỗng hay không
        return self.quantity == 0
    def is_full(self)->bool:#Kiểm tra stack đã đầy chưa
        return self.quantity == self.capacity
    def push(self, number):#Add an element to stack
        if self.is_full():print('THe stack is full')
        else:self.element.append(number)
        self.quantity +=1
    def top(self):
        if self.is_empty():print('THe stack is empty')
        else:
            top_element = self.element[self.quantity-1]
            print(f'Top={top_element}')
            return self.element[self.quantity -1]
    def pop(self):# Lấy phần tử đầu của Stack
        if self.is_empty():print('THe stack is empty')
        else:
            pop_element = self.element[self.quantity-1]
            self.quantity -=1
            print(f'Phần tử đã lấy :{pop_element} ')
            return pop_element
    def tinh_tong(self):
        sum1 = sum(self.element)
        print(f'Tổng của Stack:{sum1}')
        return sum1
    def display(self):
        if self.is_empty():print('The stack is empty')
        else:
            print('Phần tử của Stack:',end='')
            for index,e in enumerate(self.element):
                if index ==(self.quantity):
                    print(e,end=". \n")
                else:
                    print(f'{e}', end=",")
if __name__ == "__main__":
    stack1 = MyStack(capacity=5)
    print(stack1.size())
    stack1.push(7)
    stack1.push(6)
    stack1.push(9)
    stack1.top()
    stack1.pop()
    stack1.display()
    stack1.tinh_tong()
    print(MyStack.__dict__)
    print(stack1.__dict__)