import streamlit as st
from tennis.player import Player
from tennis.game import Game
from setup_logger import logger



if __name__ == "__main__":
    
    

    st.title("Tennis Game Score Display")

    st.markdown("""
        Terms used in Tennis for scores:
        - 0 : Love
        - 1 : Fifteen
        - 2 : Thirty
        - 3 : Forty
        """)

    player1_score = st.number_input("Enter score for Player 1", value=0)
    player2_score = st.number_input("Enter score for Player 2", value=0)

    # Player instances
    player1 = Player(name="Player1", score=player1_score)
    player2 = Player(name="Player2", score=player2_score)

    # Game instance
    game = Game(player1, player2)

    if st.button("Show Score"):
        try:
            result = game.calculate_score()
            
            # Display result with larger text size
            st.markdown(f"<h3 style='color: #4CAF50;'>Score: {result}</h3>", unsafe_allow_html=True)
        
        except Exception as e:
            logger.error(e)
            st.error(f"Error: {str(e)}")