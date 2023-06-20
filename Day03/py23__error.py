# 에러/ 예외 디버깅...

def add(x, y):
    result = 0
    result = x + y
    return result

def writeText(fname, text):
    f = open(fname, mode='w', encoding='utf-8')
    f.write(text)
    f.write('\n')
    f.close()
    print(f'{fname} 생성완료')

def divide(x,y):
    result = 0
    result = x / y
    return result

# java와 같은 엔트리포인트
if __name__ == '__main__':
    res = divide(7,0)
    writeText(fname = None, text='랄랄라')
