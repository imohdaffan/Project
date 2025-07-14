import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TicTacToeGUI extends JFrame implements ActionListener {
    private JButton[][] buttons = new JButton[3][3];
    private char currentPlayer = 'X';

    public TicTacToeGUI() {
        setTitle("Tic Tac Toe Game");
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(3, 3));

        initializeButtons();

        setVisible(true);
    }

    private void initializeButtons() {
        Font font = new Font("Arial", Font.BOLD, 60);
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                buttons[i][j] = new JButton("");
                buttons[i][j].setFont(font);
                buttons[i][j].setFocusPainted(false);
                buttons[i][j].addActionListener(this);
                add(buttons[i][j]);
            }
        }
    }

    public void actionPerformed(ActionEvent e) {
        JButton clickedBtn = (JButton) e.getSource();

        if (!clickedBtn.getText().equals("")) {
            return;
        }

        clickedBtn.setText(String.valueOf(currentPlayer));
        clickedBtn.setForeground(currentPlayer == 'X' ? Color.BLUE : Color.RED);

        if (checkForWin()) {
            JOptionPane.showMessageDialog(this, "🎉 Player " + currentPlayer + " wins!");
            resetBoard();
        } else if (isBoardFull()) {
            JOptionPane.showMessageDialog(this, "😅 It's a draw!");
            resetBoard();
        } else {
            currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
        }
    }

    private boolean isBoardFull() {
        for (JButton[] row : buttons) {
            for (JButton btn : row) {
                if (btn.getText().equals("")) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean checkForWin() {
        String p = String.valueOf(currentPlayer);

        // Rows and Columns
        for (int i = 0; i < 3; i++) {
            if (buttons[i][0].getText().equals(p) && buttons[i][1].getText().equals(p) && buttons[i][2].getText().equals(p))
                return true;
            if (buttons[0][i].getText().equals(p) && buttons[1][i].getText().equals(p) && buttons[2][i].getText().equals(p))
                return true;
        }

        // Diagonals
        if (buttons[0][0].getText().equals(p) && buttons[1][1].getText().equals(p) && buttons[2][2].getText().equals(p))
            return true;
        if (buttons[0][2].getText().equals(p) && buttons[1][1].getText().equals(p) && buttons[2][0].getText().equals(p))
            return true;

        return false;
    }

    private void resetBoard() {
        for (JButton[] row : buttons) {
            for (JButton btn : row) {
                btn.setText("");
            }
        }
        currentPlayer = 'X';
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new TicTacToeGUI());
    }
}
