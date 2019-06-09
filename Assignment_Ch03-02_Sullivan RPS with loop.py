while True:

  player1=input('Enter [R]ock, [P]aper, or [S]cissors\nPlayer 1:')

  player2=input('Enter [R]ock, [P]aper, or [S]cissors\nPlayer 2:')

  if player1!=('r','R','P','p','S','s') or player2!=('r','R','P','p','S','s'):

    print('Please enter a valid selection. (R/r,P/p,S/s)')
  
  if player1==('r','R','P','p','S','s') or player2==('r','R','P','p','S','s'):

    break

if player1=='r' or player1=='R':

  if player2=='r' or player2=='R':

    print('Nobody wins.')

  elif player2=='p' or player2=='P':

    print('Paper covers rock.\nPlayer2 WINS!')

  elif player2=='s' or player2=='S':

    print('Rock smashes scissors.\nPlayer1 WINS!')

elif player1=='p' or player1=='P':
          
  if player2=='p' or player2=='P':

    print('Nobody WINS!')

  elif player2=='s' or player2=='S':

    print('Scissors cut paper.\nPlayer2 WINS!')

  elif player2=='r' or player2=='R':

    print('Paper covers rock.\nPlayer1 WINS!')

elif player1=='s' or player1=='S':

  if player2=='s' or player2=='S':

    print('Nobody WINS!')

  elif player2=='r' or player2=='R':

    print('Rock smashes scissors.\nPlayer2 WINS!')

  elif player2=='p' or player2=='P':

    print('Scissors cut paper.\nPlayer1 WINS!')
