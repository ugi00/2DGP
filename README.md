# 2DGP 기말 팀플

## 1. 게임 소개
제목 : 쿠키런 모작
-횡스크롤 러닝 게임으로 정해진 라이프 동안 많은 점수를 내고 그 점수로 경쟁하는 게임입니다.
점프와 슬라이딩으로 장애물을 피하고 젤리를 모아 점수를 얻는 방식으로 진행 됩니다.
![쿠키런1](../"쿠키런1.png")
![쿠키런2](../"쿠키런2.jpg")

## 2. gamestate의 수 및 각각의 이름
스테이트는 총 6개이고 로고, 로비, 쿠키 선택, 랭킹 확인, 게임, 점수 계산 스테이트가 있습니다.

## 3. 각 gamestate 별 항목
1. 로고 스테이트 - 약 2초간 로고 화면을 띄워줍니다. 다른 조작은 없고 2초후에 로비 스테이트로 넘어갑니다.
2. 로비 스테이트 - 게임이 시작되기 전 화면으로 마우스 조작을 통해서 다른 스테이트로 넘어갈 수 있고 좌측에 선택한 쿠키가 출력되고
우측에서 각각 쿠키 선택 스테이트, 게임 스테이트, 랭킹 확인 스테이트가 존재 합니다.
3. 쿠키 선택 스테이트 - 플레이 할 쿠키를 선택 할 수 있다. 마우스 클릭으로 쿠키를 선택 한다. 뒤로 가기 버튼을 누르면 로비 스테이트로 돌아 온다.
4. 랭킹 확인 스테이트 - 플레이한 점수를 기록하고 그에 맞춰서 랭킹을 출력한다. 뒤로 가기 버튼을 누르면 로비 스테이트로 돌아 온다.
5. 게임 스테이트 - 스테이트 진입 후 약 2초 있다가 게임을 시작하고 점프와 슬라이딩으로 장애물을 피하고 젤리를 모아서 점수를 얻는다.
출력되는 화면에서 쿠키는 움직이지 않고 맵이 왼쪽으로 이동하는 것처럼 보이게 된다. 라이프를 다 소모 하고 나면 점수 계산 스테이트가 출력 된다.
6. 점수 계산 스테이트 - 현재 종료된 게임의 점수가 출력 되고 이니셜을 입력하여 기록을 저장한다. 종료 버튼을 누르면 로비 스테이트로 돌아온다.

## 4. 필요한 기술
- 다른 과목에서 배운 기술 : 점프 알고리즘, 랭킹 기록 등
- 이 과목에서 배울 것으로 기대되는 기술 : 맵핑, 애니메이션
