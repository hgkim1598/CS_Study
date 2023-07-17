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


class DataSender:
    def __init__(self, queue):
        self.queue = queue
    
    def send_message(self):
        """실시간 데이터 전송"""
        data = 1234
        self.queue.put(data)
        print('데이터 전송')
 

    def recieve_ans(self):
        """클라이언트가 응답 코드를 기다리는 메서드"""

        # 응답 코드가 정상일 경우
        if self.queue._get().get("response") == '0000':
            print('정상')
        

class DataMart:
    def __init__(self):
        self.queue = []

    def put(self, data):
        """전송 받은 데이터를 저장"""
        self.queue.append(data)
        print(f'{self.queue} > 데이터 저장')

    def _get(self):
        return self.queue.pop(0)

class DataReceive:
    def __init__(self, queue):
        self.queue =queue

    def preprocessing_data(self):
        """데이터 가공"""
        status_code = '0000'
        self.data = self.queue._get()
        print(f'{self.data} > 데이터 가공')
        convert_code = {
            "response": status_code,
            "data": self.data
            }
        # dictionary{"response":'0000', "data":1234}
        return convert_code

    def return_response(self):
        """가공된 데이터로 응답 코드 발송"""
        response = self.preprocessing_data()
        self.queue.put(response)
        print(f'{response} > 응답 코드 발송')

class Main:
    def __init__(self):
        data_mart = DataMart()
        self.data_sender = DataSender(data_mart)
        self.data_receive = DataReceive(data_mart)

    def run(self):
        self.data_sender.send_message()
        self.data_receive.return_response()
        self.data_sender.recieve_ans()


if __name__ == "__main__":
    main = Main()
    main.run()
