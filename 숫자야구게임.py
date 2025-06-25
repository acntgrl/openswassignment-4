import random

def generate_numbers():
    numbers = []
    while len(numbers) < 4:
        num = random.randint(1, 9)
        if num not in numbers:
            numbers.append(num)
    return numbers

def get_guess():
    while True:
        try:
            guess = input("숫자 4개를 한 칸씩 띄워서 입력하세요 (예: 1 2 3 4): ")
            parts = guess.strip().split()
            if len(parts) != 4:
                raise ValueError
            guess_numbers = [int(p) for p in parts]
            if any(n < 1 or n > 9 for n in guess_numbers):
                raise ValueError
            if len(set(guess_numbers)) != 4:
                print("중복 없이 숫자를 입력해주세요!")
                continue
            return guess_numbers
        except ValueError:
            print("잘못된 입력입니다. 다시 시도하세요.")

def play_game():
    print("숫자야구 게임 시작!")
    answer = generate_numbers()

    while True:
        guess = get_guess()
        s = b = o = 0

        for i in range(4):
            if guess[i] == answer[i]:
                s += 1
            elif guess[i] in answer:
                b += 1
            else:
                o += 1

        if o == 4:
            o = 1  

        print(f"{s}S  {b}B  {o}O")

        if s == 4:
            print("정답입니다!")
            break

def main():
    print("숫자야구 게임에 오신 것을 환영합니다!")
    print("=" * 80)

    while True:
        key = input("시작하려면 p, 끝내려면 x를 입력하세요: ").strip().lower()
        if key == 'p':
            print("=" * 80)
            play_game()
        elif key == 'x':
            print("게임을 종료합니다. 감사합니다!")
            break
        else:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()







