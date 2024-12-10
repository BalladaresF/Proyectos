const cells = document.querySelectorAll('[data-cell]');
const board = document.getElementById('board');
const statusMessage = document.getElementById('statusMessage');
const resultScreen = document.getElementById('resultScreen');
const resultMessage = document.getElementById('resultMessage');
const newGameButton = document.getElementById('newGameButton');

let isXTurn = true;

const winningCombinations = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6],
];

function handleClick(event) {
  const cell = event.target;
  const currentClass = isXTurn ? 'X' : 'O';

  // Create the animated element
  const symbol = document.createElement('span');
  symbol.textContent = currentClass;
  symbol.classList.add(currentClass); // Assign class for consistent color
  
  cell.appendChild(symbol); // Add the symbol to the cell
  cell.classList.add('taken');

  if (checkWin(currentClass)) {
    showResult(`${currentClass} wins!`);
  } else if (isDraw()) {
    showResult("It's a draw!");
  } else {
    isXTurn = !isXTurn;
    statusMessage.textContent = `${isXTurn ? 'X' : 'O'}'s turn`;
  }
}

function checkWin(currentClass) {
  return winningCombinations.some(combination => {
    return combination.every(index => {
      return cells[index].querySelector(`.${currentClass}`);
    });
  });
}

function isDraw() {
  return [...cells].every(cell => cell.classList.contains('taken'));
}

function showResult(message) {
  resultMessage.textContent = message;
  resultScreen.style.display = 'flex';
}

function restartGame() {
  isXTurn = true;
  statusMessage.textContent = "X's turn";
  cells.forEach(cell => {
    cell.textContent = ''; // Clear cell contents
    cell.classList.remove('taken');
    while (cell.firstChild) {
      cell.removeChild(cell.firstChild); // Remove any existing spans
    }
    cell.addEventListener('click', handleClick, { once: true });
  });
  resultScreen.style.display = 'none';
}

cells.forEach(cell => cell.addEventListener('click', handleClick, { once: true }));
newGameButton.addEventListener('click', restartGame);

// Initialize status message
statusMessage.textContent = "X's turn";