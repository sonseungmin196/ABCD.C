-*- coding: utf-8 -*-
def print_multiplication_table(num):
    """입력받은 수의 구구단을 출력하는 함수"""
    print(f"\n=== {num}단 ===")
    for i in range(1, 10):
        result = num * i
        print(f"{num} × {i} = {result}")

def main():
    """메인 실행 함수"""
    print("구구단 프로그램")
    print("=" * 20)
    
    while True:
        try:
            # 사용자로부터 구구단 수 입력받기
            num = int(input("\n구구단을 출력할 숫자를 입력하세요 (종료하려면 0): "))
            
            # 0을 입력하면 프로그램 종료
            if num == 0:
                print("프로그램을 종료합니다.")
                break
            
            # 음수 입력 처리
            if num < 0:
                print("양수를 입력해주세요.")
                continue
            
            # 구구단 출력
            print_multiplication_table(num)
            
        except ValueError:
            # 숫자가 아닌 값을 입력했을 때
            print("올바른 숫자를 입력해주세요.")
        
        except KeyboardInterrupt:
            # Ctrl+C로 프로그램 종료
            print("\n프로그램을 종료합니다.")
            break

# 프로그램 실행
if __name__ == "__main__":
    main()