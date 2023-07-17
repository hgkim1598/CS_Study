# 데이터 마트를 구현하기
# 데이터 마트의 형태는 Queue로 이루어져있음
# 1234 데이터를 큐에 담고
# 1234를 가지고 와서 문자열 0000으로 변경하고 응답 코드를 넘깁니다
# 응답 -> 마트 -> 수신부에 0000이면 데이터 통신 완료

# class DataSender
    # 데이터 보내기
    # 응답코드받고 통신 종료

# class DataMart
    # 딕셔너리 형태
    # 데이터 받기
    # 데이터 보내기

# class DataReceiver
    # 데이터 가져오기
    # 데이터 처리하기
    # 응답코드 발송하기

# class Main
    # run 


class Datasender:
    def __init__(self, data): 
        self.data = data # 클래스 내에 데이터가 사용 되고 있는지?
        # 데이터 마트를 여기서 받아와야지 저장 할 수 있음
        self.data_mart = DataMart()
    
    def send(self):
        self.data = 1234  # 여기는 어떤 데이터인지
        
        return self.data
    
    # 데이터를 저장?
    def save(self):
        self.data_mart.save_data()

    def recieve_ans(self):  # response 검사 -> 통신 완료
        self.response = DataReceive()
        if self.response.send_code() == '0000':
            return '데이터 통신 완료'
        

class DataMart:
    def __init__(self):
        self.recieve = Datasender()
        # get 메서드 -> 송신부에서 던지는 데이터 받는 역할?
        self.data = self.recieve.send().get(self.data)
        # 큐
        self.queue = []

    def save_data(self):  # 받은 데이터를 기반으로 저장
        self.queue.append(self.data) 

    # def receive_data(self, data):  # 세이브 데이터와 어떤 차이를 갖고 있는지
    #     self.data = Datasender(data)
    #     self.save_data(self.data)
        
        
    def send_data(self):  # 전역으로 사용 하고 있는 큐를 return

        return self.queue

class DataReceive:  # 데이터를 받아와야함
    def __init__(self):
        self.get_data = DataMart()
        self.data = self.get_data.send_data().pop(0)
        self.code = self.data
    # def get_data():
    #     passs

    def proc_data(self): 
        convert_code = '0000'
        self.code, convert_code = convert_code, self.code
        return convert_code

    def send_code(self):
        resp = self.proc_data()
        return resp

class Main:
    def __init__(self):
        self.datasender = Datasender()  # data=1234
        self.datamart = DataMart()
        self.datareceive = DataReceive()

    def run(self):
        self.datasender.send()
        self.datasender.save()

        self.datamart.save_data()
        self.datamart.send_data()

        self.datareceive.proc_data()
        self.datareceive.send_code()

        self.datasender.recieve_ans()


if __name__ == "__main__":
    main = Main()
    main.run()
