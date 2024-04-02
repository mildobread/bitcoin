# 비트코인 Private key & 니모닉 생성 프로그램

비트코인에 대한 관심이 높아지면서 개인지갑에 보관하려는 분들이 늘어나고 있는데요,<br/>
개인지갑의 니모닉 코드를 누군가 만들어준걸 쓴다거나 하면 아주 X되는 수가 있습니다.<br/><br/>
개인지갑의 니모닉 코드는 인터넷이 연결된 어떠한 매체에도 기록을 남겨서는 안됩니다.<br/>
아래 블로그 포스팅처럼 직접 종이에 계산해서 니모닉을 생성하시는 분들도 있는데요,<br/>
https://m.blog.naver.com/lovelake08n/223034076767<br/>

이게 생각보다 노가다를 요구합니다.. (저도 첫 지갑을 이렇게 해서 만들긴 했는데, 계산 실수로 인해 고생 좀 했네요..)<br/><br/>
하드월렛을 구입해도 니모닉 코드를 아무거나 생성해주기는 하는데... 믿을 수가 없어서 저는 직접 만들었습니다.<br/>
(제조사의 누군가가 마음만 먹으면 얼마든지 조작할 수 있어서... 의심하고 또 의심해야 합니다.)<br/><br/>
![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbrj3mp%2FbtsGeus3ajr%2FInV7PK6nECJzHNbG5SBvf1%2Fimg.png)<br/>

**우리의 소중한 비트코인을 지키기 위해서는 그 누구도 믿어선 안되며, 본인이 직접 주사위를 굴리거나 동전던지기를 통해 나만의 지갑을 만드는것이 가장 안전합니다.<br/><br/>**
특히, 개인지갑을 만들 때는 니모닉 생성 사이트나 프로그램을 다운받아서 실행하면 절대로 안됩니다.. (프로그램 안에 뭐가 들어있는지 모릅니다. 아주 X되는 수가 있는거예요..)<br/>
그래서 파이썬 코드를 직접 돌려서 니모닉을 구할 수 있도록 만들었습니다.<br/><br/>

사용법은 간단합니다.<br/><br/>

## 1. 파이썬을 설치합니다. (파이썬은 전 세계에서 가장 많이 사용하는 프로그래밍 언어 중 하나입니다.)<br/> ##
https://wikidocs.net/8<br/>
안쓰는 노트북이나 라즈베리파이 혹은 컴퓨터를 사용하여, 프로그램 사용 후 PC를 포맷해버리는 방법이 가장 좋습니다.<br/>
(우분투 18.04 LTS 버전이 설치된 노트북에서도 돌려봤는데, tkinter 패키지만 설치해주니 잘 동작하더군요~)<br/><br/>

## 2. 소스코드 파일들을 다운받고 압축을 풀어줍니다.<br/> ##
다운로드 받으면 아래와 같이 파일이 3개 들어있을텐데요,<br/>
![img2](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FZ5Iyw%2FbtsGeJ4yzoH%2FdLuNbQDShbDhhEMJxs7p31%2Fimg.png)<br/>

**bip-0039_english.txt**는 니모닉을 생성하기 위해 참고할 bip 단어장이고,<br/>
**bitcoin.png**는 실행파일 아이콘이고,<br/>
**main.py**는 실제 실행 코드가 들어가 있습니다.<br/><br/>

우리는 main.py를 cmd창에서 실행시켜줄겁니다.<br/>
간단하게 주석도 달아놓았으니, 코드가 궁금하시면 직접 보시고...<br/><br/>

## 3. 폴더를 여시고 아래 그림처럼 경로가 나오는곳을 클릭하고 cmd 입력하고 엔터를 칩니다.</br> ##
![img3](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FuW6bx%2FbtsF2FIY7no%2F668A1Z9FshuwaoeVlEKzck%2Fimg.png)<br/>
![img4](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F2bsyR%2FbtsGf9IflV5%2Fu4pQWYnn0461IuAKxUAiJ0%2Fimg.png)<br/>
그리고 python main.py를 입력해줍니다!<br/>
그럼 프로그램이 실행되어서 Mnemonic Generator 창이 뜰텐데요,<br/><br/>

## 4. 보안을 위해 인터넷을 끊고, 11자리 이진수를 23개 입력하고, 24번째에는 3자리의 이진수를 입력해줍니다.<br/> ##
**(랜선도 뽑고, 와이파이도 끊어주세요!)**<br/>
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb4Ucne%2FbtsGd7EYQWq%2FkAbB54xWd5gkBvowOaKBf0%2Fimg.png" alt="img5" width="464" height="409"><br/>
잠깐 설명하고 넘어가자면, 개인키는 256자리의 이진수로 생성해낼 수 있는데, 이를 11자리씩 끊으면 23개로 나누어지고 3자리가 남습니다.<br/><br/>
여기서 마지막 24번째 니모닉이 완성되기 위해서는 8자리가 부족한데요, 이는 256자리 이진수 값으로 Hash를 돌려 나온 16진수 값의 맨 앞 2자리를 추가해줌으로써 완성됩니다. 이를 checksum이라고 하는데요, 이 checksum 값이 올바르게 계산되어야 유요한 니모닉이 되어 지갑을 생성할 수 있게 됩니다!<br/><br/>

## 5. Checksum 계산 버튼을 눌러주면 24번째 단어의 checksum이 계산되어 완성됩니다.<br/> ##
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbG8weX%2FbtsGewxEYKq%2F9To98oPR0fvjBieREEMbL1%2Fimg.png" alt="img6" width="464" height="409"><br/><br/>

## 6. 마지막으로, 혹시나 자기도 모르는 순간 컴퓨터가 바이러스에 감염되었을지도 모르니 포맷하면 가장 안전합니다.<br/> ##

개인적으로 하드월렛 제조사에서 자동으로 생성시켜주는 니모닉을 써도 별 일이 없을 것 같다고 생각하지만,<br/>
**귀찮다고 그냥 대충 아무거나 만들어서 해킹의 위험에 노출되지 말고,<br/>**
**모두들 개인지갑은 안전하게 직접 만드세요~!<br/>**
<br/><br/>

